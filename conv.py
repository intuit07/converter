import Image
import sys

print ("Hi, I am converter format of images :-) PNG <-> JPEG")
obj = sys.argv[1]
resp = str(raw_input("Let's go? (y/n):"))
if resp == "n":
	print "By! :-("
elif resp == "y":
	img = Image.open(obj)
	size = img.size
	print "Size Image:", size	
	format = img.format
	print "Old format Image:", format
	form = str(format)
	if form == "PNG" :			
		img.save('test.jpg')
		print "Image saved in new format JPG "
	elif form =="JPG" :			
		img.save('test.png')
		print "Image saved in new format PNG"
