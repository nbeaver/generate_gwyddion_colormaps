#!/usr/bin/env python3
import os.path
import matplotlib
import numpy

def get_gwyddion_gradient(colormap, n=256):
    gwy_gradient = ["Gwyddion resource GwyGradient"]
    for x in numpy.linspace(0, 1, n):
        red, green, blue, alpha = colormap(x)
        # position red green blue alpha
        row = "{} {} {} {} 1".format(x, red, green, blue)
        gwy_gradient.append(row)
    return gwy_gradient

cmap_list = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
out_dir = "gradients"
os.mkdir(out_dir)
for cmap_name in cmap_list:
    cmap = matplotlib.cm.get_cmap(cmap_name)
    gradient = get_gwyddion_gradient(cmap)
    outpath = os.path.join(out_dir, cmap_name)
    with open(outpath, 'w', newline='\n') as fp:
        for row in gradient:
            fp.write(row + '\n')
