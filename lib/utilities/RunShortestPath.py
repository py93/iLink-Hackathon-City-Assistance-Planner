
import os

def RunShortestPath(ox, oy, dx, dy):
    # stream = os.popen('java test 1 2 3')
    # output = stream.read()
    # return output
    return '{"dist": 4, "path":[[' + str(ox) + ', ' + str(oy) + '], [' + str(dx) + ', ' + str(dy) + ']]}'
