import os, sys
import time
from PIL import Image, ImageDraw, ImageFont
from pygifsicle import optimize

# This script generates a GIF that counts down the seconds from an arbitrary time to 0. 
# To generate a GIF, call main(t) with the amount of seconds you would like to count down from.
# Calling main(90) results in a timer counting down from 1:30.

# The different official AIESEC colours, as can be found in the Blue Book.
colours = {
    'Blue':'#037FF3FF',
    'White':'#F3F4F7FF',
    'Orange':'#F48924FF',
    'Turquois':'#0A8EA0FF',
    'Transparent':'#FFFFFF00',
    'Grey':'#52565E'
}

# Statically declare height and width of gif
width = 1000
height = int(width * 0.35)

# Creates a virtual image. Does *not* write to the disk. 
# Param: The text that is printed in the picture.
def create_image(background_colour):
    img = Image.new('RGBA', (width, height), color=colours.get(background_colour))
    return img

# Inserts text into image.
def draw_on_image(img, text, text_colour):
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('/Library/Fonts/Lato-Black.ttf', height)
    w, h = d.textsize(text, font=fnt)
    d.text(
        ((width-w)/2,-height/10), 
        text, 
        font=fnt,
        fill=colours.get(text_colour)
        )

# Saves a GIF made up of different frames to the disk.
# Input: an array of frames.
def save_gif(frames, name):
    filename = 'out/{}.gif'.format(name)
    frames[0].save(
        filename, 
        format='GIF', 
        append_images=frames[1:], 
        save_all=True, 
        duration=1000, 
        fps=1,
        #transparency=0
    )
    # Optimize GIF
    optimize(filename)

def generate_gif(t, background_colour, text_colour):
    frames = []
    for i in range(t, -1, -1):
        mins, secs = divmod(i, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        # Creates new, empty frame
        new_frame = create_image(background_colour)
        # Inserts current countdown state into frame
        draw_on_image(new_frame, timeformat, text_colour)
        frames.append(new_frame)
    save_gif(frames, str(t))
    print('Finsih')