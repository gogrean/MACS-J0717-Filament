import aplpy

def chandra_image(img_fname, scale=[None, None], fov=[0, 0, 0.1, 0.1],
                  scalebar_length=0.05, smooth=None):
    '''
    Take the Chandra surface brightness map, recenter it, smooth it
    with a Gaussian of width 1 pixel, and plot it log-scaled between the
    limits set by `scale` to increase the image contrast. Return a FITSFigure
    object that includes a scalebar with length defined by `scalebar_length`.

    Parameters
    ----------

        img_fname : string
            Filename of the Chandra image.

        scale : sequence, optional
            Boundary pixel values to use for the colorscale. Defaults to the
            minimum and maximum values of the image array.

        fov : sequence, optional
            Field of view. Of form [x0, y0, width, height], where x0 and y0 are
            the coordinates that the image is centered on, and width and height
            define the size of the FOV in degrees. Defaults to [0, 0, 0.1, 0.1].

        scalebar_length : float, optional
            Length of the scalebar, in degrees. Defaults to 0.05 degrees.

        smooth : None or odd int, optional
            Width of the Gaussian used to smooth the image.
    '''
    fig = aplpy.FITSFigure(img_fname)
    fig.recenter(fov[0], fov[1], width=fov[2], height=fov[3])
    fig.show_colorscale(vmin=scale[0], vmax=scale[1], cmap='viridis',
                        smooth=smooth, stretch='log')

    fig.tick_labels.set_xformat('hhmmss')
    fig.tick_labels.set_yformat('ddmmss')

    fig.add_scalebar(scalebar_length, corner='top left')
    fig.scalebar.set_color('white')
    fig.scalebar.set_label('1 Mpc')
    fig.scalebar.set_font(size='13', family='sans-serif')
    fig.scalebar.set_linewidth(2)

    return fig


DATADIR = "../data/"
PLOTSDIR = "../plots/"
CHANDRA_IMG = DATADIR + "src_bin4_500-4000_gapsfilled_flux.img"
FOV = [109.40485,37.74404,0.165,0.158]
SCALE = [5E-9, 4E-7]
SCALEBAR = 0.04348
SMOOTH = 1

# Fig 2a: Chandra surface brightness map, with the features discussed in
# the paper labeled.
fig = chandra_image(CHANDRA_IMG, scale=SCALE, fov=FOV,
                    scalebar_length=SCALEBAR, smooth=SMOOTH)
fig.add_label(109.463, 37.735, 'FILAMENT', variant='small-caps',
              family='sans-serif', size=12, color='white')
fig.add_label(109.436, 37.6938, 'GROUP', variant='small-caps',
              family='sans-serif', size=12, color='white')
fig.show_arrows([109.458, 109.44973, 109.36008, 109.36008], [37.730, 37.694347, 37.704172, 37.704172],
                [-0.010, 0.011, -0.012, -0.010], [-0.010, 0.003, 0.004, 0.010], color='white')
fig.add_label(109.3738, 37.703072, "'FINGER'", variant='small-caps', 
              family='sans-serif', size=12, color='white')
fig.save(PLOTSDIR + 'fil-labels.pdf', dpi=400)

# Fig 2b: Chandra surface brightness map showing the regions used for
# modeling the spectra of the emission coming from the infalling group, 
# from the filament, and from the cold SW region.
fig = chandra_image(CHANDRA_IMG, scale=SCALE, fov=FOV,
                    scalebar_length=SCALEBAR, smooth=SMOOTH)
fig.show_regions(DATADIR + 'filament_composite.reg')
fig.add_label(0.283, 0.33, 'A',
              relative=True, variant='small-caps',
              family='sans-serif', size=12, color='white')
fig.add_label(0.485, 0.155, 'B', 
              relative=True, variant='small-caps', 
              family='sans-serif', size=12, color='white')
fig.add_label(0.835, 0.82, 'C',
              relative=True, variant='small-caps',
              family='sans-serif', size=12, color='white')
fig.add_label(0.84, 0.27, 'D',
              relative=True, variant='small-caps',
              family='sans-serif', size=12, color='orange')
fig.save(PLOTSDIR + 'fil-regions.pdf', dpi=400)
