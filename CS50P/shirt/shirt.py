import sys
import os
from PIL import Image
from PIL import ImageOps

try:
    open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

name1, end1 = os.path.splitext(sys.argv[1])
name2, end2 = os.path.splitext(sys.argv[2])
end1_case = end1.lower()
end2_case = end2.lower()

if end1_case not in [".jpg", ".jpeg", ".png"] or end2_case not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")

if end1_case != end2_case:
    sys.exit("Input and output have different extensions")

shirt = Image.open("shirt.png")
image = Image.open(sys.argv[1])
size = shirt.size
image2 = ImageOps.fit(image, size)
image2.paste(shirt, mask=shirt)
image2.save(sys.argv[2])
