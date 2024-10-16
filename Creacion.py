from PIL import Image, ImageDraw, ImageFont

# Crear una nueva imagen (ancho, alto) con fondo blanco
ancho, alto = 400, 400
color_fondo = (255, 255, 255)  # Color blanco
imagen = Image.new("RGB", (ancho, alto), color_fondo)

# Crear un objeto de dibujo
dibujo = ImageDraw.Draw(imagen)

# Dibujar un rectángulo azul
color_rectangulo = (0, 0, 255)  # Color azul
dibujo.rectangle([50, 50, 350, 150], fill=color_rectangulo)

# Dibujar un círculo rojo
color_circulo = (255, 0, 0)  # Color rojo
dibujo.ellipse([150, 200, 250, 300], fill=color_circulo)

# Agregar texto negro
color_texto = (0, 0, 0)  # Color negro
fuente = ImageFont.load_default()  # Usar fuente predeterminada
dibujo.text((150, 50), "Hola, Pillow!", fill=color_texto, font=fuente)

# Guardar la imagen creada
imagen.save("imagen_creada.jpg")

# Mostrar la imagen
imagen.show()
