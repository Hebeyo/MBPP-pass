'''Write a function to find the minimum number of platforms required for a railway/bus station.
'''
def find_platform(arr, dep, n):
  arr.sort()
  dep.sort()
  plat_needed = 1
  result = 1
  i = 1
  j = 0
  while (i < n and j < n):
    if (arr[i] <= dep[j]):
      plat_needed+= 1
      i+= 1
    elif (arr[i] > dep[j]):
      plat_needed-= 1
      j+= 1
    if (plat_needed > result):
      result = plat_needed
  return result
'''
Standard answer: 
def find_platform(arr, dep, n): 
    arr.sort() 
    dep.sort() 
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    while (i < n and j < n): 
        if (arr[i] <= dep[j]):           
            plat_needed+= 1
            i+= 1
        elif (arr[i] > dep[j]):           
            plat_needed-= 1
            j+= 1
        if (plat_needed > result):  
            result = plat_needed           
    return result
'''
assert find_platform([900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000],6)==3
assert find_platform([100,200,300,400],[700,800,900,1000],4)==4
assert find_platform([5,6,7,8],[4,3,2,1],4)==1
