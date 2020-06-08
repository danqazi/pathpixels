import sys
import os
import pyvips

path = os.getcwd()
images = os.listdir(path)
for image in images:
    sys.stdout.write('Processing %s\n' % (image))
    sys.stdout.write('Loading %s\n' % (image))
    # load_image = pyvips.Image.new_from_file(image, access='sequential')



