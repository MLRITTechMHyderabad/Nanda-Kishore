import random

d1 = [1, 2, 3, 4, 5, 6]
d2 = [1, 2, 3, 4, 5, 6]
li = []

for i in d1:
    for j in d2:
        li.append((i, j))


probability = {}
for i in range(2, 13):
    c = 0
    for j in li:
        if i == j[0] + j[1]:
            c += 1
    probability[str(i)] = c / len(li)

R = int(input().strip())

player1wins = 0
player2wins = 0
for i in range(R):
    player1D1, player1D2 = random.randint(1,6), random.randint(1,6)
    player2D1, player2D2 = random.randint(1, 6), random.randint(1, 6)

    sumofplayer1 = player1D1 + player1D2
    sumofplayer2 = player2D1 + player2D2

    prob1 = probability[str(sumofplayer1)]
    prob2 = probability[str(sumofplayer2)]

    print(f"Round {i+1}:")
    print(f"  Player 1 rolls: {player1D1}, {player1D2} → Sum = {sumofplayer1} (Probability: {prob1:.2%})")
    print(f"  Player 2 rolls: {player2D1}, {player2D2} → Sum = {sumofplayer2} (Probability: {prob2:.2%})")

    if prob1<prob2:
        player1wins+=1
        print("Player1 wins this round")
    elif prob2<prob1:
        player2wins+=1
        print("Player2 wins this round")
    else:
        print("Its Draw")

print("Final Result:  ")
if player1wins>player2wins:
    print("player 1 wins the game")
elif player2wins>player1wins:
    print("player 2 wins the game")
else:
    print("Its draw")