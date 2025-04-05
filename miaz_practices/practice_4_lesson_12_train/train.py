import torch
import torch.nn as nn
import torchvision
from torchvision import datasets, transforms, models
from torch.optim import lr_scheduler
import time
import copy
import os

# 1. Підготовка даних
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Каталог скрипта: {script_dir}")
data_dir = script_dir
# data_dir = 'C:\\Users\\yurav\\OneDrive\\Desktop\\training model'  # Замість цього шляху вкажіть шлях до вашого набору даних
data_transforms = {
    'train': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], 
                             [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], 
                             [0.229, 0.224, 0.225])
    ]),
}

if __name__ == "__main__":
    import torch.multiprocessing
    torch.multiprocessing.freeze_support() 
    image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x), 
                                            data_transforms[x])
                    for x in ['train', 'val']}
    dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], 
                                                batch_size=32, shuffle=True, num_workers=4)
                for x in ['train', 'val']}
    dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}
    class_names = image_datasets['train'].classes

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # 2. Завантаження попередньо навченого ResNet
    model = models.resnet50(pretrained=True)

    # 3. Заморожування шарів
    for param in model.parameters():
        param.requires_grad = False

    # 4. Заміна вихідного шару
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, len(class_names))

    model = model.to(device)

    # 5. Визначення критерію та оптимізатора
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.fc.parameters(), lr=0.001)

    # 6. Навчання моделі
    num_epochs = 25
    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0
    since = time.time()

    for epoch in range(num_epochs):
        print(f'Epoch {epoch+1}/{num_epochs}')
        print('-' * 10)
        
        # Кожен епох розділений на тренувальний та валідаційний
        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()  # режим навчання
            else:
                model.eval()   # режим валідації
            
            running_loss = 0.0
            running_corrects = 0
            
            # Ітерація по даних
            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)
                
                optimizer.zero_grad()
                
                # Прямий прохід
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)
                    
                    # Зворотний прохід + оптимізація тільки в тренувальному режимі
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()
                
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)
            
            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = running_corrects.double() / dataset_sizes[phase]
            
            print(f'{phase} Loss: {epoch_loss:.4f} Acc: {epoch_acc:.4f}')
            
            # Збереження найкращої моделі
            if phase == 'val' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())
        
        print()
        
    time_elapsed = time.time() - since
    print(f'Training complete in {time_elapsed // 60:.0f}m {time_elapsed % 60:.0f}s')
    print(f'Best val Acc: {best_acc:4f}')

    # Завантаження найкращої моделі
    model.load_state_dict(best_model_wts)

    # Збереження моделі
    torch.save(model.state_dict(), 'fine_tuned_resnet.pth')