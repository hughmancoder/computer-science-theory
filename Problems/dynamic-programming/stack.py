class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

def can_be_above(bottom, top):
    if bottom is None:
        return True
    if bottom.width > top.width and bottom.height > top.height and bottom.depth > top.depth:
        return True
    return False

def max_stack_height(boxes, bottom_index):
    if bottom_index < len(boxes) and memo[bottom_index] > 0:
        return memo[bottom_index]
    bottom = boxes[bottom_index]
    max_height = 0
    for i in range(bottom_index + 1, len(boxes)):
        if can_be_above(bottom, boxes[i]):
            height = max_stack_height(boxes, i)
            max_height = max(max_height, height)
    max_height += bottom.height
    memo[bottom_index] = max_height
    return max_height

def create_stack(boxes):
    boxes.sort(key=lambda x: x.height, reverse=True)
    global memo
    memo = [0] * len(boxes)
    max_h = 0
    for i in range(len(boxes)):
        height = max_stack_height(boxes, i)
        max_h = max(max_h, height)
    return max_h

# Test the function
boxes_1 = [Box(1, 3, 1), Box(2, 2, 2), Box(3, 1, 3), Box(2, 3, 2)]

boxes_2 = [
    Box(3, 4, 1),
    Box(8, 6, 2),
    Box(4, 5, 3)
]
print(create_stack(boxes_1))  
print(create_stack(boxes_2))  