import math
class NearestNeighbor():
  """ Approximate the shortest journey between provided points

  returns a list of the optimal route to take where each item is an\n
  element in the array provided in the first parameter 

    """
  def __init__(self, setOfPoints):
    self.dimension = len(setOfPoints[0])
    self.setOfPoints = setOfPoints 
    self.path = self.runAlgorithm()
  
  def runAlgorithm(self):
    route = [0]
    while len(route) < len(self.setOfPoints):
      closestDistance = 9999999999
      closestIndex = 0
      for point in self.setOfPoints:
        if self.setOfPoints.index(point) in route: 
          continue 
        else: 
          currDistance = self.pythagoreanDistance(self.setOfPoints[route[-1]], point)
          if currDistance < closestDistance: 
            closestDistance = currDistance 
            closestIndex = self.setOfPoints.index(point)
      route.append(closestIndex)

    return route

  def pythagoreanDistance(self, point1: list, point2: list) -> float:
    """ a^2 + b^2 = c^2 """
    a = abs(point1[0] - point2[0])
    b = abs(point1[1] - point2[1])
    return math.sqrt(a*a + b*b)