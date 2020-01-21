from random import randrange
import math 

class ThreeDGrid():
  """ Create a 3-dimensional grid 
  
  length = the length of x,y,and z \n
  numCities = the number of cities to travel to \n
  setOfPoints = a set of points not randomly generated (optional)
  """
  def __init__(self, length, numCities, setOfPoints = "null"):
    self.length = length 
    self.numCities = numCities
    self.grid = []
    self.citiesToVisit = []

    self.create3DGrid()
    # override random generator with a given set, if preferred
    if setOfPoints == "null":
      self.citiesToVisit = self.generateRandomCities()
    else:
      self.citiesToVisit = setOfPoints

    self.placeCitiesToVisitOnGrid()

  def create3DGrid(self):
    """ Generate a cube with each side equal to self.length """
    builder = []
    for x in range(0,self.length):
      xs = []
      for y in range(0,self.length):
        ys = []
        for z in range(0,self.length):
          ys.append(0)
        xs.append(ys)
      builder.append(xs)
    self.grid = builder
  
  def printPrettyGrid(self):
    """ print each row in a prettier format """
    for i in self.grid:
      print(i)


  def placeCitiesToVisitOnGrid(self):
    """ put each city onto the grid with a corresponding number, starting at 1 """
    # we start at 1 to separate from a zero space
    for i in self.citiesToVisit:
      self.grid[i[0]][i[1]][i[2]] = self.citiesToVisit.index(i) + 1

  
  def generateRandomCities(self):
    """ n-number of Random cities with x,y,z coordinates """
    numDimensions = 3
    points = []
    while len(points) < self.numCities:
      randomized = []
      for j in range(0,numDimensions):
        randomized.append(randrange(0,self.length-1))
      if randomized in points: 
        continue 
      else: 
        points.append(randomized)
    return points
  
  def getDistance(self, point1, point2):
    """ Use the Pythagorean Theorem for a 3-dimensional space
    
    distance(a,b) = sqrt( (aX-bX)^2 + (aY-bY)^2 + (aZ-bZ)^2 )
     """
    a = abs(point1[0] - point2[0])
    b = abs(point1[1] - point2[1])
    c = abs(point1[2] - point2[2])
    return math.sqrt(a*a + b*b + c*c)
  
  def nearestNeighbor(self):
    """ Approximate the shortest journey between points 

    find the point in a given set that is closest to a given point
     """
    route = [0]
    while len(route) < len(self.citiesToVisit):
      closestDistance = 9999999999
      closestIndex = 0
      for city in self.citiesToVisit:
        if self.citiesToVisit.index(city) in route: 
          continue 
        else: 
          currDistance = self.getDistance(self.citiesToVisit[route[-1]], city)
          if currDistance < closestDistance: 
            closestDistance = currDistance 
            closestIndex = self.citiesToVisit.index(city)
      route.append(closestIndex)
 
    return route

providedPoints = [[4, 5, 5], [2, 5, 1], [2, 4, 1], [0, 5, 0], [1, 1, 5], [3, 3, 0], [0, 1, 5], [3, 4, 5], [2, 0, 5]]
a = ThreeDGrid(7, 9)
print("Current Grid State:")
a.printPrettyGrid()
print("List of Cities to Visit:")
print(a.citiesToVisit)
print("Optimal Path: ")
# we add 1 to each stop in the route so you can see it on the grid
print([x+1  for x in a.nearestNeighbor()])
        