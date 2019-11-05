# Write filtergram.py. You should import your filters file into this file! Your program should have a main function. Within that main function, you should call the functions you just defined in filters.py to do the following:
import filters

def main():
    filename = "bts_picture.jpg"
    img = filters.load_img(filename)
    newBTS = filters.obamicon(img)
    filters.save_img(newBTS, "filename2.jpg")

# 1. Load an image from your computer. (You'll need to find and download an image and put it in the same folder as your program!)
# 2. Save the image to a new file on your computer. This image will look identical to the original, but that's okay for now!
if __name__ == "__main__":
    main()
