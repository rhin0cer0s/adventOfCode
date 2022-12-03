#! /usr/bin/env python3

import fileinput

"""

=== Part I

A = Rock      = X
B = Paper     = Y
C = Scissors  = Z

Score
Rock = 1
Paper = 2
Scissors = 3

Lost = 0
Draw = 3
Win = 6


Rock Paper Scissors victory matrix

|-----------------------|
| A\B |  R  |  P  |  S  |
|-----|-----|-----|-----|
|  R  |  0  |  B  |  A  |
|-----|-----|-----|-----|
|  P  |  A  |  0  |  B  |
|-----|-----|-----|-----|
|  S  |  B  |  A  |  0  |
|-----------------------|

Let's define player A as the other player - the input's first column :

|-----------------------|
| A\B |  R  |  P  |  S  |
|-----|-----|-----|-----|
|  R  |  3  |  6  |  0  |
|-----|-----|-----|-----|
|  P  |  0  |  3  |  6  |
|-----|-----|-----|-----|
|  S  |  6  |  0  |  3  |
|-----------------------|

And include shape weights

|-----------------------|
| A\B |  R  |  P  |  S  |
|-----|-----|-----|-----|
|  R  |  4  |  8  |  3  |
|-----|-----|-----|-----|
|  P  |  1  |  5  |  9  |
|-----|-----|-----|-----|
|  S  |  7  |  2  |  6  |
|-----------------------|

=== Part 2

|-----------------------|
| A\B |  L  |  D  |  W  |
|-----|-----|-----|-----|
|  R  |  S  |  R  |  P  |
|-----|-----|-----|-----|
|  P  |  R  |  P  |  S  |
|-----|-----|-----|-----|
|  S  |  P  |  S  |  R  |
|-----------------------|

"""

RPS_matrix = { 
    'A' : {'X' : 4, 'Y' : 8, 'Z' : 3},
    'B' : {'X' : 1, 'Y' : 5, 'Z' : 9},
    'C' : {'X' : 7, 'Y' : 2, 'Z' : 6},
}

RPS_cheating_moves = { 
    'A' : {'X' : 'Z', 'Y' : 'X', 'Z' : 'Y'},
    'B' : {'X' : 'X', 'Y' : 'Y', 'Z' : 'Z'},
    'C' : {'X' : 'Y', 'Y' : 'Z', 'Z' : 'X'},
}

final_score = 0
final_score_2 = 0

for round in fileinput.input() :
    if (round[0] == '\n') :
        break
    player_A = round[0]
    player_B = round[2]
    final_score += RPS_matrix[player_A][player_B]

    final_score_2 += RPS_matrix[player_A][RPS_cheating_moves[player_A][player_B]]

fileinput.close()
print(f"[P1] final score : {final_score}")
print(f"[P2] final score : {final_score_2}")

"""
Part II

X = Lose
Y = Draw
W = Win

"""