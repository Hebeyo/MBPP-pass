'''Write a function to calculate wind chill index.
'''
def wind_chill(v,t):
 windchill = 13.12 + 0.6215*t -  11.37*pow(v, 0.16) + 0.3965*t*pow(v, 0.16)
 return int(round(windchill, 0))
'''
Standard answer: 
import math
def wind_chill(v,t):
 windchill = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
 return int(round(windchill, 0))
'''
assert wind_chill(120,35)==40
assert wind_chill(40,70)==86
assert wind_chill(10,100)==116
