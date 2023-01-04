"""
G-Man energy calculator
Calculates G-Man's remaining energy after a specified move on the grid.

Assumptions:
- the grid is hardcoded to 6x6 but since G-Man moves along the edges of the grid
    the co-ordinates range from 0-6 for x and y giving 7 possible values for each.
- G-Man moves along four cardinal directions only N, S, E, W
- G-Man spends 5 energy for turning and 10 for moving one grid space
- since there are no obstacles, the move that uses the least energy will be
    either a straight line or an L shaped route
"""


def calculate_remaining_power(power, source_x, source_y, destination_x, destination_y, direction):
    # calculate destination_directions as a list of maximum 2 cardinal directions G-Man has to turn to
    destination_directions = []

    # add N or S to the list
    if destination_y > source_y:
        destination_directions.append("N")
    elif destination_y < source_y:
        destination_directions.append("S")

    # add W or E to the list
    if destination_x > source_x:
        destination_directions.append("E")
    elif destination_x < source_x:
        destination_directions.append("W")

    # at this point we can check if G-Man has to move at all
    # if the destination_directions list is empty then source and destination are the same locations
    if len(destination_directions) == 0:
        return 200

    #######################################
    # Calculating energy usage for tuning #
    #######################################
    # we have established G-Man will either move in a straight line or along an L shaped route
    # if destination_direction list contains 2 elements then we are dealing with the latter case
    # G-man will need to turn once or twice depending on whether he is already facing in one of the listed directions
    if len(destination_directions) == 2:
        if direction in destination_directions:
            power -= 5
        else:
            power -= 10

    # if destination list contains only 1 element then G-Man will be moving in a straight line
    # worst case scenario he will need to turn 2 times; best case: 0
    else:
        # opposite source and destination directions mean 2 turns
        if (direction == "N" and destination_directions[0] == "S") or (
                direction == "S" and destination_directions[0] == "N") \
                or (direction == "W" and destination_directions[0] == "E") or (
                direction == "E" and destination_directions[0] == "W"):
            power -= 10

        # if G-Man is already facing the right direction do nothing
        elif direction == destination_directions[0]:
            pass

        # remaining cases mean G-Man will turn only once
        else:
            power -= 5

    #######################################
    # Calculating energy usage for moving #
    #######################################

    # calculate the power usage for moving along the x-axis
    x_locs = [source_x, destination_x]
    x_locs.sort()
    power -= (x_locs[1] - x_locs[0]) * 10

    # calculate the power usage for moving along the y-axis
    y_locs = [source_y, destination_y]
    y_locs.sort()
    power -= (y_locs[1] - y_locs[0]) * 10


    return power


if __name__ == '__main__':
    # get input variables form user
    # source and destination co-ordinates and G-Mans facing direction
    source_x = 0
    source_y = 0
    destination_x = 0
    destination_y = 0
    direction = "N"
    power = 200

    # set of possible grid values and directions
    grid_values = {0, 1, 2, 3, 4, 5, 6}
    directions = {"N", "S", "E", "W"}
    while True:
        user_input = input("Input source co-ordinates followed by G-Man's facing "
                           "direction separated by spaces (e.g.: 2 4 E)\n>").split()
        if len(user_input) != 3:
            print("Invalid input. Try again.")
            continue

        source_x = user_input[0]
        if source_x.isnumeric() and int(source_x) in grid_values:
            source_x = int(source_x)
        else:
            print("Invalid input. Co-ordinates must be in range from 0 to 6. Try again.")
            continue

        source_y = user_input[1]
        if source_y.isnumeric() and int(source_y) in grid_values:
            source_y = int(source_y)
        else:
            print("Invalid input. Co-ordinates must be in range from 0 to 6. Try again.")
            continue

        if user_input[2].strip().upper() in directions:
            direction = user_input[2].strip().upper()
        else:
            print("Invalid input. Try again.")
            continue
        break

    while True:
        user_input = input("Input destination co-ordinates separated by a space (e.g.: 6 0)\n>").split()
        if len(user_input) != 2:
            print("Invalid input. Try again.")
            continue

        destination_x = user_input[0]
        if destination_x.isnumeric() and int(destination_x) in grid_values:
            destination_x = int(destination_x)
        else:
            print("Invalid input. Co-ordinates must be in range from 0 to 6. Try again.")
            continue

        destination_y = user_input[1]
        if destination_y.isnumeric() and int(destination_y) in grid_values:
            destination_y = int(destination_y)
        else:
            print("Invalid input. Co-ordinates must be in range from 0 to 6. Try again.")
            continue

        break

    ###################################
    # Display G-Man's remaining power #
    ###################################
    # invoke the function that calculates and displays G_man's remaining power
    power = calculate_remaining_power(power, source_x, source_y, destination_x, destination_y, direction)
    print("G-Man has arrived at his destination.")
    print(f"Power Left: {power}")


