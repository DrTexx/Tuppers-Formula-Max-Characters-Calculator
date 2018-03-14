# Tupper's Formula Max Character Calculator
# Coded by Denver P.
# 2018

runTests = True

class sizeOnGrid:
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
    # generate an instance of sizeOnGrid class named testIns
    testIns = sizeOnGrid(104,15)
    # print the values for the instance testIns
    print(vars(testIns))

# values subject to change, in particular the width of char & space and the width & height of border
# something along the lines of "standards" or the like may be a better name for this dictionary
areas = {
    'fullGrid': sizeOnGrid(106,17),
    'gridBorder':sizeOnGrid(2,2),
    'char': sizeOnGrid(10,15),
    'space': sizeOnGrid(2,15)
}
# calculate the workspace dimensions and area based on the values found in fullGrid and gridBorder
areas['workspace'] = sizeOnGrid(
    areas['fullGrid'].w - areas['gridBorder'].w,
    areas['fullGrid'].h - areas['gridBorder'].h
)

if(runTests):
    print("areas' contents:")
    for item in areas:
        print("item:",item,"=",vars(areas[item]))

# accepts only instances in the form of sizeOnGrid class
def canXfitY(area,contents):
#    print("area volume:",area)
#    print("contents volume:",contents)
    print("can you fit",contents,chr(0x00B2),"within",area,chr(0x00B2),"?")
#    print("(or, is",area,"-",contents,">= 0?)")
    if(area-contents >= 0):
        return True
    else:
        return False

no_of_chars = 1
print("no.# of characters in drawing:",no_of_chars)
print("no.# of spaces in drawing:",no_of_chars)
no_of_spaces = no_of_chars

print(canXfitY(areas['workspace'].v, areas['char'].v*no_of_chars+areas['space'].v*no_of_spaces))