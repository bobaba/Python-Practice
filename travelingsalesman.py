from random import randrange
import math

def create_random_points(numPoints: int, xySize: int) -> list:
  """ Randomly generate a set of points 
  
  Parameters
  ----------
  numPoints : int
    the number of points on salesman's map
  xySize : int
    the bounds of the map
  """
  i = 0
  points = []
  while i < numPoints:
    uniquely = [randrange(0,xySize), randrange(0,xySize)]
    if uniquely not in points:
      points.append(uniquely)
      i += 1
  return points

def printMap(points: list, size: int):
  """ Prints a map of your collected points for visualizing quickly
  
  Points should be an array of arrays : [[8, 1], [7, 5], [6, 2], [1, 2], [0, 0]] - 
  Provide a size to build your map off of. Must be a single integer
  """
  i = 0
  while i < size: 
    j = 0 
    subr = []
    while j < size: 
      if [i,j] in points: 
        subr.append('X')
      else:
        subr.append('O')
      j+=1
    print(" ".join(subr))
    i+=1

def calc_distance(x: list,y: list) -> float:
  """ Calculate the distance between two points using the Pythagorean Theorem """
  a = abs(x[0] - y[0])
  b = abs(x[1] - y[1])
  return math.sqrt(a*a + b*b)

def nearest_neighbor(points: list) -> list:
  """ Use the Nearest Neighbor algorithm for a given set of points
  
  Provide an array of points e.g. [[8, 1], [7, 5], [6, 2], [1, 2], [0, 0]]
  The Nearest Neighbor algorithm is run and returns an array that describes
  what steps to take through the array. e.g. [0, 2, 1, 3, 4]
   """
  travel_this_route = [0] 
  while len(travel_this_route) < len(points):
    # curr_best may need to start higher based on the problem size
    curr_best = 99999999
    fill_with = 0
    i = 0 
    while i < len(points):
      if i in travel_this_route: 
        i+=1
        continue
      this_calc = calc_distance( points[travel_this_route[-1]], points[i] )
      if this_calc < curr_best:
        curr_best = this_calc 
        fill_with = i
      i+=1
    travel_this_route.append(fill_with)
  return travel_this_route

plot = create_random_points(5, 10)
print(plot)
printMap(plot, 10)
print(nearest_neighbor(plot))

