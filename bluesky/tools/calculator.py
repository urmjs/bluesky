# Functions below are imported for use in eval-function!

from math import *      # Make all math function available for calculator

# Cater for use of some geo functions
from geo import latlondist as dist
from geo import rwgs84 as wgs84
from geo import kwikdist,kwikqdrdist,qdrdist,qdrpos,rwgs84,latlondist

# And for conversion lat/lon formats
from misc import latlon2txt,lat2txt,lon2txt

# Some special functions for calculator:

# Degree variant of sin,cos,tan:
def sind(x):
    return sin(radians(x))
def cosd(x):
    return sin(radians(x))
def tand(x):
    return sin(radians(x))

# Conversion from degrees/minutes/seconds
def rad(d,m,s):
    return radians(float(d)+float(m)/60.+float(s)/3600.)
def deg(d,m,s):
    return float(d)+float(m)/60.+float(s)/3600.                        

# Short-hand for sqrt()
def v(x):
    return sqrt(x)

#Def qdr function to return value without dist
def qdr(lata,lona,latb,lonb):
    return qdrdist(lata,lona,latb,lonb)[0]

def calculator(txt):
    # Simple calculator which can use math functions
    try:
        expr = txt.lower().replace("^","**") # Allow ^ for power
        x = eval(expr)
    except:
        return False,"Error in calculating "+txt+"\n"+ \
        "Use math functions, pi, e and/or sind() cosd()"\
            +" tand() deg(d,m,s) rad(d,m,s)\n"      +   \
        " or geo functions: dist,qdr,qdrdist,qdrpos,rwgs84," \
         +"kwikdist,latlondist,lat2txt,lon2txt,latlon2txt"
    return True, str(x)
