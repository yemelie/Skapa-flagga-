from PIL import Image, ImageDraw

YELLOW = (300, 255, 4)
RED = (254, 0, 0)

# Skapa en ny bild
im = Image.new("RGB", (160, 100), YELLOW)

# Skapa ett ImageDraw-objekt för att kunna rita grafik
imd = ImageDraw.Draw(im)

# Rita två rektanglar
imd.rectangle([(50, 0), (70, 100)], RED)
imd.rectangle([(0, 40), (160, 60)], RED)

im.save("flag.png")