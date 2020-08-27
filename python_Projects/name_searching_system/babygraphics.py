"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000
Y_UNIT = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/MAX_RANK   # the y-axis unit


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * (width-2*GRAPH_MARGIN_SIZE)/len(YEARS)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0,
                           get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT, width=LINE_WIDTH, fill='black')
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW, font='times 15')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    color_num = 0    # set a variable for checking the color of line
    for name in lookup_names:
        color_num %= 4
        if name in name_data:
            d = name_data[name]
            x1 = 0      # x position for the first point
            y1 = 0      # y position for the first point
            for i in range(len(YEARS)):  # when no rank in specific year of searching names, give *
                if str(YEARS[i]) not in d:
                    d[str(YEARS[i])] = "*"
            for i in range(len(YEARS)):
                if i == 0:
                    x1 = get_x_coordinate(CANVAS_WIDTH, i)
                    if d[str(YEARS[i])] == "*":
                        y1 = GRAPH_MARGIN_SIZE + MAX_RANK * Y_UNIT
                    else:
                        y1 = GRAPH_MARGIN_SIZE + int(d[str(YEARS[i])]) * Y_UNIT
                    canvas.create_text(x1 + TEXT_DX, y1, text=f'{name} {d[str(YEARS[i])]}', anchor=tkinter.SW,
                                       font='times 12', fill=COLORS[color_num])
                else:
                    x2 = get_x_coordinate(CANVAS_WIDTH, i)
                    if d[str(YEARS[i])] == "*":
                        y2 = GRAPH_MARGIN_SIZE + MAX_RANK * Y_UNIT
                    else:
                        y2 = GRAPH_MARGIN_SIZE + int(d[str(YEARS[i])]) * Y_UNIT
                    canvas.create_text(x2 + TEXT_DX, y2, text=f'{name} {d[str(YEARS[i])]}', anchor=tkinter.SW,
                                       font='times 12', fill=COLORS[color_num])
                    canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[color_num])
                    x1 = x2
                    y1 = y2
            color_num += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
