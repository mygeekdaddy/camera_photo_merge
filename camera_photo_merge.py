mport clipboard
from PIL import Image
import console
import photos
import webbrowser

console.clear()

console.alert("Pick first image", "", "Select")
img1 = photos.pick_asset()
img1 = img1.get_image()

console.alert("Pick second image", "", "Select")
img2 = photos.pick_asset()
img2 = img2.get_image()

console.show_activity()



w1, h1 = img1.size
w2, h2 = img2.size

# Set the width and height of each image
img1_w = img1.size[0]
img1_h = img1.size[1]
img2_w = img2.size[0]
img2_h = img1.size[1]

def image_merge(img):
	if (img1_w * 1.0) / img1_h > 1:
		print("Landscape screenshot...")
		# Landscape screenshot
		background = Image.new('RGB', ((img1_w+20),  ((img1_h*2)+30)), (88,88,88))
		print ("Generating image...")
		background.paste(img1,(10,10))
		background.paste(img2,(10,(img1_h+20)))
		# background.show()
		photos.save_image(background)
		print ("Image saved")	
	else:
		print ("Portrait screenshot...")
		#(1536, 2048)
		#Portrait screenshot
		background = Image.new('RGB', (((img1_w*2)+30),(img1_h+20)), (88, 88, 88))
		print ("Generating image...")
		background.paste(img1,(10,10))
		background.paste(img2,((img1_w+20),10))
		# background.show()
		photos.save_image(background)
		print("Image saved")

if img1_w == img2_w:
	image_merge(img1)
	print("Done...")
	webbrowser.open_new('launcher://crash')
else:
	console.alert("Incorrect image ratio", "", "Ok")
	webbrowser.open('launcher://crash')