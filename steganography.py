# Import the required library
from PIL import Image
import stepic


def encode():
    im = Image.open('goldie.jpg')
    languages = open("sample.txt", 'rb')

    # using join() + ord() + format()
    # Converting String to binary
    # res = ''.join(format(ord(i), 'b') for i in languages.read())
    res = languages.read()

    # Encode some text into your Image file and save it in another file
    im1 = stepic.encode(im, res)
    im1.save('goldie_cool.jpeg', 'PNG')

    # Now is the time to check both images and see if there is any visible changes
    im1 = Image.open('goldie_cool.jpeg')
    im1.show()


def decode():
    # Decode the image so as to extract the hidden data from the image
    im2 = Image.open('goldie_cool.jpeg')
    stego_image = stepic.decode(im2)
    print(f'decoded output: {stego_image}')


choice = int(input("1. Encode, 2. Decode\n"))
if choice >= 2:
    decode()
else:
    encode()
