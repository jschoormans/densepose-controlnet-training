import os 
from PIL import Image   

folder = 'data_folder/train_old'
newfolder = 'data_folder/train'

# lsit all images in the folder
images = os.listdir(folder)
# images = [i for i in images if '_densepose.jpg' not in i]

# sort alphabetically
images.sort()

print('we have {} images'.format(len(images)))

# loop over all images
for image in images:
    # open image
    im = Image.open(folder + '/' + image)
    # resize image
    # im = im.resize((512,512))
    # crop square center
    width, height = im.size
    new_width = min(width, height)
    new_height = min(width, height)
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    im = im.crop((left, top, right, bottom))
    im = im.resize((1024,1024))
    
    # save image
    im.save(newfolder + '/' + image)
    print('resized {}'.format(image))