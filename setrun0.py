"""
Module to set up run time parameters for Clawpack.

The values set in the function setrun are then written out to data files
that will be read in by the Fortran code.

"""

import os
from pyclaw import data
import numpy as np


#------------------------------
def setrun(claw_pkg='geoclaw'):
#------------------------------

    """
    Define the parameters used for running Clawpack.

    INPUT:
        claw_pkg expected to be "geoclaw" for this setrun.

    OUTPUT:
        rundata - object of class ClawRunData

    """

    assert claw_pkg.lower() == 'geoclaw',  "Expected claw_pkg = 'geoclaw'"

    ndim = 2
    rundata = data.ClawRunData(claw_pkg, ndim)

    #------------------------------------------------------------------
    # Problem-specific parameters to be written to setprob.data:
    #------------------------------------------------------------------

    #probdata = rundata.new_UserData(name='probdata',fname='setprob.data')

    #------------------------------------------------------------------
    # GeoClaw specific parameters:
    #------------------------------------------------------------------

    rundata = setgeo(rundata)   # Defined below

    #------------------------------------------------------------------
    # Standard Clawpack parameters to be written to claw.data:
    #   (or to amr2ez.data for AMR)
    #------------------------------------------------------------------

    clawdata = rundata.clawdata  # initialized when rundata instantiated


    # Set single grid parameters first.
    # See below for AMR parameters.


    # ---------------
    # Spatial domain:
    # ---------------

    # Number of space dimensions:
    clawdata.ndim = ndim

    # Lower and upper edge of computational domain:
    clawdata.xlower = 106
    clawdata.xupper = 130

    clawdata.ylower = -32
    clawdata.yupper = 0


    # Number of grid cells:
    clawdata.mx = 24
    clawdata.my = 32


    # ---------------
    # Size of system:
    # ---------------

    # Number of equations in the system:
    clawdata.meqn = 3

    # Number of auxiliary variables in the aux array (initialized in setaux)
    clawdata.maux = 3

    # Index of aux array corresponding to capacity function, if there is one:
    clawdata.mcapa = 2


    # -------------
    # Initial time:
    # -------------

    clawdata.t0 = 0.0


    # -------------
    # Output times:
    #--------------

    # Specify at what times the results should be written to fort.q files.
    # Note that the time integration stops after the final output time.
    # The solution at initial time t0 is always written in addition.

    clawdata.outstyle = 1

    if clawdata.outstyle==1:
        # Output nout frames at equally spaced times up to tfinal:
        clawdata.nout = 16
        clawdata.tfinal = 3600*4

    elif clawdata.outstyle == 2:
        # Specify a list of output times.
        clawdata.tout =  [0.5, 1.0]   # used if outstyle == 2
        clawdata.nout = len(clawdata.tout)

    elif clawdata.outstyle == 3:
        # Output every iout timesteps with a total of ntot time steps:
        iout = 2
        ntot = 6
        clawdata.iout = [iout, ntot]



    # ---------------------------------------------------
    # Verbosity of messages to screen during integration:
    # ---------------------------------------------------

    # The current t, dt, and cfl will be printed every time step
    # at AMR levels <= verbosity.  Set verbosity = 0 for no printing.
    #   (E.g. verbosity == 2 means print only on levels 1 and 2.)
    clawdata.verbosity = 1



    # --------------
    # Time stepping:
    # --------------

    # if dt_variable==1: variable time steps used based on cfl_desired,
    # if dt_variable==0: fixed time steps dt = dt_initial will always be used.
    clawdata.dt_variable = 1

    # Initial time step for variable dt.
    # If dt_variable==0 then dt=dt_initial for all steps:
    clawdata.dt_initial = 0.016

    # Max time step to be allowed if variable dt used:
    clawdata.dt_max = 1e+99

    # Desired Courant number if variable dt used, and max to allow without
    # retaking step with a smaller dt:
    clawdata.cfl_desired = 0.75
    clawdata.cfl_max = 1.0

    # Maximum number of time steps to allow between output times:
    clawdata.max_steps = 5000




    # ------------------
    # Method to be used:
    # ------------------

    # Order of accuracy:  1 => Godunov,  2 => Lax-Wendroff plus limiters
    clawdata.order = 2

    # Transverse order for 2d or 3d (not used in 1d):
    clawdata.order_trans = 2

    # Number of waves in the Riemann solution:
    clawdata.mwaves = 3

    # List of limiters to use for each wave family:
    # Required:  len(mthlim) == mwaves
    clawdata.mthlim = [3,3,3]

    # Source terms splitting:
    #   src_split == 0  => no source term (src routine never called)
    #   src_split == 1  => Godunov (1st order) splitting used,
    #   src_split == 2  => Strang (2nd order) splitting used,  not recommended.
    clawdata.src_split = 1


    # --------------------
    # Boundary conditions:
    # --------------------

    # Number of ghost cells (usually 2)
    clawdata.mbc = 2

    # Choice of BCs at xlower and xupper:
    #   0 => user specified (must modify bcN.f to use this option)
    #   1 => extrapolation (non-reflecting outflow)
    #   2 => periodic (must specify this at both boundaries)
    #   3 => solid wall for systems where q(2) is normal velocity

    clawdata.mthbc_xlower = 1
    clawdata.mthbc_xupper = 1

    clawdata.mthbc_ylower = 1
    clawdata.mthbc_yupper = 1


    # ---------------
    # AMR parameters:
    # ---------------


    # max number of refinement levels:
    mxnest = 5

    clawdata.mxnest = -mxnest   # negative ==> anisotropic refinement in x,y,t

    # List of refinement ratios at each level (length at least mxnest-1)
    clawdata.inratx = [4,5,6,10]
    clawdata.inraty = [4,5,6,10]
    clawdata.inratt = [1,1,1,1]

    # Instead of setting these ratios, set:
    # geodata.variable_dt_refinement_ratios = True
    # in setgeo.
    # to automatically choose refinement ratios in time based on estimate
    # of maximum wave speed on all grids at each level.


    # Specify type of each aux variable in clawdata.auxtype.
    # This must be a list of length maux, each element of which is one of:
    #   'center',  'capacity', 'xleft', or 'yleft'  (see documentation).

    clawdata.auxtype = ['center','capacity','yleft']


    clawdata.tol = -1.0     # negative ==> don't use Richardson estimator
    clawdata.tolsp = 0.5    # used in default flag2refine subroutine
                            # (Not used in geoclaw!)

    clawdata.kcheck = 3     # how often to regrid (every kcheck steps)
    clawdata.ibuff  = 2     # width of buffer zone around flagged points

    # More AMR parameters can be set -- see the defaults in pyclaw/data.py

    return rundata
    # end of function setrun
    # ----------------------


#-------------------
def setgeo(rundata):
#-------------------
    """
    Set GeoClaw specific runtime parameters.
    For documentation see ....
    """

    try:
        geodata = rundata.geodata
    except:
        print "*** Error, this rundata has no geodata attribute"
        raise AttributeError("Missing geodata attribute")

    # == setgeo.data values ==

    geodata.variable_dt_refinement_ratios = True

    geodata.igravity = 1
    geodata.gravity = 9.81
    geodata.icoordsys = 2
    geodata.Rearth = 6367.5e3
    geodata.icoriolis = 0

    # == settsunami.data values ==
    geodata.sealevel = 0.
    geodata.drytolerance = 1.e-3
    geodata.wavetolerance = 1.e-1
    geodata.depthdeep = 1.e2
    geodata.maxleveldeep = 4
    geodata.ifriction = 1
    geodata.coeffmanning =.025
    geodata.frictiondepth = 200.


    # == settopo.data values ==
    geodata.topofiles = []
    # for topography, append lines of the form
    #   [topotype, minlevel, maxlevel, t1, t2, fname]
    geodata.topofiles.append([3, 1, 1, 0., 1e10, 'ebanda.asc'])
   

    # == setdtopo.data values ==
    geodata.dtopofiles = []
    # for moving topography, append lines of the form:  (<= 1 allowed for now!)
    #   [topotype, minlevel, maxlevel, fname]
    geodata.dtopofiles.append([3,1,3,'BandaArc1852.tt3'])

    geodata.iqinit = 0
    geodata.qinitfiles = []

    # == setgauges.data values ==
    geodata.gauges = []
    # for gauges append lines of the form [gaugeno,x,y,t1,t2]
    geodata.gauges.append([1, 109.000, -7.789, 0., 1e10]) #Cialciap
    geodata.gauges.append([2, 109.040, -7.722, 0., 1e10]) #Cialciap Bay
    geodata.gauges.append([3, 110.292, -8.027, 0., 1e10]) #Bantul
    geodata.gauges.append([4, 111.086, -8.233, 0., 1e10]) #Pacitan
    geodata.gauges.append([5, 111.558, -8.319, 0., 1e10]) #Pelang Beach
    geodata.gauges.append([6, 111.968, -8.286, 0., 1e10]) #Sine Beach
    geodata.gauges.append([7, 112.982, -8.326, 0., 1e10]) #Guying
    geodata.gauges.append([8, 113.176, -8.286, 0., 1e10]) #Muara
    geodata.gauges.append([9, 113.461, -8.383, 0., 1e10]) #Puger
    geodata.gauges.append([10, 113.336, -8.506, 0., 1e10]) #Barung Island
    geodata.gauges.append([11, 114.110, -8.621, 0., 1e10]) #Lampon
    geodata.gauges.append([12, 114.396, -8.231, 0., 1e10]) #Banyuwani
    geodata.gauges.append([13, 112.880, -7.278, 0., 1e10]) #Surabiya
    geodata.gauges.append([14, 114.965, -8.533, 0., 1e10]) #Tabanan
    geodata.gauges.append([15, 115.144, -8.697, 0., 1e10]) #Kuta
    geodata.gauges.append([16, 115.193, -8.848, 0., 1e10]) #Nusa Dua
    geodata.gauges.append([17, 116.064, -8.586, 0., 1e10]) #Mataram
    geodata.gauges.append([18, 115.260, -8.727, 0., 1e10]) #Sanur
    geodata.gauges.append([19, 116.031, -8.873, 0., 1e10]) #Sepi Bay
    geodata.gauges.append([20, 116.135, -8.872, 0., 1e10]) #Serangan Beach
    geodata.gauges.append([21, 116.283, -8.902, 0., 1e10]) #Kuta Lombok
    geodata.gauges.append([22, 116.400, -8.868, 0., 1e10]) #Awang Bay
    geodata.gauges.append([23, 116.466, -8.924, 0., 1e10]) #Surga Beach
    geodata.gauges.append([24, 116.744, -8.918, 0., 1e10]) #Maluk
    geodata.gauges.append([25, 116.833, -9.047, 0., 1e10]) #Tongo
    geodata.gauges.append([26, 117.199, -9.023, 0., 1e10]) #Linyuk
    geodata.gauges.append([27, 117.762, -8.939, 0., 1e10]) #Leppu
    geodata.gauges.append([28, 118.377, -8.785, 0., 1e10]) #Huu
    geodata.gauges.append([29, 118.172, -8.780, 0., 1e10]) #Rontu Beach
    geodata.gauges.append([30, 119.403, -8.729, 0., 1e10]) #Mantea Alley
    geodata.gauges.append([31, 119.374, -9.788, 0., 1e10]) #Nihiwatu
    geodata.gauges.append([32, 119.466, -9.742, 0., 1e10]) #Waigalli
    geodata.gauges.append([33, 119.945, -9.975, 0., 1e10]) #Tarimbang Beach
    geodata.gauges.append([34, 120.183, -10.233, 0., 1e10]) #Lalindi
    geodata.gauges.append([35, 120.264, -10.257, 0., 1e10]) #Manoekangga
    geodata.gauges.append([36, 120.546, -10.241, 0., 1e10]) #Baing
    geodata.gauges.append([37, 120.312, -9.661, 0., 1e10]) #Waingapu
    geodata.gauges.append([38, 119.871, -8.501, 0., 1e10]) #Labun Badjo
    geodata.gauges.append([39, 120.604, -8.822, 0., 1e10]) #Mborong
    geodata.gauges.append([40, 123.560, -10.166, 0., 1e10]) #Kupang
    geodata.gauges.append([41, 121.824, -10.491, 0., 1e10]) #Baa



