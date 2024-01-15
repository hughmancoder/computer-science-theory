import random

# Simulation
def simulate():
    epoch_size = int(1e5)
    girls = 0
    boys = 0
    for i in range(epoch_size):
        while True:
            has_girl = random.randint(0, 1) >= 0.5
            if has_girl:
                girls += 1
                break
            else:
                boys += 1

    print(f"outcome yields {girls} girls and {boys} boys with girls:boys gender ratio {girls/boys}", {girls, boys})

simulate()

# Logical solution
"""
Assumption: Each child has an equal probability (50%) of being a boy or a girl.

Family Behavior: Each family keeps having children until they have a girl, then stops.

For each family: The probability of having a girl on the first try is 50%

If not a girl, then the probability of having a girl on the second try is also 50%, but the probability of reaching this point is 50% (since the first child was a boy). So, the probability of having a boy first and a girl second is 0.5 x 0.5 = 0.25

This pattern continues. The probability of having a girl after n boys is (0.5)^(n+1)

The expected number of boys in a family before having a girl is calculated as the sum of boys in each scenario, weighted by the probability of that scenario. 

This is the infinite series: 0.5 + 0.5^2 + 0.5^3 + ... = 0.5/(1-0.5) = 1

Since there is 1 girl per family (as families stop after having a girl), the gender ratio in the new generation would be approximately 1:1 (boys:girls)
"""