 #!/usr/bin/python

try:
    from pdf import * ##This file can be found here https://github.com/cmontalvo251/Python/blob/master/pdf/pdf.py
except:
    import sys
    sys.path.append('../../Python/pdf/')
    from pdf import *
from Universe import *
import matplotlib.pyplot as plt
from datetime import datetime

def date_to_julian(date_string):
    date = datetime.strptime(date_string, '%Y-%m-%d')
    return date.toordinal() + 1721424.5

# Get date input from user
date_input = input("Enter a date in YYYY-MM-DD format: ")

# Convert to Julian date
julian_day = date_to_julian(date_input)

print(f"Julian day: {julian_day}")

# Create JPL object
planets = JPL(julian_day)

# Compute orbits
planets.MilkyWay.Orbit()

# Create plots
print('Creating Plots')
pp = PDF(0,plt)

# Plot all planets
planets.MilkyWay.PlotOrbit(pp,-1)

# Plot inner planets
planets.MilkyWay.numsatellites = 5
planets.MilkyWay.PlotOrbit(pp,-1)

pp.close()
sys.exit()

# Animation code (commented out)
'''
planets.MilkyWay.numsatellites = 4 + 1
pa = PDF(1,plt)
day_skip = 1.0
num_skips = 100000
pause_time = 0.00001
os.system('rm Frames/*.png')
planets.AnimateOrbits(pa,julian_day,day_skip,num_skips,pause_time)
'''

# Mayavi plotting (commented out)
'''
planets.MilkyWay.numsatellites = 10
planets.MilkyWay.PlotMayavi()
'''