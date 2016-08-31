import aplpy
from matplotlib import pylab

root = '/Users/gogrean/data/chandra/macsj0717/'

bcg_ra = 109.47302
bcg_dec = 37.70262

def group_sectors():
    f1 = pylab.figure()
    fig = aplpy.FITSFigure(root+'merged4/src_bin4_500-4000_gapsfilled_flux.img',
                           figure=f1)
    fig.show_colorscale(vmin=4e-9, vmax=3e-8, cmap='viridis',
                        smooth=3, stretch='log')
    fig.recenter(109.47114, 37.703013, width=0.1, height=0.1)

    fig.tick_labels.set_xformat('hhmmss')
    fig.tick_labels.set_yformat('ddmmss')

    fig.add_scalebar(0.02174, corner='top left')
    fig.scalebar.set_color('white')
    fig.scalebar.set_label('500 kpc')
    fig.scalebar.set_font(size='13', family='sans-serif')
    fig.scalebar.set_linewidth(2)

    fig.show_regions('group-sx-profiles.reg')

    fig.save('group-sectors.pdf', dpi=144)

def xray():
    f1 = pylab.figure()
    fig = aplpy.FITSFigure(root+'merged4/src_bin4_500-4000_gapsfilled_flux.img',
                           figure=f1)
    fig.show_colorscale(vmin=5e-9, vmax=1e-7, cmap='viridis',
                        smooth=1, stretch='log')
    fig.recenter(109.47114, 37.703013, width=0.025, height=0.025)

    fig.tick_labels.set_xformat('hhmmss')
    fig.tick_labels.set_yformat('ddmmss')

    fig.add_scalebar(0.004348, corner='top left')
    fig.scalebar.set_color('white')
    fig.scalebar.set_label('100 kpc')
    fig.scalebar.set_font(size='13', family='sans-serif')
    fig.scalebar.set_linewidth(2)

    fig.show_markers(bcg_ra, bcg_dec, s=300, marker="h", linewidth=2)

    fig.save('group-xray.pdf', dpi=144)

def optical():
    f1 = pylab.figure()
    fig = aplpy.FITSFigure(root+'hst/filament_region/hst_10084_j7_wfpc2_f606w_wf_drz.fits',
                           figure=f1)
    fig.show_colorscale(vmin=0., vmax=0.1, cmap='viridis',
                        smooth=1, stretch='sqrt')
    fig.recenter(109.47114, 37.703013, width=0.025, height=0.025)

    fig.tick_labels.set_xformat('hhmmss')
    fig.tick_labels.set_yformat('ddmmss')

    fig.add_scalebar(0.004348, corner='top left')
    fig.scalebar.set_color('white')
    fig.scalebar.set_label('100 kpc')
    fig.scalebar.set_font(size='13', family='sans-serif')
    fig.scalebar.set_linewidth(2)

    fig.show_markers(bcg_ra, bcg_dec, marker='h', s=300, linewidth=2)

    fig.save('group-optical.pdf', dpi=144)


def radio():
    f1 = pylab.figure()
    fig = aplpy.FITSFigure(root+'radio/im_all_comb_1.image.tt0.pbcor.fits',
                           figure=f1)
    fig.show_colorscale(vmin=5e-7, vmax=0.02, cmap='viridis',
                        smooth=1, stretch='log')
    fig.recenter(109.47114, 37.703013, width=0.025, height=0.025)

    fig.tick_labels.set_xformat('hhmmss')
    fig.tick_labels.set_yformat('ddmmss')

    fig.add_scalebar(0.004348, corner='top left')
    fig.scalebar.set_color('white')
    fig.scalebar.set_label('100 kpc')
    fig.scalebar.set_font(size='13', family='sans-serif')
    fig.scalebar.set_linewidth(2)
    fig.add_beam(color='white')

    fig.show_markers(bcg_ra, bcg_dec, marker='h', s=300, linewidth=2)

    fig.save('group-radio.pdf', dpi=144)
