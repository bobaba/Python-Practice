from random import randrange
class TSPGrid():
  """ Create a 2 or 3-dimensional grid 
  
  length = the length of x,y,and z \n
  numCities = the number of cities to travel to \n
  dimensions = defaults to 2, optional 3
  setOfPoints = a set of points not randomly generated (optional)\n
  EXAMPLE USE:\n
  twoD = TSPGrid(10,10,2)\n
  twoD.printPrettyGrid()\n
  threeD = TSPGrid(5,10,3)\n
  threeD.printPrettyGrid()\n
  """
  def __init__(self, length, numCities, dimensions = 2, setOfPoints = "null"):
    self.length = length 
    self.numCities = numCities
    self.dimensions = dimensions
    self.grid = []
    self.citiesToVisit = []

    self.createGrid()
    # override random generator with a given set, if preferred
    if setOfPoints == "null":
      self.citiesToVisit = self.generateRandomCities()
    else:
      self.citiesToVisit = setOfPoints

    self.placeCitiesToVisitOnGrid()

  def createGrid(self):
    """ Generate a cube with each side equal to self.length """
    builder = []
    if self.dimensions == 3:
      for x in range(self.length):
        xs = []
        for y in range(self.length):
          ys = []
          for z in range(self.length):
            ys.append(0)
          xs.append(ys)
        builder.append(xs)
    elif self.dimensions == 2:
      for x in range(self.length):
        xs = [] 
        for y in range(self.length):
          xs.append(0)
        builder.append(xs)
    self.grid = builder
      
  
  def printPrettyGrid(self):
    """ print each row in a prettier format """
    
    if self.dimensions == 3:
      for i in self.grid:
        print(i)
    elif self.dimensions == 2:
      i = 0
      while i < self.length: 
        j = 0 
        subr = []
        while j < self.length: 
          if [i,j] in self.citiesToVisit: 
            subr.append(f'{self.citiesToVisit.index([i,j])}')
          else:
            subr.append('-')
          j+=1
        print(" ".join(subr))
        i+=1


  def placeCitiesToVisitOnGrid(self):
    """ put each city onto the grid with a corresponding number, starting at 1 """
    # we start at 1 to separate from a zero space
    if self.dimensions == 3:
      for i in self.citiesToVisit:
        self.grid[i[0]][i[1]][i[2]] = self.citiesToVisit.index(i) + 1
    elif self.dimensions == 2:
      for i in self.citiesToVisit:
        self.grid[i[0]][i[1]] = self.citiesToVisit.index(i) + 1

  
  def generateRandomCities(self):
    """ n-number of Random cities with x,y,z coordinates """
    numDimensions = self.dimensions
    points = []
    while len(points) < self.numCities:
      randomized = []
      for j in range(numDimensions):
        randomized.append(randrange(self.length-1))
      if randomized in points: 
        continue 
      else: 
        points.append(randomized)
    return points

