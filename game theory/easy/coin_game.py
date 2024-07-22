''''

2 player turn based game with n coins

p1 moves first
    3 moves - take 1,3 or 4 coins

player to take away last coin wins

no skips

''''




''''

same, but moves are 2^k coins, k any whole number

n = 0 L
n = 1 W
n = 2 W
n = 3 L ;take 1 or 2 and go to n =2 or n =1, which is winning pos -> is losing pos
n= 4 W 
n = 5 W ;take 1 or 2 or 4 and go to n = 4 or n =3 or n=1; 1 L state (n=3) ->W

2 states - n%3 =0 and n%3>0 (1 or 2)
if n%3 > 0, can take 1 or 2 to reach state n%3=0
from n%3=0, only can go to n %3 =0 state ; -> 0 -> Losing state

so p1 wins if n%3>0
''''
# TODO