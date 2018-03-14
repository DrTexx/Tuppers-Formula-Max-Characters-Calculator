class gridSize:
    def __init__(self,width,height):
        try: int(width)
        except ValueError: print("width must be an integer!")
        self.h = height
        if (self.w & self.h):
            pass

volumes = {
    'fullGrid': {'width': 106,'height': 17},
    'workspace': {'width': 104, 'height': 15},
    'char': {'width': 10, 'height': 15},
    'space': {'width': 2, 'height': 15}
}