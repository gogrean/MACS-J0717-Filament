import aplpy
import matplotlib.pylab as plt

DATADIR = "../data/"
PLOTSDIR = "../plots/"
CHANDRA_IMG = DATADIR + "src_bin4_500-4000_gapsfilled_flux.img"
HST_IMG = DATADIR + "hst_10084_j7_wfpc2_f606w_wf_drz.fits"
VLA_IMG = DATADIR + "im_all_comb_1.image.tt0.pbcor.fits"
IMG_FNAME = [CHANDRA_IMG, HST_IMG, VLA_IMG]
STRETCH = ['log', 'sqrt', 'log']
SCALE = [(5E-9, 1E-7), (0, 0.1), (5E-7, 2E-2)]
FOV = [109.47114, 37.703013, 0.025, 0.025]
SCALEBAR = 0.004348
SCALEBAR_PHYS = '100 kpc'
BCG_RA = 109.47302
BCG_DEC = 37.70262

f = plt.figure(figsize=(12, 5))
for (i, fname), sc, st in zip(enumerate(IMG_FNAME), SCALE, STRETCH):
    fig = aplpy.FITSFigure(fname, figure=f, subplot=(1, 3, i+1))
    fig.show_colorscale(vmin=sc[0], vmax=sc[1], cmap='viridis',
                        smooth=1, stretch=st)
    fig.recenter(FOV[0], FOV[1], width=FOV[2], height=FOV[3])
    fig.tick_labels.set_xformat('hhmmss')
    fig.tick_labels.set_yformat('ddmmss')
    fig.add_scalebar(SCALEBAR, corner='top right')
    fig.scalebar.set_color('white')
    fig.scalebar.set_label(SCALEBAR_PHYS)
    fig.scalebar.set_font(size='13', family='sans-serif')
    fig.scalebar.set_linewidth(2)
    fig.show_markers(BCG_RA, BCG_DEC, s=300, marker="h", linewidth=2)
    if i != 0:
        fig.hide_yaxis_label()
        fig.hide_ytick_labels()
    if i == 1:
        fig.ticks.hide_y()
f.subplots_adjust(wspace=0)
f.savefig(PLOTSDIR + 'group_bcg.pdf')
