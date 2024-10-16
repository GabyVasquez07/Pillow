from PIL import Image

from PIL import Image

# Abrir la imagen original
imagen = Image.open('Pillow.png')
#Convertir el formato de la imagen
imagen = imagen.convert("RGB")

# Reflejar la imagen horizontalmente
imagen_reflejada_horizontalmente = imagen.transpose(Image.FLIP_LEFT_RIGHT)

# Guardar la imagen reflejada
imagen_reflejada_horizontalmente.save('imagen_reflejada_horizontalmente.jpg')

# Mostrar la imagen reflejada
imagen_reflejada_horizontalmente.show()
 
 # Reflejar la imagen verticalmente
imagen_reflejada_verticalmente = imagen.transpose(Image.FLIP_TOP_BOTTOM)

# Guardar la imagen reflejada
imagen_reflejada_verticalmente.save('imagen_reflejada_verticalmente.jpg')

# Mostrar la imagen reflejada
imagen_reflejada_verticalmente.show()

# Rotar la imagen 90 grados en sentido antihorario
imagen_rotada_90 = imagen.transpose(Image.ROTATE_90)

# Guardar la imagen rotada
imagen_rotada_90.save('imagen_rotada_90.jpg')

# Mostrar la imagen rotada
imagen_rotada_90.show()

# Rotar la imagen 180 grados
imagen_rotada_180 = imagen.transpose(Image.ROTATE_180)

# Guardar la imagen rotada
imagen_rotada_180.save('imagen_rotada_180.jpg')

# Mostrar la imagen rotada
imagen_rotada_180.show()

# Rotar la imagen 270 grados en sentido antihorario
imagen_rotada_270 = imagen.transpose(Image.ROTATE_270)

# Guardar la imagen rotada
imagen_rotada_270.save('imagen_rotada_270.jpg')

# Mostrar la imagen rotada
imagen_rotada_270.show()

