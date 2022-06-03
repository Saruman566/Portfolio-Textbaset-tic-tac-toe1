
def play_ground():

    playground = {'up': [1, 2, 3, ],
                  'middle': [4, 5, 6, ],
                  'down': [7, 8, 9, ]}

    for keys in playground:
        playground[keys] = str(playground[keys]).replace(',', '')

    player_one(playground)


def player_one(playground):

    print(f"\n{playground['up']}\n{playground['middle']}\n{playground['down']}")

    player_input = str(input("\nPlayer 1 please choose a number to get a 'x' on this field."))

    if player_input.isdigit() is True:
        player_input = str(player_input)
        playground_new(playground, player_input=player_input, player=player_one)
    else:
        print("Please enter numbers only 1-9!")
        print('Please try again.')
        player_input = str(input("\nPlayer 1 please choose a number to get a 'x' on this field."))
        playground_new(playground, player_input=player_input, player=player_one)


def player_two(playground):

    print(f"\n{playground['up']}\n{playground['middle']}\n{playground['down']}")

    player_input_two = str(input("\nPlayer 2 please choose a number to get a 'o' on this field."))

    if player_input_two.isdigit() is True:
        player_input_two = str(player_input_two)
        playground_new(playground, player_input=player_input_two, player=player_two)
    else:
        print("Please enter numbers only 1-9!")
        print('Please try again.')
        player_input_two = str(input("\nPlayer 2 please choose a number to get a 'o' on this field."))
        playground_new(playground, player_input=player_input_two, player=player_two)


def winner(playground):

    any_up = []
    any_middle = []
    any_down = []

    for lists in playground['up']:
        any_up.append(lists)

    for lists in playground['middle']:
        any_middle.append(lists)

    for lists in playground['down']:
        any_down.append(lists)

    any_up.remove(']')
    any_up.remove('[')
    any_up.remove(' ')
    any_up.remove(' ')
    any_middle.remove(']')
    any_middle.remove('[')
    any_middle.remove(' ')
    any_middle.remove(' ')
    any_down.remove(']')
    any_down.remove('[')
    any_down.remove(' ')
    any_down.remove(' ')

    if any_up[0] == 'x' and any_up[1] == 'x' and any_up[2] == 'x':
        return True
    elif any_middle[0] == 'x' and any_middle[1] == 'x' and any_middle[2] == 'x':
        return True
    elif any_down[0] == 'x' and any_down[1] == 'x' and any_down[2] == 'x':
        return True
    elif any_up[0] == 'x' and any_middle[1] == 'x' and any_down[2] == 'x':
        return True
    elif any_up[2] == 'x' and any_middle[1] == 'x' and any_down[0] == 'x':
        return True
    elif any_up[0] == 'x' and any_middle[0] == 'x' and any_down[0] == 'x':
        return True
    elif any_up[1] == 'x' and any_middle[1] == 'x' and any_down[1] == 'x':
        return True
    elif any_up[2] == 'x' and any_middle[2] == 'x' and any_down[2] == 'x':
        return True
    elif any_up[0] == 'o' and any_up[1] == 'o' and any_up[2] == 'o':
        return True
    elif any_middle[0] == 'o' and any_middle[1] == 'o' and any_middle[2] == 'o':
        return True
    elif any_down[0] == 'o' and any_down[1] == 'o' and any_down[2] == 'o':
        return True
    elif any_up[2] == 'o' and any_middle[1] == 'o' and any_down[0] == 'o':
        return True
    elif any_up[0] == 'o' and any_middle[1] == 'o' and any_down[2] == 'o':
        return True
    elif any_up[0] == 'o' and any_middle[0] == 'o' and any_down[0] == 'o':
        return True
    elif any_up[1] == 'o' and any_middle[1] == 'o' and any_down[1] == 'o':
        return True
    elif any_up[2] == 'o' and any_middle[2] == 'o' and any_down[2] == 'o':
        return True
    else:
        return False


def playground_new(playground, player_input, player):

    if player == player_one:
        for keys in playground:
            if player_input in playground[keys]:
                playground[keys] = playground[keys].replace(player_input, 'x')
                if winner(playground):
                    print('Congratulations... Player 1 is the winner!')
                    again = input('Play again? "y" for Yes or any Key for quit').lower()
                    if again == 'y':
                        play_ground()
                    else:
                        quit()
                else:
                    player_two(playground)

    if player == player_two:
        for keys in playground:
            if player_input in playground[keys]:
                playground[keys] = playground[keys].replace(player_input, 'o')
                if winner(playground):
                    print('Congratulations... Player 2 is the winner!')
                    again = input('Play again? "y" for Yes or any Key for quit').lower()
                    if again == 'y':
                        play_ground()
                    else:
                        quit()
                else:
                    player_one(playground)


play_ground()
