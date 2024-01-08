# Execute on root project directory

import glob
from PIL import Image, ImageDraw

files=glob.glob("ddpm-shoes-128-v3/samples/*.png")
files=sorted(files)

img=[Image.open(filename) for filename in files]

# filename,duration=milliseconds
img[0].save('train.gif',save_all=True,append_images=img[1:],optimize=False,duration=500)