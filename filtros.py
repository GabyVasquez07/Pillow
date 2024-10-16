from PIL import Image, ImageFilter

# Abrir la imagen original
imagen = Image.open('Pillow.png')
#Convertir el formato de la imagen
imagen = imagen.convert("RGB")

# Aplicar diferentes filtros
imagen_desenfocada = imagen.filter(ImageFilter.BLUR)
imagen_desenfocada.save('imagen_desenfocada.jpg')

imagen_contorno = imagen.filter(ImageFilter.CONTOUR)
imagen_contorno.save('imagen_contorno.jpg')

imagen_detalle = imagen.filter(ImageFilter.DETAIL)
imagen_detalle.save('imagen_detalle.jpg')

imagen_borde_mejorado = imagen.filter(ImageFilter.EDGE_ENHANCE)
imagen_borde_mejorado.save('imagen_borde_mejorado.jpg')

imagen_relieve = imagen.filter(ImageFilter.EMBOSS)
imagen_relieve.save('imagen_relieve.jpg')

imagen_nitida = imagen.filter(ImageFilter.SHARPEN)
imagen_nitida.save('imagen_nitida.jpg')

imagen_desenfoque_gaussiano = imagen.filter(ImageFilter.GaussianBlur(radius=5))
imagen_desenfoque_gaussiano.save('imagen_desenfoque_gaussiano.jpg')

print("Filtros aplicados y guardados.")
