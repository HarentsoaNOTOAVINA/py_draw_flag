from curses.textpad import rectangle
from xml.dom.expatbuilder import FILTER_ACCEPT
import matplotlib.pyplot as pl;
import matplotlib.patches as pt;

white = pt.Rectangle((0,0), width=5, height=10, facecolor='white', edgecolor='grey')
red = pt.Rectangle((5,5), width=10, height=5, facecolor='red')
green = pt.Rectangle((5,0), width=10, height=5, facecolor='green')
m,n = pl.subplots()
n.add_patch(white)
n.add_patch(red)
n.add_patch(green)
pl.axis("equal")
pl.show()