class Tower:
    def __init__(self, index):
        self.disks = []
        self.index = index

    def add(self, d):
        if len(self.disks) > 0 and self.disks[-1] <= d:
            print("Error placing disk", d)
        else:
            self.disks.append(d)

    def move_top_to(self, t):
        # Implement this method

    def move_disks(self, n, destination, buffer):
        # Implement this method

def hanoi(n):
    towers = [Tower(i) for i in range(3)]

    for i in range(n, 0, -1):
        towers[0].add(i)

    towers[0].move_disks(n, towers[2], towers[1])

hanoi(3)