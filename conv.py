import Image
import sys

print("Hi, I am image format converter :-) PNG <-> JPEG")
obj = sys.argv[1]
resp = str(input("Let's go? (y/n):"))
if resp == "n":
	print("Bye! :-(")
elif resp == "y":
	img = Image.open(obj)
	size = img.size
	print("Image Size:", size)
	image_format = img.format
	print("Old Image format:", image_format)
	form = str(image_format)
	if form == "PNG":
		img.save('test.jpg')
		print("Image saved in new format JPG ")
	elif form =="JPG":
		img.save('test.png')
		print("Image saved in new format PNG")
