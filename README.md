# Fun with LaTeX and matplotlib

The purpose of this repository is to change fonts in my matplotlib
figures so that the math looks nicer and the fonts match what appears
in the manuscript text. The titles, axis labels, and tick labels are
kept as [DejaVu Sans typeface](https://en.wikipedia.org/wiki/DejaVu_fonts) (the current default for matplotlib 2x).

## Getting started

Add plotting as a submodule to your Git repository
```
git submodule add <url> plotting
git submodule update --init --recursive --remote
```

## Using plotting
Below is the most basic usage. The defaults I have set are used
and a plot is generated.

```python
from plotting.plotting import *
import numpy as np

t = np.arange(0.0, 1.0 + 0.01, 0.01)
s = np.cos(4 * np.pi * t) + 2

plt.plot(t, s)
plt.xlabel(r'\textbf{time} (s $^\text{-1}$)')
plt.ylabel(r'\textit{voltage} (mV)',fontsize=10)
plt.title(r"\LaTeX\ is awesome "
          r"$\displaystyle\sum_{n=\text{1}}^\infty\frac{-e^{i\pi}}{\text{2}^n}$!",
          fontsize=12, color='gray')
plt.text(0.1, 2.4,
         r" $\displaystyle\frac{\partial u}{\partial t} - \beta yv = 0$\newline"
         r"$\displaystyle\frac{\partial v}{\partial t} + \beta y u + \frac{\partial \Phi}{\partial y} = 0$",
         fontsize=10)
plt.subplots_adjust(top=0.8)
plt.show()
```

**Note**: If you did not clone the code as a submodule and you just copied the `plotting.py` script,
you will need to change the import from `from plotting.plotting import *` to `from plotting import *`.

*This example is based on the one included in [Text rendering With LaTeX](https://matplotlib.org/users/usetex.html).*

### Fixing the tick labels
When matplotlib is configured to use LaTeX, it sets the tick labels to math mode by
default. Why? No Idea. To change the tick labels back to their default behavior,
add a call to `fix_ticklabels` before calling `plt.savefig` or `plt.show`.

### Changing the font to match a different society
By default, plotting uses [Utopia Regular with Math Design](http://www.tug.dk/FontCatalogue/utopia-mathdesign/).
However, AMS and AGU use different fonts. To change this, call `change_style`.
`change_style` takes the keyword `society` which can be set to the following
* `ams` - Loads a Times New Roman like font to be used for AMS publications
* `agu` - Loads Helvetica, which is close to what AGU is now using
* `utopia` - My personal favorite option

Setting `society` to an empty string will cause the math font to reset to Computer Modern (the LaTeX default)

### Points and picas and inches, oh my!
AMS has preferred figure widths. Of course, they are in picas!

| Number of columns | Width in picas |
| ----------------- | -------------- |
| One column        | 19             |
| Two columns       | 33             |
| More than two     | 39             |

Use `pc2in` to convert from picas to inches for figsize in matplotlib.

*There are 6 picas to 1 inch.*


## Known gotchas
LaTeX text rendering comes with its share of issues. To understand those, please refer to
the following

* https://matplotlib.org/users/usetex.html#possible-hangups
* https://matplotlib.org/users/usetex.html#troubleshooting
