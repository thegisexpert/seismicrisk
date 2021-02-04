import sys
sys.path.append('C:/Users/AG/.qgis2/python/plugins/PruebaAutoFields/wntr')

import wntr
from scipy.stats import lognorm
FC = wntr.scenario.FragilityCurve()
FC.add_state('Minor', 1, {'Default': lognorm(0.5,scale=0.3)})
FC.add_state('Major', 2, {'Default': lognorm(0.5,scale=0.7)})
wntr.graphics.plot_fragility_curve(FC, xlabel='Peak Ground Acceleration (g)')