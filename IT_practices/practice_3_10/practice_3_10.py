import cv2
import os

# Отримання шляху до поточного каталогу
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "test_image.jpg")

# Завантаження зображення
image = cv2.imread(image_path)

# Перевірка чи зображення завантажено
if image is None:
    print("Зображення не знайдено за шляхом:", image_path)
    exit()

# Відображення
cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ----- 1. Фільтрація -----

# Гаусове розмиття (усуває шум, згладжує зображення)
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# Медіанне розмиття (ефективне проти шуму типу "сіль і перець")
median_blur = cv2.medianBlur(image, 5)

# ----- 2. Зміна розмірності -----

# Зменшення розміру в 2 рази
small = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# Збільшення розміру в 2 рази
large = cv2.resize(image, (0, 0), fx=2.0, fy=2.0)

# ----- 3. Відображення -----

cv2.imshow("Original", image)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)
cv2.imshow("Smaller Image", small)
cv2.imshow("Larger Image", large)

cv2.waitKey(0)
cv2.destroyAllWindows()

