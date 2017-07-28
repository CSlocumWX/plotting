"""
An example that changes the font to Helvetica, a
san-serif font the gets close to AGU's current choice
"""

from plotting import *
import numpy as np

change_style(society="agu")

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
fix_ticklabels()
plt.savefig("test_usetex.pdf")
plt.savefig("test_usetex.png")
plt.show()
