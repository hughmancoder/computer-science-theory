class PaintFill:
    offsets = [[0,1],[0,-1],[1,0],[-1,0]]
    def __init__(self, screen):
        self.screen = screen

    def is_valid(self, x, y):
        return x >= 0 and x < len(self.screen) and y >= 0 and y < len(self.screen[0])
    
    def fill(self, point, new_color):
        colour = self.screen[point[0]][point[1]]
        self.screen[point[0]][point[1]] = new_color
        for x, y in self.offsets:
            new_x = point[0] + x
            new_y = point[1] + y
            if self.is_valid(new_x, new_y) and self.screen[new_x][new_y] == colour and self.screen[new_x][new_y] != new_color:
                self.fill((new_x, new_y), new_color)
        

def test_paint_fill():
    screen = [
        ['red', 'red', 'blue'],
        ['red', 'blue', 'blue'],
        ['blue', 'blue', 'blue']
    ]
    paint_fill = PaintFill(screen)
    
    paint_fill.fill((0, 1), 'green')

    assert paint_fill.screen == [
        ['green', 'green', 'blue'],
        ['green', 'blue', 'blue'],
        ['blue', 'blue', 'blue']
    ]

    print("All tests passed!")


test_paint_fill()