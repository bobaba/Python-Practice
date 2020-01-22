import math

def pythagoreanDistance(point1: list, point2: list, dimensions = 2) -> float:
  """ a^2 + b^2 = c^2 """
  a = abs(point1[0] - point2[0])
  b = abs(point1[1] - point2[1])
  if dimensions == 3:
    c = abs(point1[2] - point2[2])
    return math.sqrt(a*a + b*b + c*c)
  else:
    return math.sqrt(a*a + b*b)

def getDistanceOfRoute(route: list, cities: list, dimensions = 2) -> float:
  """ return the distance traveling the specified route """
  distance = 0
  for i in range(len(route)-1):
    distance += pythagoreanDistance(cities[route[i]], cities[route[i+1]], dimensions)
  return distance