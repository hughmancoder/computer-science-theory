"""
The trick is to use a balance scale to compare the weight of the pills by taking one pill from bottle on, two from bottle two, etc.

Expected Total Weight = 1 + 2 + 3 + ... + 20 = (20 / 2) * (1 + 20) = 210

Let i be the index of the bottle with the heavy pill

NetWeight - i * 1 = 210 - i * 1.1

i = (NetWeight - 210) / 0.1

"""

def findHeavyPill(weights):
    totalWeight = 0
    for i, w in enumerate(weights):
        totalWeight += w * (i + 1)
    
    index = (totalWeight - 210) // 0.1
    print("The heavy pill is in bottle " + str(index))
    return index
    

weights = [1,1,1,1,1,1,1,1,1,1,1.1,1,1,1,1,1,1,1,1,1]
print(findHeavyPill(weights) == weights.index(1.1))
    
