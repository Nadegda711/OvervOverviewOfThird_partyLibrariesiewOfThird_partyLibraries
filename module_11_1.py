from PIL import Image, ImageFilter

#-----------------------------------------------------------------------------------------------------------
image_path = "C:/Users/Надежда/Pictures/24acef8b3a6a45d7239480bcc4ff0193.jpg" # Полный путь к изображению

image = Image.open(image_path) # загружаем изображение

original_image = image.copy() # сохранение оригинала для восстановления

bw_image = image.convert('L') # сделать изображение черно-белым
bw_image.save("C:/Users/Надежда/Pictures/новыйтигр.jpg")# Сохранение результата под новым именем
# bw_image.show()

radius = 3  # Радиус размытия
percent = 500 # Процент повышения резкости
threshold = 10  # Порог изменения
sharpened_image = bw_image.filter(ImageFilter.UnsharpMask(radius, percent, threshold))
sharpened_image.save("C:/Users/Надежда/Pictures/новыйтигрконтур.jpg")
# sharpened_image.show()

radius = 20
blurred_image = image.filter(ImageFilter.GaussianBlur(radius)) #размытие с параметрами
blurred_image.save("C:/Users/Надежда/Pictures/размытыйтигр.jpg")
# blurred_image.show()

image = original_image # Восстановление оригинала
# image.show()  # Показываем восстановленное изображение

#--------------------------------------------------------------------------------------------------------------
import pandas as pd
tefia = "C:/Users/Надежда/Desktop/бренд,наименование,артикул,цена,опи.csv"
df = pd.read_csv(tefia)
print(df.head())  # Покажет первые 5 строк таблицы
print('---------------------------------------------------------------------------')
print(df.info())
print('---------------------------------------------------------------------------')
print(df.describe()) #статистика числовых столбцов
print('---------------------------------------------------------------------------')
print(df['наименование'])
print('---------------------------------------------------------------------------')
# Добавление нового столбца
df['количество'] = ['50', "", ""]  # Замените 'значение' на нужные данные

# Сохранение изменений в тот же файл
tefia1 = df.to_csv("C:/Users/Надежда/Desktop/копия_накладной.csv", index=False)
print(tefia1)
