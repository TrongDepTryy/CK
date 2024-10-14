#-----------------------------------------------------------------------
# windchill.py

# Wind chill. Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the National Weather Service defines the effective temperature (the wind chill) to be:

# w = 35.74 + 0.6215 t + (0.4275 t - 35.75) v0.16
# Compose a program that takes two floats t and v from the command-line and writes the wind chill. Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger than 120 or less than 3 (you may assume that the values you get are in that range).
#-----------------------------------------------------------------------


import sys

 # Accept as command-line arguments a temperature t (in Fahrenheit)
 # and a wind speed v (in miles per hour). Compute the wind chill
 # w using the formula from the National Weather Service.
 # Write w to standard output.
 #
 #  Reference:  http://www.nws.noaa.gov/om/windchill/index.shtml

t = float(sys.argv[1])
v = float(sys.argv[2])

w = 35.74 + 0.6215*t + (0.4275*t - 35.75) * (v ** 0.16)

print('Temperature = ' + str(t))
print('Wind speed  = ' + str(v))
print('Wind chill  = ' + str(w))

#-----------------------------------------------------------------------

# python windchill.py 32 10
# Temperature = 32.0
# Wind speed  = 10.0
# Wind chill  = 23.72714425963738



# Copyright © 2000–2015, Robert Sedgewick, Kevin Wayne, and Robert Dondero.
# Last updated: Fri Oct 20 20:45:16 EDT 2017.