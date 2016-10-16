# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def check_neighbor(grid, position, cost):
    result = []
    grid[position[1]][position[2]] = 1
    for i in delta:
        newdelta = [i[0]+position[1], i[1]+position[2]]
        if newdelta[0]>-1 and newdelta[0]<len(grid) \
            and newdelta[1]>-1 and newdelta[1]<len(grid[0]):
            if grid[newdelta[0]][newdelta[1]] == 0:
                grid[newdelta[0]][newdelta[1]] = 1
                newdelta.insert(0,position[0]+cost)
                result.append(newdelta)
    return result, grid

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    init.insert(0,0)
    positions = [init]
    while True:
        print positions
        if len(positions)==0:
            print "fail"
            return None

        for position in positions:
            positions.remove(position)

            print "Take list item %s" % (position)

            results, grid = check_neighbor(grid, position, cost)
            if results:
                print "new open list:"
                for result in results:
                    print "\t%s" % (result)
                    if result[1]==goal[0] and result[2]==goal[1]:
                        print "########"
                        print "search successful"
                        print result
                        return result
        positions+=results
    

search(grid, init, goal, cost)