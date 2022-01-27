import sys
from PIL import Image
import json

im = Image.open(sys.argv[1], 'r')
outfile = sys.argv[1].replace('.bmp', '.sts')
f = open(outfile, "w")

width, height = im.size

pix_val = list(im.getdata())

f.write(str(width) + " " + str(height) + "\n")
f.write(json.dumps(pix_val))
f.close()