"""
Loads my matplotlibrc file and allows me to customize
additional aspects of my plots
"""
import os
from warnings import warn
import matplotlib as mpl
import matplotlib.pyplot as plt
path = os.path.dirname(os.path.abspath(__file__))
mpl.rc_params_from_file(path + "/matplotlibrc")


def change_style(society="utopia"):
    """
    Loads other fonts based on the professional society

    Parameters
    ----------
    society : str
        the name of the society
    """
    if society == "ams":
        font = "\usepackage{mathptmx},"
    elif society == "agu":
        font = "\usepackage[helvet]{sfmath},"
    elif society == "utopia":
        font = "\usepackage[adobe-utopia]{mathdesign},"
    else:
        warn("Style for society {society} not found. Using Computer Modern")
        font = ''
    with open(path + "/preamble.txt", "r") as preamble:
        mpl.rcParams['text.latex.preamble'] = preamble.read().format(font=font)


def pc2in(picas):
    """
    Converts picas to inches

    Parameters
    ----------
    picas : int or float
        dimension in picas

    Returns
    -------
    inches : float
        dimensions in inches
    """
    if picas not in [19, 27, 33, 39, 68]:
        warn("Not a standard AMS width")
    return picas / 6.


def fix_ticklabels():
    """
    Sets tick label typeface back to default while
    preserving the default behavior of the major
    label formatter
    """
    for attr in ["xaxis", "yaxis"]:
        fmt = getattr(plt.gca(), attr).get_major_formatter()
        fmt._usetex = False
        getattr(plt.gca(), attr).set_major_formatter(fmt)
