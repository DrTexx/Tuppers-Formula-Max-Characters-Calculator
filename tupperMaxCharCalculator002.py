# Tupper's Formula Max Character Calculator
# Coded by Denver P.
# 2018
from tupperMaxCharCalculator001 import gridSize

runTests = True

class gridSize:
    def __init__(self,width,height):
        # width must be an integer to set it
        if (isinstance(width, int)):
            self.w = width
        else:
            raise TypeError("width must be an integer!")
        # height must be an integer to set it
        if (isinstance(height, int)):
            self.h = height
        else:
            raise TypeError("height must be an integer!")
        # calculate and define the volume used
        self.v = self.w * self.h

if(runTests):
    # generate an instance of gridSize class named testIns
    testIns = gridSize(104,15)
    # print the values for the instance testIns
    print(vars(testIns))

volumes = {
    'fullGrid': gridSize(106,17),
    'workspace': gridSize(104,15),
    'char': gridSize(10,15),
    'space': gridSize(2,15)
}

if(runTests):
    print("volumes contents:")
    for item in volumes:
        print("item:",item,"=",vars(volumes[item]))
