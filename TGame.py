# -----------------------Global Variables-----------------------

# Game board
game_map = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"
]

# Game Status
game_still_going = True

# Player indicator
player_location = "X"

# ----Locations----
def player_location_description():
    if player[0]:
        display_map()
        print("You see a large fountain in the middle of the plaza, "
          "there are some beautiful trees and some people walking "
          "around this bustling area.")
    elif player[1]:
        display_map()
        print("You see a large fountain in the middle of the plaza, "
          "there are some beautiful trees and some people walking "
          "around this bustling area.")
    elif player[2]:
        display_map()
        print("You see a large fountain in the middle of the plaza, "
          "there are some beautiful trees and some people walking "
          "around this bustling area.")
    elif player[3]:
        display_map()
        print("You see a large fountain in the middle of the plaza, "
          "there are some beautiful trees and some people walking "
          "around this bustling area.")
    elif player[4]:
        display_map()
        print("You see a large fountain in the middle of the plaza, "
          "there are some beautiful trees and some people walking "
          "around this bustling area.")
    elif player[5]:
        display_map()
        print("You see a large fountain in the middle of the plaza, "
          "there are some beautiful trees and some people walking "
          "around this bustling area.")
    elif player[6]:
        display_map()
        print("You see a large fountain in the middle of the plaza, "
          "there are some beautiful trees and some people walking "
          "around this bustling area.")
    elif player[7]:
        display_map()
        print("You see a large fountain in the middle of the plaza, "
          "there are some beautiful trees and some people walking "
          "around this bustling area.")
    elif player[8]:
        display_map()
        print("You see a large fountain in the middle of the plaza, "
          "there are some beautiful trees and some people walking "
          "around this bustling area.")


# -----------------------Global Variables-----------------------

# Display board
def display_map():
    print(game_map[0] + " | " + game_map[1] + " | " + game_map[2])
    print(game_map[3] + " | " + game_map[4] + " | " + game_map[5])
    print(game_map[6] + " | " + game_map[7] + " | " + game_map[8])

def start_game():
    display_map()
    handle_turn(player_location)
    player_location_description(player)

def handle_turn(player):

    position = input("Input command> ")

    valid = False
    while not valid:




        position = int(position)

        if game_map[position] == "-":
            valid = True
        else:
            print("Already used try again: ")
    game_map[position] = player
    display_map()


start_game()

#
