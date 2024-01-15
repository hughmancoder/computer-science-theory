# Ants on a Triangle

A collision will occur if two ants move in the same direction (clockwise/counter clockwise)

P(clockwise) = (1/2)^3
P(counter clockwise) = (1/2)^3
P(Same direction) = (1/2)^3 + (1/2)^3 = 1/4

Hence P(collision) = 1 - P(Same direction) = 0.75

## Ants on an n-Vertex Polygon

P(same direction) = 2 \* (1/2)^n = (1/2)^(n-1)

P(collision) = 1 - (1/2)^(n-1)
