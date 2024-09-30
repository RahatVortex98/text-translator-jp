from PIL import Image,ImageFilter

# img = Image.open('./Pokedex/charmander.jpg')

# filtered_img = img.filter(ImageFilter.BLUR)

# filtered_img=img.convert('L')

# crooked=filtered_img.rotate(90)
# crooked.save("rotated.png",'png')

# resize = filtered_img.resize((200,300))
# resize.save("resize.png",'png')

# filtered_img.save("grey.png",'png')


# box=(100,100,400,400)
# region = filtered_img.crop(box)
# region.save("croped.png",'png')

# filtered_img.show()

# print(img.mode)


img = Image.open('./Pokedex/astro.jpg')
img.thumbnail((400,400))
img.save('thumgnil.jpg')
 