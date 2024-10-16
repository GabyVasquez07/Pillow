from PIL import Image

# Abrir una imagen
imagen = Image.open('Pillow.png')

#Convertir el formato de la imagen
imagen = imagen.convert("RGB")

# Guardar la imagen 
imagen.save('imagen_nueva.jpg')

# Redimensionar la imagen
nueva_tamano = (400, 300)
imagen_redimensionada = imagen.resize(nueva_tamano)
imagen_redimensionada.save('imagen_redimensionada.jpg')

# Rotar
imagen_rotada = imagen.rotate(90)
imagen_rotada.save('imagen_rotada.jpg')

# Recortar
caja_recorte = (100, 100, 400, 400) #(left, upper, right, lower)
imagen_recortada = imagen.crop(caja_recorte)
imagen_recortada.save('imagen_recortada.jpg')

#Mostrar la Imagen
imagen.show()
