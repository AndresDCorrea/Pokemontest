import os
import time
import readchar




def print_string(string):
    string = [list(row) for row in string.split("\n")]
    MAP_WIDTH = len(string[0])
    MAP_HEIGHT = len(string)
    # top
    print(upper_left_corner, end="")
    print(upper_and_bottom_limit * MAP_WIDTH, end="")
    print(upper_right_corner)

    for coordinate_y in range(MAP_HEIGHT):

        print(side_walls, end="")
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = string[coordinate_y][coordinate_x]
            print("{}".format(char_to_draw), end="", flush=True)
            time.sleep(0.001)


        print(side_walls)

    #bottom
    print(bottom_left_corner,end="")
    print(upper_and_bottom_limit * MAP_WIDTH,end="")
    print(bottom_right_corner)

#strings pokemons
pikachu_string = """\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⢀⠀⠀⠀⠀⠀⠀⢀⠔⠋⠁⠀⠀     
⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠒⠊⠉⠉⠁⣽⣿⣿⡿⠋⠀⠀⠀⠀⣠⠖⠁⠀⠀⠈⠀⠀     
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢀⠇⢀⣀⣀⣀⣀⣀⠀⠀⠀⢀⡠⠔⠊⠁⠀⠀⠀⠀⠀⠀⢠⣿⡿⠋⠁⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⡄⠀     
⠀⠀⠀⠀⠀⠀⠀⢸⣀⠴⠋⠉⠁⠀⠀⠀⠀⠀⠉⠙⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠛⠁⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⢠⠀     
⠀⠀⠀⠀⠀⠀⢀⠞⠁⠀⠀⠀⠀⠀⠀⣾⢙⣶⡄⠀⠀⠰⢤⣠⡤⠤⠔⠒⠂⠉⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀     
⠀⠀⠀⠀⠀⠀⣮⣞⣹⠀⠀⠀⠀⠀⠀⠙⠿⠿⠃⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠼⠃     
⠀⠀⠀⠀⠀⢰⠛⠿⠁⣈⣀⣀⣀⣤⠀⠀⠀⢠⠖⠒⠲⡄⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⢰⠧⠤⠔⠂⠐⠈⠈⠀⠀⠀⣠⠔⠊⠁⠀⠀     
⠀⠀⠀⠀⢠⡟⣇⠀⠉⢿⣿⣿⣿⣿⠀⠀⠀⢯⡐⠲⣠⡇⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⣠⠔⠋⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⠸⣦⡟⠀⠀⠈⢿⠟⠛⢻⠀⠀⠀⠀⠙⠚⠋⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠳⣄⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⢀⣀⠬⠷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠚⠃⠢⢄⠀⠈⢣⡀⠀⠀⠀⠀⠀⢀⡽⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⣤⠔⠊⠁⠀⠀⠀⠈⠳⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⢿⠁⠀⠀⠀⠈⠀⠀⠘⡿⢆⠀⠀⣠⠔⠉⠀⠀⣀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠐⡏⠸⠀⠀⠀⠀⠀⠀⠀⢢⠀⠈⠳⢄⣀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⣀⡀⠀⠀⠀⠱⡈⠣⡀⠀⢠⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠻⠦⢤⣀⠀⠀⠀⠀⠀⠀⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠤⠼⠛⠁⠀⠀⠀⠀⠘⣆⠙⢶⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⠀⠉⠉⠙⠒⠒⠒⠒⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠳⣾⣿⣿⡿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⡘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⣀⡤⠔⠲⣶⣆⣀⡀⠀⠐⠤⠤⠔⠒⠉⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠤⣥⠤⢴⠚⠉⠀⠀⠀⠈⠉⠒⠂⠤⠤⢤⡤⠞⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢋⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \
"""
snorlax_string ="""\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠍⠋⠻⢿⠷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⡘⠠⢀⠈⢷⣯⣛⠿⣷⣄⣀⣀⣤⣤⠤⠤⠤⠤⢤⣤⣄⣀⠀⠀⠀⠀⠀⢀⣠⡤⠾⠿⠉⠉⡁⢀⢈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢯⡀⠄⡁⠀⡄⠠⠙⢿⣿⣼⣝⣿⡿⠃⠀⢀⠀⠄⢀⠠⡀⢌⠉⡉⠛⣶⣤⠶⠛⠙⠠⢀⠂⠠⠀⠉⠀⣼⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠤⡠⠠⠀⢃⠠⠄⡃⢀⠘⠿⠻⠟⠀⠀⠀⠀⠄⡀⠄⠄⢃⠀⡀⢸⣼⠟⠃⠃⠄⠘⠀⠀⢄⠃⠄⠃⠤⣸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠰⠄⠡⠐⠀⢂⠐⠀⠂⠀⠀⠀⠀⠀⠀⠀⢀⠂⠡⢈⠐⠂⠄⠀⠈⠁⠀⠄⠐⠀⠠⠑⡈⠄⡈⠐⢠⠒⣽⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠄⠃⠄⠡⠈⠀⠀⢁⠈⢀⠡⢀⡠⠀⡄⠈⠄⡈⠄⡡⢈⠐⠠⠈⠀⠄⡁⠠⢈⠀⡁⢂⠡⢐⠠⢁⣮⣹⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠧⠐⠈⠄⠡⠀⠌⡀⢀⣄⡄⠂⠄⢠⠁⠄⡁⢂⠁⢀⠀⠄⢀⠠⠀⢁⡀⠠⠐⠀⠢⠐⡀⠂⠄⠂⣼⢛⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⠀⠐⡀⡈⣄⣵⠾⠛⠋⠉⢻⣆⠈⠄⢈⠐⡠⠈⠄⡀⠠⠀⣤⡾⠛⠳⠶⣤⣀⠃⠄⠑⢈⠁⠠⣙⢣⣿⣿⣽⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠁⠀⠀⢠⣴⠞⠋⠀⠀⠀⠀⠀⠀⠻⣧⡀⠀⢂⠐⠠⠀⡀⣢⡾⠋⠀⠀⠀⠀⠀⠙⠻⢦⣄⠂⢀⢣⢼⣿⡿⣾⡽⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠞⢉⣿⠇⠀⢀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣾⣴⡪⣔⣱⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⣎⡾⣿⣻⣽⣳⢿⡽⣿⣿⣽⣻⢿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠞⠉⠁⠀⢠⢾⣿⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢧⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣳⢯⣿⣻⣟⣿⣿⣷⢯⡿⣾⣽⣻⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠖⠻⠁⠀⠀⠀⠀⠄⠂⣘⣿⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣯⢷⡿⣞⣿⣿⣯⡿⣽⣳⢯⡷⣿⣾⠄⠉⠻⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠛⠉⠀⠀⠀⠀⠀⠈⡈⠀⠐⠈⢿⣇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣯⢿⣻⣿⣿⣯⣟⡿⣽⢯⡿⣽⡗⠨⠁⢀⠠⠙⠷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢂⠐⠌⠠⠐⠘⣿⣿⡇⠀⠀⠘⠳⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡄⠀⠀⠀⢸⣿⣯⡿⣷⣿⣿⣳⢯⣟⣯⢿⣽⢳⠈⠄⠐⡀⠀⠌⠐⠘⠻⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀⠀⠠⠀⠀⠀⠀⠀⠁⠠⠈⡄⠡⠀⠂⡉⢿⣿⣄⠀⠀⠀⠀⠀⠈⠉⠙⠛⠒⠚⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⡗⠶⠖⠶⠶⠒⠚⠛⠋⠀⠀⠀⠀⠀⢸⣿⡿⣽⣿⣿⣳⢯⡿⣽⢾⣟⣎⠣⠐⡈⠄⡀⠡⠀⠌⠀⠄⠃⢹⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠇⠀⣀⠐⠂⠀⠀⠐⠀⠀⠀⡐⠀⡁⠂⡄⠡⠌⠀⠄⠌⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣟⡷⣯⢿⡽⣯⡿⠚⡄⢁⠂⠄⠠⠐⡀⠌⠠⠈⡀⠄⢂⠨⠝⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⡕⠀⠀⡁⠄⠂⡁⠆⠈⠄⠒⠌⠀⡀⠌⠠⠁⠄⠡⢈⠠⣀⣦⣸⣴⣿⣿⣦⡀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⣿⣳⢯⢿⡽⢯⡟⢧⠃⠅⡐⢈⠐⡈⠐⡀⠀⠂⠐⠀⠄⡈⠄⢂⠐⠠⢹⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⣗⢮⣑⢢⢄⠢⡐⢄⠠⣁⢌⡰⣈⠤⡐⠤⢒⡩⢎⣱⢎⢷⠻⣏⣽⣾⡷⠟⠛⠙⠳⣤⣀⠀⠀⠈⠙⠓⠦⠤⣤⣤⣤⣤⣤⣤⠴⠾⠛⠉⠀⠀⠀⠀⠀⢀⣠⠶⠋⠈⠙⠻⣿⣶⣭⣛⢮⡝⣳⡜⢦⣈⠐⡈⠄⠂⠅⡈⠄⢂⠡⢈⡐⠀⠐⠈⠄⠂⠀⠄⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣻⠗⣎⢧⢫⢏⢯⡳⡝⣮⢳⡞⡼⣲⢱⡎⣗⣫⠧⣝⢮⣵⣾⣯⣷⡟⠋⠁⠀⠀⠀⠀⠀⠀⠈⠛⠲⠤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠴⠚⠋⠀⠀⠀⠀⠀⠀⠀⠙⠳⣾⡳⣜⢧⡛⠷⣎⣳⡰⢌⡰⣀⠐⡀⠊⠄⠂⠠⠐⠈⠄⠂⢈⠐⠀⠠⠁⡘⢷⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⢭⡻⡜⢮⡝⣎⢧⡳⣝⢮⡳⢞⡵⣣⠟⣜⡲⢧⣻⣼⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣮⣝⢫⠶⡥⢏⡻⣴⢣⡗⣌⡲⡈⡔⢠⠁⢂⠈⡐⠀⠈⠌⠠⠁⠄⠠⠻⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣚⣥⢳⡹⣣⢞⡱⣎⢷⡹⢎⡳⡭⣖⣭⣾⣵⣿⠿⣟⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢾⣧⢻⣼⢫⡳⣭⢇⡿⣜⣳⠳⡼⣡⢮⣅⢳⣈⠳⣘⠒⡤⢣⠜⡰⢘⠻⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣹⢻⣿⣖⣮⣇⣗⣣⣯⣱⣏⣶⣹⣭⣷⡿⣟⡻⣝⢮⢷⣽⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣯⢿⣿⣿⣶⣏⡶⣹⠖⣯⣕⢫⡖⣮⢳⣭⢻⣱⢋⡶⢳⣺⢱⡏⣿⣿⣷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠐⠿⢺⣛⣿⡿⢿⣿⡿⠟⣿⠿⠛⣿⣿⢏⡷⣩⠷⣹⢮⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣾⣹⢿⣿⣿⣷⣯⡶⣭⡝⣮⠳⡭⣞⢭⡞⡭⣞⡱⣎⢯⢞⡱⢯⡽⣿⣆⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠟⢹⣇⡼⠋⠙⠶⠃⠀⢠⣿⣛⢮⡳⡝⣎⣷⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡞⣦⢳⣎⣟⡻⢷⣿⣶⣏⡗⣎⡳⢼⡱⢮⡕⡯⣞⠭⣞⢳⣼⣿⡿⣗
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⠀⠀⣿⣿⡸⢧⣛⠼⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⡲⢧⣚⡴⣙⢏⡶⣫⢟⡿⣷⡿⣿⣿⣷⣾⣷⣽⣾⣯⣿⣾⡿⣟⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⢧⣏⡳⢎⣻⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣇⡳⢎⡝⣮⢱⣏⠾⣜⣿⣧⠀⠀⠉⣇⢀⡟⠛⠻⢦⣹⡙⠻⠂
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⡾⣜⢧⣯⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣞⡵⣋⡞⠶⣍⢮⣻⣽⣿⣿⡄⠀⠀⠸⠟⠀⠀⠀⠀⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣯⢿⣹⢞⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣞⡵⣩⢟⡼⣣⢿⣾⣻⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⢯⡷⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡿⣼⣱⣞⣳⣯⣿⣟⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣧⢿⣳⣿⣯⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡤⢤⣀⠀⠀⠀⠀⠀⢀⣼⠃⠘⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⢿⣿⡿⣟⣿⣿⣿⣿⣿⡿⢷⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢘⡇⠀⠙⡷⣤⠶⠶⠲⣾⠁⠀⠀⠸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠈⢿⣿⣿⣿⣿⣿⣿⠋⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣼⣇⢄⣸⣅⣸⡇⠀⠀⠻⣄⣲⣲⣀⣼⡿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠘⣿⡉⠉⢉⡽⠁⠀⠀⣘⣿⡀⠀⠀⠀⠀⠀⣀⡀⠀⠀
⢠⣤⣄⣀⣰⡏⠀⠙⠶⠓⠋⠁⠀⠀⠀⠀⠈⠉⠉⠉⠁⠁⠘⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠿⣧⣀⡀⣀⣼⠇⠀⠀⠳⣤⡀⠠⢍⣿⠉⠳⣄⣠⡴⠛⢙⡇⠀⠀
⠈⣿⠀⠈⢿⡿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠈⠙⠛⠛⠁⠀⠀⣟⠁⠂⠀⣼⠀⠀⠀
⠀⢘⣷⣠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⣸⠋⠀⠀⠀
⠀⠀⢸⡏⠁⠀⠀⠀⣀⣤⠴⠶⠶⠶⠦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢻⡄⠀⠀⠀
⠀⠀⠸⡇⠀⠀⠀⣸⠋⠀⠀⠀⠀⠀⠠⠀⠉⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠈⢽⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀
⠀⠀⠀⢻⡆⠀⠀⣿⡆⠀⡀⠁⠀⠂⢀⠀⣂⡰⡌⣽⣦⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⠇⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠉⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀
⠀⠀⠀⠀⠹⡄⠀⢸⣧⢄⢠⡴⢰⡐⠦⣭⡵⡶⣽⢼⣻⣷⠀⠀⠀⠀⠀⠀⠈⢹⣿⣯⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⡆⠀⠀⠀⠀⠀⢀⣾⣿⢿⣈⠧⡐⠤⡄⣄⢠⠀⠀⠈⣷⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⡆⠀⢻⣾⣧⢳⣽⡍⢻⡔⢣⣿⣽⣯⣵⣿⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣾⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⣾⣯⡟⣶⢩⡞⣭⠛⣽⡞⣾⣷⣿⣧⣽⠂⠀⠀⠀⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢧⡈⠻⣿⡳⣦⢝⡣⣟⣽⣻⢾⡿⢷⣿⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡽⠿⠿⠛⠓⠶⢤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣶⣾⣿⣿⣿⣿⢿⣿⡿⣿⣿⡄⠀⠀⠀⢸⣿⣾⡝⢦⣋⡶⣍⢾⣱⢺⡕⣳⢚⣷⡿⠀⠀⢠⡾⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣬⡙⠳⢿⣴⣛⣾⣝⣺⣿⠟⠃⠀⠀⠀⠀⣀⡶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠓⠲⠤⣤⣤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⠴⠶⠒⠛⠛⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡿⢷⣄⠀⠀⠈⢿⣿⣭⢛⡜⡳⣍⠞⡷⢻⡼⣱⣿⠟⠀⠀⣰⠞⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⢤⣌⣁⣈⢀⣀⣀⣀⣀⣠⡴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠙⠷⣿⣼⣳⣌⣿⣼⡿⠟⠋⠁⣀⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠦⣄⣀⡀⠀⠀⠉⠉⣉⣁⣀⡤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠙⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\
"""
eeve_string ="""\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣾⣷⣾⣿⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⢹⣧
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠋⠀⢸⣿
⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠁⠀⠀⢸⣿
⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⠁⠀⠀⠀⣿⣿
⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⢤⣬⣥⣾⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠁⠀⠀⠀⢰⣿⡏
⣸⣿⣿⣿⣿⣿⣿⡟⠛⠻⠿⠿⠿⠿⣿⡿⠇⢨⣍⣙⣛⣠⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡏⠀⠀⠀⢀⣾⣿⠁
⣿⣿⣿⣿⣿⣿⣿⣧⡘⢶⣶⣶⣶⣶⣶⣤⣤⣤⣤⣭⣉⣉⣉⣛⠛⠿⠿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⢀⣠⣴⣦⣤⣶⣶⣿⣿⣧⣤⣤⣄⠉⢻⡇⠀⠀⠀⣼⣿⡏⠀
⣿⣿⣿⣿⣿⣿⠿⣿⣿⣄⠙⢿⣿⣄⠀⠀⠀⠀⠈⠉⠙⠛⠻⠿⣿⣿⣶⣤⡉⠻⣿⣿⣿⡆⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣥⣤⣭⣁⣀⠀⣸⣿⡟⠀⠀
⢻⣿⣿⣿⣿⣿⡄⢬⣙⠻⢰⣤⡙⠻⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣷⣌⠻⢿⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣍⡁⠿⠋⠀⠀⠀
⠸⣿⡏⣉⡻⢿⣿⡜⣿⣿⣿⣿⣿⣶⣄⡙⠻⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣷⣄⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣛⣛⠛⠂⠀⠀⠀⠀
⠀⢻⡇⣿⣿⣶⣬⣙⠈⢿⣿⣿⣿⣿⣿⣿⣶⣌⡙⠻⢿⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
⠀⠈⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣈⠙⠻⢿⣿⣶⣦⣄⣀⣀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠗⢀⣀⣉⠙⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣉⠻⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⣠⣾⣿⣿⠟⣁⣤⣴⣶⣶⢸⣿⣿⣿⣿⣿⣿⣿⢟⣛⠻⣿⣿⣿⣿⣿⣿⣿⣿⠁⣿⠇⠸⣿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⢿⣿⣿⣿⣿⡿⠃⣴⣿⣿⣿⠟⣡⣾⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⢣⣿⣿⠀⠘⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⢀⣾⣿⣿⣿⠏⣼⡿⢟⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⠘⠛⠋⠀⠀⢹⣿⣿⣿⣿⣿⣿⣇⠠⠤⢃⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣀⡅⣠⣿⣿⣿⣿⣿⣿⣇⢹⣿⣿⣿⣿⣿⠰⣷⣀⣠⡄⣸⣿⣿⣿⣿⣿⠿⢻⣷⣶⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⢡⣿⣿⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣷⣬⣉⣉⣴⣿⣿⣿⣿⣿⣿⣿⠿⢟⣿⣿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⢸⡇⣿⣿⣿⣿⣿⡿⢹⣿⣦⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣋⣭⣶⣾⡿⢟⣡⣾⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣇⢈⣥⢸⣿⣿⣿⣿⡇⣾⣿⣿⣿⣶⣬⣙⠻⠿⣿⣿⣿⣿⣿⣿⠿⠿⢛⣉⣥⣶⣿⡿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⡿⠈⢿⣿⣿⣿⡀⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣤⣤⣴⣶⣾⣿⣿⢿⣿⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⠡⣿⣌⢻⣿⣿⣧⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠇⠀⢿⣿⣷⡙⠛⣿⡇⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⠀⠀⠈⢿⣿⣿⣶⠈⣰⣷⣬⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠈⠉⠋⢠⣿⣿⣿⣿⣮⡛⢿⠏⠻⢿⣿⣿⣿⣿⢟⣴⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⢿⠆⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⢉⡛⠟⣱⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⠀⠀⠀⠀⠈⣿⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⢹⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠉⠛⠋⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⡟⢿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\
"""
charmander_string ="""\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠉⠀⠀⠀⠀⠀⠈⠑⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⣠⣄⠀⠈⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⠁⠀⠀⠀⠀⠀⠀⡸⢛⣷⡀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡿⠋⠀⠀⠀⠀⠀⠀⢰⣷⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠿⢏⡏⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠋⠁⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⣦⡀⠐⠂⠠⠴⠀⠀⠀⠀⠀⠀⠀⣀⡴⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢀⠀⠀⠀
⠀⢰⠦⣄⠈⢿⣶⡶⠤⠤⠤⠔⠒⠒⣶⠒⡫⢋⡄⠀⢸⠀⠀⠀⠀⢀⣀⠤⣤⠀⠀⠀⠀⠀⢀⡞⠉⠛⢆⠀⠀
⢰⡟⢷⠂⠉⠚⠿⣿⣄⣀⣀⣀⣠⣴⣛⣯⠔⠋⠀⠠⠼⠦⠔⠒⠊⠁⠠⡶⢧⡄⠀⠀⠀⠀⠸⣧⠀⡀⠈⣿⠀
⠀⠙⢮⡀⠀⠀⠀⠈⠉⡖⠛⠋⠉⠉⠁⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣥⠞⠁⠀⠀⠀⠀⠀⡏⠿⢧⢀⠈⡆
⠀⠀⠀⠙⢄⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⣇⠀⠸⣯⠀⡿
⠀⠀⠀⠀⠀⠓⢄⣠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠐⠒⢖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠉⣶⡇
⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠈⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣴⢦⠞⠁
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⢸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⣀⠜⠁⢀⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠚⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠤⠤⢤⣸⠓⠢⠄⢀⠀⠤⠔⠊⠁⠀⠀⡼⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠈⠑⠦⣀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢳⡄⠀⠀⠀⠀⠀⢀⡜⠉⠉⠛⢧⠀⠀⠀⠀⠀⠀⣸⠥⣄⣀⣀⣀⠠⠖⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⢸⠇⠀⠀⠀⢀⣴⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣿⣷⣦⣀⣀⣀⡀⠤⠤⠤⠚⠁⠀⠀⠀⢸⡤⢤⡤⢤⡴⢤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠾⡷⠞⠿⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\
"""
squirtle_string= """\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⠤⠤⠤⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠢⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠀⠀⢀⣀⡐⢄⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⡜⠁⠀⣿⡌⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⣸⣷⣤⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠊⣼⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢤⡀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⡜⣼⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⠉⠲⣄⣀⣼⡇⠀⠀⠀⠀⠀⠀⠻⠿⣿⣟⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⠉⠁⠀⡏⠑⠌⠓⢬⣧⠀⠀⠀⠀⠘⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠇⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠈⠉⠓⠒⠲⠤⢤⣀⠀⠂⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⢀⣠⠤⠖⠒⠒⠒⠦⢤⡀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⠤⠤⠒⠋⢉⠟⠀⠀⠀⠀
⠀⠀⢀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⢠⡞⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠋⠀⠀⠀⠀⠀
⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢇⠀⢠⡟⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠈⠑⠢⢤⣀⣀⠀⠀⠀⠀⢀⣀⡤⠖⠯⣀⠀⠀⠀⠀⠀⠀
⢀⡟⠀⠀⠀⠀⠠⠴⠤⣀⠀⠀⠀⠀⠀⢸⣠⡟⠀⠀⠀⠀⢹⣄⠀⠀⠀⠀⠀⠀⢀⣼⡁⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⢻⠀⠀⠀⠀⠀⠉⠢⣄⣀⡀⠀
⢸⡇⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⢈⣿⡇⠀⠀⠀⠀⢸⠉⢢⣀⡀⢀⣀⣴⠟⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⢇⡀
⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⢸⡇⣷⠀⠀⠀⢀⡞⠀⢰⠏⠉⠉⠁⢸⡀⠀⠀⠀⠈⠓⠶⠤⣤⣄⣀⣠⡤⠴⡇⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁
⠀⠹⣆⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⢸⠁⠸⡆⠀⣠⠞⠀⢀⡞⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⢰⣧⣀⣀⡀⠀⢀⣀⣠⠴⠃⠀
⠀⠀⠹⡓⠦⠤⠤⠖⠋⠀⠀⠀⠀⠀⠀⢸⠀⠀⠹⡴⠁⠀⢠⠞⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⣸⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢸⢁⡠⠴⢧⡀⠀⠀⠀⠀⣀⠔⠳⣄⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⣠⡿⠋⠀⠀⠀⠙⢦⣀⡠⠞⠁⠀⠀⠈⠙⠶⣤⣀⡀⣰⠃⠀⠀⣠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⠀⠀⠀⠈⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣹⠋⠉⠉⣹⠏⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠲⢤⣄⣀⣠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⢀⣤⠞⠁⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠶⠤⠤⠤⠤⠤⢤⣞⡥⠖⠋⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⠒⠀⠀⠒⠒⠺⢯⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⢄⣈⠆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢄⡀⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣄⠀⠀⠀⠀⢀⣠⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⣀⡤⠖⢄⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠒⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠈⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\
"""
victory = """\
                                                                  
____   ___.______________________________ _______________.___._._.      
\   \ /   |   \_   ___ \__    ___\_____  \|______   \__  |   | | |      
 \   Y   /|   /    \  \/ |    |   /   |   \|       _//   |   | | |      
  \     / |   \     \____|    |  /    |    |    |   \|____   |\|\|      
   \___/  |___|\______  /|____|  \_______  |____|_  // ______|____      
                      \/                 \/       \/ \/       \/\/      
                                                                        \
"""
defeat = """\
                                                                        
__________.__                    _____                .__     _________
\______   \  | _____  ___.__.   /  _  \    _________  |__| ___\_____   |
 |     ___/  | \__  \<   |  |  /  /_\  \  / ___\__  \ |  |/    \ /   __/
 |    |   |  |__/ __ \|___  | /    |    \/ /_/  > __ \|  |   |  \   |
 |____|   |____(____  / ____| \____|__  /\___  (____  /__|___|  /___|
                    \/\/              \//_____/     \/        \/<___>   
                                                                        \
"""




def effectiveness(tipo_ataque, tipo_defensor):
    efectividades = {
        'fuego':     {'fuego': 0.5, 'agua': 0.5, 'planta': 2,   'electrico': 1, 'hielo': 2,   'roca': 0.5, 'bicho': 2,   'tierra': 1, 'dragon': 0.5, 'acero': 2},
        'agua':      {'fuego': 2,   'agua': 0.5, 'planta': 0.5, 'electrico': 1, 'roca': 2,   'tierra': 2, 'dragon': 0.5},
        'planta':    {'fuego': 0.5, 'agua': 2,   'planta': 0.5, 'roca': 2,      'tierra': 2, 'bicho': 0.5, 'dragon': 0.5, 'veneno': 0.5},
        'electrico': {'agua': 2,    'planta': 0.5, 'tierra': 0, 'volador': 2,   'dragon': 0.5},

    }

    tipo_ataque = tipo_ataque.lower()
    tipo_defensor = tipo_defensor.lower()

    # Si no existe el tipo, devolver 1 (neutro)
    return efectividades.get(tipo_ataque, {}).get(tipo_defensor, 1.0)

def slow_print(texto):
    delay = 0.05
    for c in texto:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

#class pokemon
class Pokemon:
    def __init__(self, nombre, vida, tipo, ataque_1, ataque_2, splash_art):
        self.nombre = nombre
        self.vida_max = vida
        self.vida = vida
        self.tipo = tipo
        self.ataque_1 = ataque_1
        self.ataque_1_cantidad = 10
        self.ataque_2 = ataque_2
        self.ataque_2_cantidad = 15
        self.splash_art = splash_art
    def descansar(self, cantidad):
        self.vida += cantidad
    def atacar_1(self, pokemon):
        efectividad = effectiveness(self.tipo, pokemon.tipo)
        pokemon.vida -= self.ataque_1_cantidad * efectividad
        slow_print(f"{self.nombre} " + "ataca con " + f"{self.ataque_1} ")
        if pokemon.vida < 0:
            pokemon.vida = 0
        if efectividad == 2:
            slow_print("El ataque es muy efectivo")
        elif efectividad == 1:
            slow_print("El ataque es efectivo")
        else:
            slow_print("No es muy efectivo...")
        return 0


    def atacar_2(self, pokemon):
        if self.nombre == "Snorlax":
            self.vida += 20
            if self.vida >= self.vida_max:
                self.vida = self.vida_max
            slow_print("Zzz...\n"
                  "Snorlax se ha dormido")
            return 0
        slow_print(f"{self.nombre} " + "ataca con " + f"{self.ataque_2}")
        efectividad = effectiveness(self.tipo, pokemon.tipo)
        pokemon.vida -= self.ataque_2_cantidad * efectividad
        if pokemon.vida < 0:
            pokemon.vida = 0
        if efectividad == 2:
            slow_print("El ataque es muy efectivo")
        elif efectividad == 1:
            slow_print("El ataque es efectivo")
        else:
            slow_print("No es muy efectivo...")
        return  0
    def instakill(self, pokemon):
        pokemon.vida = 0



#lista de pokemones
pikachu = Pokemon("Pikachu", 100, "electrico", "Bola voltio", "Impactrueno", pikachu_string)
charmander = Pokemon("Charmander",100,'fuego',"Ascuas", "Lanzallamas", charmander_string)
eeve = Pokemon("Eeve", 90, "normal", "Mordisco", "Placaje", eeve_string)
snorlax = Pokemon("Snorlax", 150, "normal", "Bostezo", "Descanso", snorlax_string )
squirtle = Pokemon("Squirtle", 100, "agua", "Pistola agua", "Burbuja", squirtle_string )


os.system("cls")
def iniciar_combate(propio, enemigo):
    from random import randint
    import os
    os.system("cls")
    #interfaz vida
    TAMANIO_BARRA_VIDA = 25

    while propio.vida > 0 and enemigo.vida > 0:
        # Pim-pam combate
        user_input = None

        # Turno de propio
        print_string(propio.splash_art)
        slow_print(f"Es el turno de {propio.nombre}")

        while user_input != "1" and user_input != "2" and user_input != "99" and user_input != "X":
            slow_print(f"Que ataque deseas realizar?:\n"
                  f" 1: {propio.ataque_1}\n"
                  f" 2: {propio.ataque_2}\n")
            user_input = input()
            if user_input == "1":
                propio.atacar_1(enemigo)
            elif user_input == "2":
                propio.atacar_2(enemigo)
            elif user_input == "99":
                propio.instakill(enemigo)




        barra_de_vida_propio = int(propio.vida * TAMANIO_BARRA_VIDA // propio.vida_max)
        slow_print(f"{propio.nombre}:  " + "    [{}{}] ({}/{})".format("#" * barra_de_vida_propio,
                                                  " " * (TAMANIO_BARRA_VIDA - barra_de_vida_propio),
                                                                       propio.vida, propio.vida_max))

        barra_de_vida_enemigo = int(enemigo.vida * TAMANIO_BARRA_VIDA / enemigo.vida_max)
        slow_print(f"{enemigo.nombre}: " + "    [{}{}] ({}/{})".format("#" * barra_de_vida_enemigo,
                                                   " " * (TAMANIO_BARRA_VIDA - barra_de_vida_enemigo),
                                                                       enemigo.vida, enemigo.vida_max))



        if enemigo.vida == 0:
            slow_print(f"{propio.nombre} gana!")
            print_string(victory)
            input("Presiona enter para continuar...")
            return 0
        elif propio.vida == 0:
            slow_print(f"{enemigo.nombre} gana!")
            print_string(defeat)
            input("Presiona enter para continuar...")


        os.system("cls")

        # Turno Squirtle
        print_string(enemigo.splash_art)
        slow_print(f"Es el turno de {enemigo.nombre}")
        ataque = randint(1, 2)
        if ataque == 1:
            enemigo.atacar_1(propio)
        elif ataque == 2:
            enemigo.atacar_2(propio)



        barra_de_vida_propio = int(propio.vida * TAMANIO_BARRA_VIDA // propio.vida_max)
        slow_print(f"{propio.nombre}:  " + "    [{}{}] ({}/{})".format("#" * barra_de_vida_propio,
                                                                  " " * (TAMANIO_BARRA_VIDA - barra_de_vida_propio),
                                                                       propio.vida, propio.vida_max))

        barra_de_vida_enemigo = int(enemigo.vida * TAMANIO_BARRA_VIDA // enemigo.vida_max)
        slow_print(f"{enemigo.nombre}: " + "    [{}{}] ({}/{})".format("#" * barra_de_vida_enemigo,
                                                                  " " * (TAMANIO_BARRA_VIDA - barra_de_vida_enemigo),
                                                                       enemigo.vida, enemigo.vida_max))


        input("Presiona enter para continuar...")

        os.system("cls")



        if enemigo.vida == 0:
            slow_print(f"{propio.nombre} gana!")
            print_string(victory)
            input("Presiona enter para continuar...")
        elif propio.vida == 0:
            slow_print(f"{enemigo.nombre} gana!")
            print_string(defeat)
            input("Presiona enter para continuar...")



new_position = None
my_position = [34, 0]
POS_X = 0
POS_Y = 1
main_character = "@"


#Draw map


upper_and_bottom_limit = "═"
wall = "▓"
upper_left_corner = "╔"
upper_right_corner = "╗"
bottom_left_corner = "╚"
bottom_right_corner = "╝"
side_walls = "║"
obstacles_definition = """\
4                    ▓▓▓▓▓▓▓▓          
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓          
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓          
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓          
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓          
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓          
                     ▓▓▓▓▓▓▓▓          
   3                 ▓▓▓▓▓▓▓▓          
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     1    
        ▓▓▓▓▓▓▓▓                       
        ▓▓▓▓▓▓▓▓                       
        ▓▓▓▓▓▓▓▓        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        ▓▓▓▓▓▓▓▓        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                                      2\
""" #map string

obstacles_definition = [list(row) for row in obstacles_definition.split("\n")]
MAP_WIDTH = len(obstacles_definition[0])
MAP_HEIGHT = len(obstacles_definition)


wins=[]
while len(wins) < 4:
    #top
    print(upper_left_corner,end="")
    print(upper_and_bottom_limit * MAP_WIDTH,end="")
    print(upper_right_corner)

    #playable coordinates
    for coordinate_y in range (MAP_HEIGHT):
        print(side_walls, end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = obstacles_definition[coordinate_y][coordinate_x]

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = main_character

            print("{}".format(char_to_draw), end="")

        print (side_walls)

    #bottom
    print(bottom_left_corner,end="")
    print(upper_and_bottom_limit * MAP_WIDTH,end="")
    print(bottom_right_corner)

    #Movement
    user_input = readchar.readkey().lower()



    if user_input == "w":
        if my_position [POS_Y] > 0:
            new_position = [my_position[POS_X], my_position[POS_Y] - 1]

    elif user_input == "a":
        if my_position[POS_X] > 0:
            new_position = [my_position[POS_X] - 1, my_position[POS_Y]]


    elif user_input == "d":
        if my_position [POS_X] < 38:
            new_position = [my_position[POS_X] + 1, my_position[POS_Y]]

    elif user_input == "s":
        if my_position[POS_Y] < 14:
            new_position = [my_position[POS_X], my_position[POS_Y] + 1]

    elif user_input == "q":
        break

    if new_position: #If new_position is != None it will update the value for my_position.
        if obstacles_definition[new_position[1]][new_position[0]] == " ": #Player can only move if there is blank spaces
            my_position = new_position


    os.system("cls")

    #entrenadores hardcodeados
    if 33 <= my_position[POS_X] <= 35 and 7 <= my_position[POS_Y] <= 9: #entrenador 1
        print("Presiona [E] para iniciar el combate")
        if user_input == "e":
            iniciar_combate(pikachu,eeve)
            obstacles_definition[8][34] = " "
            wins.append(1)

    if my_position[POS_X] == 37 and my_position[POS_Y] == 14:#entrenador 2

        print("Presiona [E] para iniciar el combate")
        if user_input == "e":
            iniciar_combate(pikachu,charmander)
            obstacles_definition[14][38] = " "
            wins.append(2)

    if 2 <= my_position[POS_X] <= 4 and 6<= my_position[POS_Y]<=8: #entrenador 3
        print("Presiona [E] para iniciar el combate")
        if user_input == "e":
            iniciar_combate(pikachu,squirtle)
            obstacles_definition[7][3] = " "
            wins.append(3)

    if  my_position[POS_X] == 1 and my_position[POS_Y] == 0: #entrenador 4
        print("Presiona [E] para iniciar el combate")
        if user_input == "e":
            iniciar_combate(pikachu,snorlax)
            obstacles_definition[0][0] = " "
            wins.append(4)





os.system("cls")
print("Felicitaciones, has terminado el juego")


