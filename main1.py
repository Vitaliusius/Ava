from PIL import Image

ava = Image.open("monro.jpg")
red, green, blue = ava.split()



coordinates = (30, 0, red.width, red.height)
cropred1 = red.crop(coordinates)

coordinates = (15, 0, red.width-15, red.height)
cropred2 = red.crop(coordinates)

red_end = Image.blend(cropred1, cropred2, 0.5)


coordinates = (0, 0, blue.width-30, blue.height)
cropblue1 = blue.crop(coordinates)

coordinates = (15, 0, blue.width-15, blue.height)
cropblue2 = blue.crop(coordinates)

blue_end = Image.blend(cropblue1, cropblue2, 0.5)


coordinates = (15, 0, green.width-15, green.height)
green_end = green.crop(coordinates)

full_image = Image.merge("RGB",(red_end,green_end,blue_end))

full_image.thumbnail((80,80))
full_image.save("ava.jpg")
























