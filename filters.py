# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    img = Image.open(filename)
    return img
# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(img):
    img.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(img, filename):
    img.save(filename, "jpeg")
    show_img(img)
# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img):
    darkBlue = (0, 51, 76)
    lightBlue = (217, 26, 33)
    red = (112, 150, 158)
    yellow = (252, 227, 166)
    newPixels = []
    #list of pixels called pixels
    pixels = img.getdata()
#If you add all three values together, you get a number that correlates to how "light" the color is, also known as its intensity
    for p in pixels:
        # redPixels = pixels[p][0]
        # greenPixels = pixels[p][1]
        # bluePixels = pixels[p][2]
        intensity = p[0] + p[1] + p[2]

        print(intensity)

        if intensity < 182:
            newPixels.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            newPixels.append(red)
        elif intensity >= 364 and intensity < 546:
            newPixels.append(lightBlue)
        else:
            newPixels.append(yellow)

    newImage = Image.new("RGB", img.size)

    newImage.putdata(newPixels)

    return newImage

    # newImage.show()


#     im = Image.open("bts_picture")
#     colorpixels = list(im.getdata())
#     list_length=len(colorpixels)
#
#     for i in range(list_length):
#         redapples = colorpixels[i][0]
#         blueapples = colorpixels[i][1]
#         greenapples = colorpixels[i][2]
#         sum = redapples + blueapples + greenapples
#
#         print(sum)
#
#         if sum < 182:
# 		colorpixels[i] = darkBlue
#         elif sum >= 182 and sum < 364:
# 		colorpixels[i] = red
#         elif sum >= 364 and sum< 546:
# 		colorpixels[i] = lightBlue
#         else:
# 		colorpixels[i]= yellow
#
# im.putdata(colorpixels)
#
# im.show()


# elif 364 < intensity < 546:
#     intensity = (112, 150, 158)
# elif: 182 < intensity < 364:
#     intensity = (217, 26, 33)
# else: intensity < 182:
#     intensity = (0, 51, 76)
\
