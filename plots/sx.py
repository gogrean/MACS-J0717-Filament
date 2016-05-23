import aplpy
from matplotlib import pylab

root = '/Users/gogrean/data/chandra/macsj0717/merged4/'

def regions():
    f1 = pylab.figure()
    fig = aplpy.FITSFigure(root+'src_bin4_500-4000_gapsfilled_flux.img',
                           figure=f1)
    fig.show_colorscale(vmin=5e-9, vmax=4e-7, cmap='viridis',
                        smooth=1, stretch='log')
    fig.recenter(109.40485, 37.74404, width=0.165, height=0.138)

    fig.tick_labels.set_xformat('hhmmss')
    fig.tick_labels.set_yformat('ddmmss')

    fig.add_scalebar(0.04348, corner='top left')
    fig.scalebar.set_color('white')
    fig.scalebar.set_label('1 Mpc')
    fig.scalebar.set_font(size='13', family='sans-serif')
    fig.scalebar.set_linewidth(2)

    fig.add_label(109.463, 37.735, 'FILAMENT',
                  variant='small-caps', family='sans-serif', size=12,
                  color='white')
    fig.add_label(109.436, 37.6938, 'GROUP',
                  variant='small-caps', family='sans-serif', size=12,
                  color='white')
    fig.add_label(109.3408, 37.796, 'FLY-THROUGH',
                  variant='small-caps', family='sans-serif', size=12,
                  color='white')
    fig.add_label(109.3408, 37.79, 'CORE',
                  variant='small-caps', family='sans-serif', size=12,
                  color='white')

    fig.show_arrows([109.458, 109.44973, 109.34079],
                    [37.730, 37.694347, 37.7844],
                    [-0.010, 0.011, 0.00345], [-0.010, 0.003, -0.01],
                    color='white')

    fig.save('fil-labels.pdf', dpi=144)

    f2 = pylab.figure()
    fig = aplpy.FITSFigure(root+'src_bin4_500-4000_gapsfilled_flux.img',
                           figure=f2)
    fig.show_colorscale(vmin=5e-9, vmax=4e-7, cmap='viridis',
                        smooth=1, stretch='log')
    fig.recenter(109.40485, 37.74404, width=0.165, height=0.138)

    fig.tick_labels.set_xformat('hhmmss')
    fig.tick_labels.set_yformat('ddmmss')

    fig.add_scalebar(0.04348, corner='top left')
    fig.scalebar.set_color('white')
    fig.scalebar.set_label('1 Mpc')
    fig.scalebar.set_font(size='13', family='sans-serif')
    fig.scalebar.set_linewidth(2)

    fig.show_regions('filament_composite.reg')

    fig.save('fil-regions.pdf', dpi=144)

    f2 = pylab.figure()
    fig = aplpy.FITSFigure(root+'src_bin4_500-4000_gapsfilled_flux.img',
                           figure=f2)
    fig.show_colorscale(vmin=5e-9, vmax=4e-7, cmap='viridis',
                        smooth=1, stretch='log')
    fig.recenter(109.37833, 37.755275, width=0.1, height=0.1)

    fig.tick_labels.set_xformat('hhmmss')
    fig.tick_labels.set_yformat('ddmmss')

    fig.add_scalebar(0.04348, corner='top left')
    fig.scalebar.set_color('white')
    fig.scalebar.set_label('1 Mpc')
    fig.scalebar.set_font(size='13', family='sans-serif')
    fig.scalebar.set_linewidth(2)

    fig.show_regions('flythrough.reg')

    fig.save('flythrough-regions.pdf', dpi=144) 


def sectors():
    f1 = pylab.figure()
    fig = aplpy.FITSFigure(root+'src_bin4_500-4000_gapsfilled_flux.img',
                           figure=f1)
    fig.show_colorscale(vmin=5e-9, vmax=2e-7, cmap='viridis',
                        smooth=1, stretch='log')
    fig.recenter(109.31321, 37.79979, width=0.1219, height=0.1066)

    fig.tick_labels.set_xformat('hhmmss')
    fig.tick_labels.set_yformat('ddmmss')

    fig.add_scalebar(0.04348, corner='top left')
    fig.scalebar.set_color('white')
    fig.scalebar.set_label('1 Mpc')
    fig.scalebar.set_font(size='13', family='sans-serif')
    fig.scalebar.set_linewidth(2)

    fig.show_regions('core_sx_circ.reg')
    fig.save('circ-panda.pdf', dpi=144)

    f2 = pylab.figure()
    fig = aplpy.FITSFigure(root+'src_bin4_500-4000_gapsfilled_flux.img',
                           figure=f2)
    fig.show_colorscale(vmin=5e-9, vmax=2e-7, cmap='viridis',
                        smooth=1, stretch='log')
    fig.recenter(109.31321, 37.79979, width=0.1219, height=0.1066)

    fig.tick_labels.set_xformat('hhmmss')
    fig.tick_labels.set_yformat('ddmmss')

    fig.add_scalebar(0.04348, corner='top left')
    fig.scalebar.set_color('white')
    fig.scalebar.set_label('1 Mpc')
    fig.scalebar.set_font(size='13', family='sans-serif')
    fig.scalebar.set_linewidth(2)

    fig.show_regions('core_sx_ell.reg')
    fig.save('ell-panda.pdf', dpi=144)
