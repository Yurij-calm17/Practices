import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LeakyReLU
from tensorflow.keras.utils import to_categorical

# 1. Генерація даних (як у Завданні 2)
np.random.seed(42)
n_samples = 1000
X = np.random.rand(n_samples, 4) * 100
y = []
for row in X:
    if row[0] > 70 and row[1] > 60:
        y.append(1)
    elif row[2] > 50:
        y.append(2)
    else:
        y.append(0)
y = np.array(y)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

y_train_cat = to_categorical(y_train, num_classes=3)
y_test_cat = to_categorical(y_test, num_classes=3)

# 2. Функція для побудови і тренування моделей
def build_and_train_model(activation_name):
    model = Sequential()
    if activation_name == 'leaky_relu':
        model.add(Dense(32, input_shape=(4,)))
        model.add(LeakyReLU(alpha=0.1))
        model.add(Dense(16))
        model.add(LeakyReLU(alpha=0.1))
    else:
        model.add(Dense(32, activation=activation_name, input_shape=(4,)))
        model.add(Dense(16, activation=activation_name))
    model.add(Dense(3, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    history = model.fit(X_train, y_train_cat, epochs=50, batch_size=16, verbose=0, validation_split=0.2)
    return history

# 3. Перелік функцій активації
activations = ['relu', 'sigmoid', 'tanh', 'leaky_relu']
histories = {}

for act in activations:
    print(f"🔁 Навчання моделі з активацією: {act}")
    histories[act] = build_and_train_model(act)

# 4. Побудова графіків
plt.figure(figsize=(14, 6))

for i, act in enumerate(activations):
    plt.subplot(1, 2, 1)
    plt.plot(histories[act].history['val_accuracy'], label=act)
    plt.title("Validation Accuracy")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(histories[act].history['val_loss'], label=act)
    plt.title("Validation Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()

plt.tight_layout()
plt.show()

#Порівняння функцій активації показало, що найкращу точність та швидкість збіжності демонструє ReLU.
Функції Sigmoid та Tanh мають повільнішу динаміку навчання.
LeakyReLU показала стабільну роботу, демонструючи гарну продуктивність завдяки уникненню проблеми нульових градієнтів.