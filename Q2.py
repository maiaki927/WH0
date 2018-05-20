import sys

sys.path.append("./venv/lib/python3.6/site-packages")
from PIL import Image

import os
import sys


#print(sys.argv[1])
q=sys.argv[1]
if(q[-1]=='/'):
    ax=sys.argv[1]+'westbrook.jpg'
else:
    ax=sys.argv[1]+'/westbrook.jpg'

im = Image.open(ax)
xx,yy=im.size
c = Image.new("RGB", (xx, yy))
width = im.size[0]
height = im.size[1]
im = im.convert('RGB')
array = []
for x in range(width):
    for y in range(height):
        r, g, b = im.getpixel((x,y))
        c.putpixel([x, y], (int(r/2), int(g/2), int(b/2)))

c.show()
c.save("Q2.jpg")
