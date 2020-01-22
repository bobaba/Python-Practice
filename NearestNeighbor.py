import distanceHelpers as dh

class NearestNeighbor():
  """ Approximate the shortest journey between provided points

  this greedy algorithm searches for the next closest point from where it is standing\n
  without going

    """
  def __init__(self, setOfPoints, dimensions = 2):
    self.dimension = dimensions
    self.setOfPoints = setOfPoints 
    self.path = self.runAlgorithm()
    self.optimized = self.optimize_path()
  
  def runAlgorithm(self):
    route = [0]
    while len(route) < len(self.setOfPoints):
      closestDistance = 9999999999
      closestIndex = 0
      for point in self.setOfPoints:
        if self.setOfPoints.index(point) in route: 
          continue 
        else: 
          currDistance = dh.pythagoreanDistance(self.setOfPoints[route[-1]], point, self.dimension)
          if currDistance < closestDistance: 
            closestDistance = currDistance 
            closestIndex = self.setOfPoints.index(point)
      route.append(closestIndex)

    return route
  
  def optimize_path(self):
    route = [0]
    while len(route) < len(self.setOfPoints):
      closestDistance = 9999999999
      closestIndex = 0
      for point in self.setOfPoints:
        if self.setOfPoints.index(point) in route: 
          continue 
        else: 
          currDistance = dh.pythagoreanDistance(self.setOfPoints[route[-1]], point)
          if currDistance < closestDistance: 
            closestDistance = currDistance 
            closestIndex = self.setOfPoints.index(point)
      route.append(closestIndex)

    return route
