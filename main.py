import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(art.logo)

while True:
    perm = input('Do you want to play game? y or n ')
    if perm == 'n':
        break

    player = []
    comp = []
    player.append(random.choice(cards))
    player.append(random.choice(cards))
    comp.append(random.choice(cards))
    comp.append(random.choice(cards))

    print(f"your cards {player} current sum : {sum(player)}")
    print(f"computer first card : {comp[0]}")
    if sum(player) == 21 and len(player) == 2:
        print(f" You won  your cards : {player}")
        continue
    elif sum(comp) == 21 and len(comp) == 2:
        print(f"You lose comp cards: {comp}")
        continue

    while True:
        choice = input('y for another card and n for pass')
        if choice == 'y':
            player.append(random.choice(cards))
            if 11 in player and sum(player) > 21:
                player[player.index(11)] = 1
            if sum(player) > 21:
                print(f'You Lose!!! your cards {player} comp cards {comp}')
                  # Set the flag to end the outer loop
                break
            else:
                print(f"your cards {player} current sum : {sum(player)}")
                print(f"computer first card : {comp[0]}")

                comp.append(random.choice(cards))
                if sum(comp) > 21:
                    print(f"You Win you cards {player} comp cards {comp}")
                elif sum(comp) < 21 and sum(comp) > sum(player):
                    print(f'You Lose your cards {player} comp cards {comp}')
                elif sum(player) < 21 and sum(player) > sum(comp):
                    print(f"You Win you cards {player} comp cards {comp}")
                elif sum(player) == sum(comp):
                    print(f'Draw your cards {player} comp cards {comp} ')
        elif choice == 'n':
            while sum(comp) < 17:
                comp.append(random.choice(cards))
                if 11 in comp and sum(comp) > 21:
                    comp[comp.index(11)] = 1
            if sum(comp) > 21:
                print(f"You Win you cards {player} comp cards {comp}")
            elif sum(comp) < 21 and sum(comp) > sum(player):
                print(f'You Lose your cards {player} comp cards {comp}')
            elif sum(comp) < sum(player) and sum(player) < 21:
                print(f"You Win you cards {player} comp cards {comp}")
            elif sum(comp) == sum(player):
                print(f'Draw your cards {player} comp cards {comp} ')
            else:
                print(f" Your Cards {player} ")
            break


print('Finished')