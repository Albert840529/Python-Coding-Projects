"""
SC101 - Assignment3
Adapted from Nick Parlante's Ghost assignment by
Jerry Liao.

-----------------------------------------------

TODO:
"""
import math
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    """
    color_distance = math.sqrt((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red_total = 0
    blue_total = 0
    green_total = 0
    for i in range(len(pixels)):      # count the sum of r,g,b
        red_total += pixels[i].red
        blue_total += pixels[i].blue
        green_total += pixels[i].green
    rgb = [int(red_total/len(pixels)), int(green_total/len(pixels)), int(blue_total/len(pixels))]
    # return the rgb as list [red, green, blue]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    best = pixels[0]
    rgb = get_average(pixels)
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    shortest_distance = get_pixel_dist(pixels[0], red, green, blue)
    for i in range(len(pixels)):   # compare different photos and find the shortest color distance
        color_distance = get_pixel_dist(pixels[i], red, green, blue)
        if shortest_distance > color_distance:
            shortest_distance = color_distance
            best = pixels[i]
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    for x in range(width):
        for y in range(height):  # need to do this process for every pixels in the picture
            pixels = []
            for i in range(len(images)):  # add each pixels of different images into one list
                img = images[i]
                pixel = img.get_pixel(x, y)
                pixels.append(pixel)
            best = get_best_pixel(pixels)    # find best pixel
            new_pixel = result.get_pixel(x, y)
            new_pixel.red = best.red
            new_pixel.green = best.green
            new_pixel.blue = best.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
