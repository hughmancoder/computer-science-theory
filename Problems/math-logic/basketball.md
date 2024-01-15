# Basketball

## Game 1

Probability = p

## Game 2

Let X denote amount of shots
P(X >= 2) = P(X = 2) + P(X = 3)

Making 2/3 shots follows a binomial distribution
(p,~p,p), (p,p,~p), (~p,p,p)

    Probability = P(X = 2) = p^2 * (1-p) * 3C2
    = p^2 * (1-p) * 3

    P(X = 3) = p^3 * 3C3 = p^3

    Hence P(X >= 2) = 3p^2 - 2p^3

## Comparing outcomes

    Play game 1 given P(game 1) > P(game 2)

    p > 3p^2 - 2p^3

    (p-1)(2p - 1) > 0

    If 0 < p < 1/2, play game 1

    Else if 1/2 < p < 1, play game 2

    If p = 0, 1, or 1/2, play either game
