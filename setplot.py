
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 

#import os
#thisdir = os.getcwd()   # this directory, where setgauges.data is found

from pyclaw.geotools import topotools
from pyclaw.data import Data
import pylab
import glob

try:
    from setplotfg import setplotfg
except:
    print "Did not find setplotfg.py"
    setplotfg = None



#--------------------------
def setplot(plotdata):
#--------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of pyclaw.plotters.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 


    from pyclaw.plotters import colormaps, geoplot

    plotdata.clearfigures()  # clear any old figures,axes,items data


    # To plot gauge locations on pcolor or contour plot, use this as
    # an afteraxis function:

    def addgauges(current_data):
        from pyclaw.plotters import gaugetools
        gaugetools.plot_gauge_locations(current_data.plotdata, \
             gaugenos='all', format_string='ko', add_labels=True)


    
    #-----------------------------------------
    # Figure for pcolor plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Coarse', figno=0)
    plotfigure.show = True
    
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'Coarse'
    plotaxes.scaled = True

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.surface_or_depth
    my_cmap = colormaps.make_colormap({-1.0: [0.0,0.0,1.0], \
                                      -0.1: [0.5,0.5,1.0], \
                                       0.0: [1.0,1.0,1.0], \
                                       0.1: [1.0,0.5,0.5], \
                                       1.0: [1.0,0.0,0.0]})
    plotitem.imshow_cmap = my_cmap
    plotitem.imshow_cmin = -1.0
    plotitem.imshow_cmax = 1.0
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]
    plotaxes.xlimits = [106,122]
    plotaxes.ylimits = [-10,-6]
 

    #-----------------------------------------
    # Figure for pcolor plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Java', figno=15)
    plotfigure.show = True
    
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'Java'
    plotaxes.scaled = True

    def fixup(current_data):
        import pylab
        addgauges(current_data)
        t = current_data.t
        t = t / 3600.  # hours
        pylab.title('Surface at %4.2f hours' % t, fontsize=20)
        pylab.xticks(fontsize=15)
        pylab.yticks(fontsize=15)
    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.surface_or_depth
    my_cmap = colormaps.make_colormap({-1.0: [0.0,0.0,1.0], \
                                      -0.1: [0.5,0.5,1.0], \
                                       0.0: [1.0,1.0,1.0], \
                                       0.1: [1.0,0.5,0.5], \
                                       1.0: [1.0,0.0,0.0]})
    plotitem.imshow_cmap = my_cmap
    plotitem.imshow_cmin = -1.0
    plotitem.imshow_cmax = 1.0
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]
    plotaxes.xlimits = [109,110]
    plotaxes.ylimits = [-10,-6]

    #-----------------------------------------
    # Figure for pcolor plot zoom
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Java2', figno=25)
    plotfigure.show = True
    
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'Java2'
    plotaxes.scaled = True

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.surface_or_depth
    my_cmap = colormaps.make_colormap({-1.0: [0.0,0.0,1.0], \
                                      -0.1: [0.5,0.5,1.0], \
                                       0.0: [1.0,1.0,1.0], \
                                       0.1: [1.0,0.5,0.5], \
                                       1.0: [1.0,0.0,0.0]})
    plotitem.imshow_cmap = my_cmap
    plotitem.imshow_cmin = -1.0
    plotitem.imshow_cmax = 1.0
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]
    plotaxes.xlimits = [110,111]
    plotaxes.ylimits = [-10,-6]
    plotaxes.afteraxes = addgauges
 
   # Add contour lines of bathymetry:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    from numpy import arange, linspace
    plotitem.contour_levels = arange(-10., 0., 1.)
    plotitem.amr_contour_colors = ['k']  # color on each level
    plotitem.kwargs = {'linestyles':'solid'}
    plotitem.amr_contour_show = [0,0,0,0,1]  # show contours only on finest level
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True
    plotitem.kwargs = {'linewidths':2}
 
    # Add contour lines of topography:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    from numpy import arange, linspace
    plotitem.contour_levels = arange(0., 11., 1.)
    plotitem.amr_contour_colors = ['g']  # color on each level
    plotitem.kwargs = {'linestyles':'solid'}
    plotitem.amr_contour_show = [0,0,0,0,1]  # show contours only on finest level
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True
    
    #-----------------------------------------
    # Figure for pcolor plot zoom
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Java3', figno=20)
    plotfigure.show = True
    
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'Java3'
    plotaxes.scaled = True

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.surface_or_depth
    my_cmap = colormaps.make_colormap({-1.0: [0.0,0.0,1.0], \
                                      -0.1: [0.5,0.5,1.0], \
                                       0.0: [1.0,1.0,1.0], \
                                       0.1: [1.0,0.5,0.5], \
                                       1.0: [1.0,0.0,0.0]})
    plotitem.imshow_cmap = my_cmap
    plotitem.imshow_cmin = -1.0
    plotitem.imshow_cmax = 1.0
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]
    plotaxes.xlimits = [111,112]
    plotaxes.ylimits = [-10,-6]
    plotaxes.afteraxes = addgauges
 
   # Add contour lines of bathymetry:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    from numpy import arange, linspace
    plotitem.contour_levels = arange(-10., 0., 1.)
    plotitem.amr_contour_colors = ['k']  # color on each level
    plotitem.kwargs = {'linestyles':'solid'}
    plotitem.amr_contour_show = [0,0,0,0,1]  # show contours only on finest level
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True

    # Add contour lines of topography:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    from numpy import arange, linspace
    plotitem.contour_levels = arange(0., 11., 1.)
    plotitem.amr_contour_colors = ['g']  # color on each level
    plotitem.kwargs = {'linestyles':'solid'}
    plotitem.amr_contour_show = [0,0,0,0,1]  # show contours only on finest level
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True
 
    #-----------------------------------------
    # Figure for pcolor plot zoom
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Java4', figno=30)
    plotfigure.show = True
    
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'Java4'
    plotaxes.scaled = True

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.surface_or_depth
    my_cmap = colormaps.make_colormap({-1.0: [0.0,0.0,1.0], \
                                      -0.1: [0.5,0.5,1.0], \
                                       0.0: [1.0,1.0,1.0], \
                                       0.1: [1.0,0.5,0.5], \
                                       1.0: [1.0,0.0,0.0]})
    plotitem.imshow_cmap = my_cmap
    plotitem.imshow_cmin = -1.0
    plotitem.imshow_cmax = 1.0
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]
    plotaxes.xlimits = [112,113]
    plotaxes.ylimits = [-10,-6]
    plotaxes.afteraxes = addgauges
 
   # Add contour lines of bathymetry:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    from numpy import arange, linspace
    plotitem.contour_levels = arange(-10., 0., 1.)
    plotitem.amr_contour_colors = ['k']  # color on each level
    plotitem.kwargs = {'linestyles':'solid'}
    plotitem.amr_contour_show = [0,0,0,0,1]  # show contours only on finest level
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True

    # Add contour lines of topography:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    from numpy import arange, linspace
    plotitem.contour_levels = arange(0., 11., 1.)
    plotitem.amr_contour_colors = ['g']  # color on each level
    plotitem.kwargs = {'linestyles':'solid'}
    plotitem.amr_contour_show = [0,0,0,0,1]  # show contours only on finest level
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True


    #-----------------------------------------
    # Figure for topography & bathymetry
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Topography', figno=5)
    plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'Topography'
    plotaxes.scaled = True

    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.topo
    plotitem.pcolor_cmap = geoplot.bathy1_colormap
    plotitem.pcolor_cmap = colormaps.make_colormap({-1:[0.3,0.2,0.1],
                                           -0.01:[0.95,0.9,0.7],
                                           .01:[.5,.7,0], 
                                           1:[.2,.5,.2]})
                                           
    plotitem.pcolor_cmin = -60.0
    plotitem.pcolor_cmax = 60.0
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [1,0,0]
    plotitem.amr_gridedges_show = [1]

    #plotaxes.xlimits = [-127.4,-123.5]
    #plotaxes.ylimits = [45.5,49.5]
   # plotaxes.ylimits = [45.5,48.5]
    plotaxes.xlimits = [160,170]
    plotaxes.ylimits = [55,62.5]


    #-----------------------------------------
    # Figures for gauges
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='gauge plot', figno=300, \
                    type='each_gauge')

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = 'auto'
    plotaxes.title = 'Surface'

    # Plot surface as blue curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 3
    plotitem.plotstyle = 'b-'

    # Plot topo as green curve:
#    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')

#    def gaugetopo(current_data):
#        q = current_data.q
#        h = q[:,0]
#        eta = q[:,3]
#        topo = eta - h
#        return topo
        
#    plotitem.plot_var = gaugetopo
#    plotitem.plotstyle = 'g-'

    def add_zeroline(current_data):
        from pylab import plot, legend, xticks, floor, axis, xlabel
        t = current_data.t
        gaugeno = current_data.gaugeno
    
        if gaugeno == 32412:
            plot(TG32412[:,0], TG32412[:,1], 'r')
            legend(['GeoClaw','Obs'],'lower right')
            axis((0,t.max(),-0.3,0.3))
        if gaugeno == 51406:
            plot(TG51406[:,0], TG51406[:,1], 'r')
            legend(['GeoClaw','Obs'],'lower left')
            axis((0,t.max(),-0.3,0.3))

        #legend(('surface','topography'),loc='lower left')
        plot(t, 0*t, 'k')
        #n = int(floor(t.max()/3600.) + 2)
        #xticks([3600*i for i in range(n)],rotation=20)
        xticks(rotation=20)
        xlabel('Time (seconds since earthquake)')

    plotaxes.afteraxes = add_zeroline

    # Plot surface from a different run:
    if 0:
        plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
        plotitem.plot_var = 3
        plotitem.plotstyle = 'r-'
        plotitem.outdir = thisdir + '/_output_run3'




    #-----------------------------------------
    # Figure for contour plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='contour', figno=1)
    plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = [0,1]
    plotaxes.ylimits = [0,1]
    plotaxes.title = 'Solution'
    plotaxes.scaled = True

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.surface
    plotitem.contour_nlevels = 40
    plotitem.contour_min = -0.1
    plotitem.contour_max = 0.1
    plotitem.amr_contour_colors = ['r','k','b']  # color on each level
    plotitem.amr_contour_show = [0,1]            # show lines on each level?
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.amr_grid_bgcolor = ['#ffeeee', '#eeeeff', '#eeffee']
    plotitem.show = True 

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.land
    plotitem.contour_nlevels = 40
    plotitem.contour_min = 0.0
    plotitem.contour_max = 100.0
    plotitem.amr_contour_colors = ['g']  # color on each level
    plotitem.amr_grid_bgcolor = ['#ffeeee', '#eeeeff', '#eeffee']
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = False 


    #-----------------------------------------
    # Figure for grids alone
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='grids', figno=2)
    plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = [0,1]
    plotaxes.ylimits = [0,1]
    plotaxes.title = 'grids'
    plotaxes.scaled = True

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type='2d_grid')
    plotitem.amr_grid_bgcolor = ['#ffeeee', '#eeeeff', '#eeffee']
    plotitem.amr_gridlines_show = [1,1,0]   
    plotitem.amr_gridedges_show = [1]     

   # -----------------  
   # Fixed grid plots
   # -----------------

    if setplotfg is not None:

       # Repeat as desired for other fixed grids...
       # These show up when using 'make .plots'
       #----------       
       
       fgno = 1
       otherfig = plotdata.new_otherfigure('Fixed Grid %s' % fgno)
       sfgno = str(fgno).zfill(2)  # e.g. '01'
       otherfig.fname = '_PlotIndex_FixedGrid%s.html' % sfgno
       def make_fgplots(plotdata):
           fgdata = setplotfg(fgno, outdir=plotdata.outdir)
           # See the setplotfg function for setting up fixed grid plots
           fgdata.fg2html(framenos='all')
       otherfig.makefig = make_fgplots
       #------------------------
       
     
    #-----------------------------------------
    
    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.print_gaugenos = 'all'          # list of gauges to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

    