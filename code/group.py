from chandra_sx_maps import chandra_image

DATADIR = '../data/'
PLOTSDIR = '../plots/'
CHANDRA_IMG = DATADIR + 'src_bin4_500-4000_gapsfilled_flux.img'
FOV = [109.47114, 37.703013, 0.1, 0.1]
SCALE = [4E-9, 3E-8]
SCALEBAR = 0.02174
SMOOTH = 3

fig = chandra_image(CHANDRA_IMG, scale=SCALE, fov=FOV,
                    scalebar_length=SCALEBAR, smooth=SMOOTH)
fig.show_regions(DATADIR + 'group-sx-profiles.reg')
fig.save(PLOTSDIR + 'group-sectors.pdf', dpi=400)
