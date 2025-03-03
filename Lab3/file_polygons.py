"""
Name(s):
CS105
Lab 3

This program draws polygons in a window from data read from a file.
Each line of the file has red, blue, green values for the color of the
polygon followed by the coordinates for the vertices of the polygon as
x, y values. The numbers on each line are separated by spaces.


"""
from graphics2 import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BORDER = 30


def main():
    # Enter file name and open to read

    
    # Create window where polygons will be drawn
    window = GraphWin("File Polygons", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('white')
    

      
main()