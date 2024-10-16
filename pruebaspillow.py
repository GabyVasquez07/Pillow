from PIL import Image, ImageFilter
opcion = int(input("Por favor ingrese un numero de acuerdo con lo que quiere ver: "))

# Abrimos una imagen
imagen = Image.open('11oct\miimagen.jpg')

if opcion == 1:
    # 1. BLUR: Aplica un desenfoque básico
    imagenborrosa = imagen.filter(ImageFilter.BLUR)
    imagenborrosa.show()
elif opcion == 2:
    # 2. CONTOUR: Resalta los bordes y las líneas
    contorno_imagen = imagen.filter(ImageFilter.CONTOUR)
    contorno_imagen.show()
elif opcion == 3:
    # 3. DETAIL: Mejora el detalle de la imagen
    imagendetalle = imagen.filter(ImageFilter.DETAIL)
    imagendetalle.show()
elif opcion == 4:
    # 4. EDGE_ENHANCE: Mejora la definición de los bordes
    mejoradeborde = imagen.filter(ImageFilter.EDGE_ENHANCE)
    mejoradeborde.show()
elif opcion == 5:
    # 5. EMBOSS: Aplica un efecto de relieve
    relieve = imagen.filter(ImageFilter.EMBOSS)
    relieve.show()
elif opcion == 6:
    # 6. SHARPEN: Aumenta la nitidez de la imagen
    nitidez = imagen.filter(ImageFilter.SHARPEN)
    nitidez.show()
elif opcion == 7:
    # 7. GaussianBlur (con radio 5): Aplica un desenfoque gaussiano
    desenfoque = imagen.filter(ImageFilter.GaussianBlur(radius=5))
    desenfoque.show()
elif opcion == 8:
    #------------------------------------------------------------------------------
    from PIL import Image, ImageDraw, ImageFont

    # Creamos una imagen nueva en blanco (fondo blanco)
    width, height = 400, 400
    image = Image.new('RGB', (width, height), 'white')

    # Creamos un objeto ImageDraw
    dibujar = ImageDraw.Draw(image)

    # Dibujamos un rectángulo azul
    dibujar.rectangle([50, 50, 200, 200], fill='blue', outline='black', width=3)

    # Dibujamos un círculo rojo
    dibujar.ellipse([220, 50, 370, 200], fill='red', outline='black', width=3)

    # Dibujamos una línea verde
    dibujar.line((50, 250, 250, 250), fill='green', width=5)

    # Dibujamos un texto en la imagen (se puede personalizar la fuente)
    try:
        font = ImageFont.truetype("verdana.ttf", 24)  # Nos aseguremos que arial esté disponible
    except IOError:
        font = ImageFont.load_default()  # Usamos la fuente predeterminada si no se encuentra arial

    dibujar.text((100, 250), "Hola mundo pillow :P", font=font, fill='black')

    # Mostrar la imagen resultante
    image.show()


