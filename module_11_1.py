from PIL import Image

# Укажите полный путь к изображению
image_path = "C:/Users/Надежда/Pictures/24acef8b3a6a45d7239480bcc4ff0193.jpg"
# загружаем изображение
image = Image.open(image_path)

# сохранение оригинала для восстановления
original_image = image.copy()

# сделать изображение черно-белым
bw_image = image.convert('L')

# Сохранение результата под новым именем, чтобы цветное изображение не изменилось
bw_image.save("C:/Users/Надежда/Pictures/новыйтигр.jpg")
# Восстановление оригинала
image = original_image
image.show()  # Показываем восстановленное изображение


