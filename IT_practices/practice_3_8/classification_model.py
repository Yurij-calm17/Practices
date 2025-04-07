import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# 1. Генерація даних
np.random.seed(42)
n_samples = 1000
X = np.random.rand(n_samples, 4) * 100  # 4 ознаки
y_raw = []

# Просте логічне правило для створення класів
for row in X:
    if row[0] > 70 and row[1] > 60:
        y_raw.append(1)  # DDoS
    elif row[2] > 50:
        y_raw.append(2)  # Port scanning
    else:
        y_raw.append(0)  # Немає атаки

y = np.array(y_raw)

# 2. Масштабування та розбиття
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 3. One-hot кодування
y_train_cat = to_categorical(y_train, num_classes=3)
y_test_cat = to_categorical(y_test, num_classes=3)

# 4. Побудова моделі
model = Sequential([
    Dense(32, activation='relu', input_shape=(4,)),
    Dense(16, activation='relu'),
    Dense(3, activation='softmax')  # 3 класи
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 5. Навчання
history = model.fit(X_train, y_train_cat, epochs=50, batch_size=16, validation_split=0.2, verbose=0)

# 6. Оцінка
loss, acc = model.evaluate(X_test, y_test_cat, verbose=0)
print(f"Test Accuracy: {acc:.2f}")

# 7. Прогноз і аналіз
y_pred_probs = model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 8. Візуалізація матриці неточностей
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
plt.imshow(cm, cmap='Blues')
plt.title("Матриця неточностей")
plt.xlabel("Передбачено")
plt.ylabel("Факт")
plt.xticks([0, 1, 2], ['No Attack', 'DDoS', 'Scan'])
plt.yticks([0, 1, 2], ['No Attack', 'DDoS', 'Scan'])
for i in range(3):
    for j in range(3):
        plt.text(j, i, cm[i, j], ha='center', va='center', color='black')
plt.colorbar()
plt.tight_layout()
plt.show()
