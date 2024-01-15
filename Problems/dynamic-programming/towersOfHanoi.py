class Tower:
    def __init__(self, index):
        self.disks = []
        self.index = index

    def add(self, d):
        if len(self.disks) > 0 and self.disks[-1] <= d:
            print("Error placing disk", d)
        else:
            self.disks.append(d)

    def move_top_to(self, tower):
        top = self.disks.pop()
        tower.add(top)

    """Tower 1 acts as a buffer followed by tower 0 as we cycle items to their destination"""
    def move_disks(self, n, destination, buffer):
        if n > 0:
            self.move_disks(n-1, buffer, destination)
            self.move_top_to(destination)
            buffer.move_disks(n-1, destination, self)
        

def hanoi(n):
    towers = [Tower(i) for i in range(n)]

    for i in range(n, 0, -1):
        towers[0].add(i)

    towers[0].move_disks(n, towers[2], towers[1])

    return towers[2].disks

print(hanoi(3))
print(hanoi(6))
print(hanoi(12 ))