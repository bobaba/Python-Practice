import math

def pythagoreanDistance(point1: list, point2: list) -> float:
  """ a^2 + b^2 = c^2 """
  a = abs(point1[0] - point2[0])
  b = abs(point1[1] - point2[1])
  return math.sqrt(a*a + b*b)

def getDistanceOfRoute(route: list, cities: list) -> float:
  """ return the distance traveling the specified route """
  distance = 0
  for i in range(len(route)-1):
    distance += pythagoreanDistance(cities[route[i]], cities[route[i+1]])
  return distance