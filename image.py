from PIL import Image

img = Image.open('Capture1.jpg')
image = Image.open('Capture3.jpg')
listed = list(img.getdata())
listed2 = list(image.getdata())
img2 = Image.new('RGB', (img.width, img.height))
img3 = Image.new('RGB', (img.width*2, img.height))
new_image = []

# Merging images 1
for i in range(0, img.width*img.height, img.width):
        new_row = listed[img.width+i:i:-1]+listed2[img.width+i:i:-1]
        new_image.extend(new_row)
img3.putdata(new_image)
img3.save('cap_resized.jpg')

#merging images 2
for i in range(len(listed)):
        listed[i] = ((listed[i][0] + listed2[i][2])//2, (listed[i][1] + listed2[i][1])//2, (listed[i][2] + listed2[i][2])//2)
img2.putdata(listed)
img2.save('cap2.jpg')
img = Image.open('trial2.jpg')
listed = list(img.getdata())
new_image = []
#mirroring image
for i in range(0, img.width * img.height, img.width):
        new_row = listed[img.width+i:i:-1]
        new_image.extend(new_row)

img4 = Image.new('RGB', (img.width, img.height))
img4.putdata(new_image)
img4.save('img_mirrored.jpg')
