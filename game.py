''' 

    E Y E B L I N K

    A text adventure written by Miguel Reinoso (miguelreinoso7@gmail.com)

    August 2019

'''

# ============================== THINGS THAT I'M TESTING ====================================

# This will print the output in a more cinematic way

'''
import sys

BAUD = 1200

def baudout(s):
    for c in s:
        sleep(9. / BAUD)  # 8 bits + 1 stop bit @ the given baud rate
        sys.stdout.write(c)
        sys.stdout.flush()

baudout()
'''
 
from time import sleep
from player import Player
import world, pygame

# ========================================== Functions ========================================
         
def three_blank_lines(): # Spaces between paragraphs
    print()
    print()
    print()

def shpause(): # short pause in the narrative
    sleep(1)

def lpause(): # long pause in the narrative
    sleep(2)

def get_player_command(): # Player prompt
    print()
    return input("What now? ")

def play(): # Game loop
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        action_input = get_player_command()
        if action_input == 'n':
            player.move_north()
        elif action_input == 's':
            player.move_south()
        elif action_input == 'e':
            player.move_east()
        elif action_input == 'w':
            player.move_west()
        elif action_input == 'i':
            player.print_inventory()
        elif action_input == 'a':
            player.attack()
        elif action_input == 'h':
        	player.heal()
        elif action_input == 'music off':
            pygame.mixer.music.stop()
        elif action_input == 'music on':
            pygame.mixer.music.play(-1, 0.2)
        else:
            print("Invalid action")        
                         
                
            
        

# ==================================== NARRATIVE ================================================

pygame.init() # music
pygame.mixer.music.load('Kai_Engel-Interception.mp3')
pygame.mixer.music.play(-1, 0.2)

three_blank_lines()

print("     #######    #     #    #######    ######     #          ###    #     #    #    # ")
print("     #           #   #     #          #     #    #           #     ##    #    #   #  ")
print("     #            # #      #          #     #    #           #     # #   #    #  #   ")
print("     #####         #       #####      ######     #           #     #  #  #    ###    ")
print("     #             #       #          #     #    #           #     #   # #    #  #   ")
print("     #             #       #          #     #    #           #     #    ##    #   #  ")
print("     #######       #       #######    ######     #######    ###    #     #    #    # ")

three_blank_lines()

shpause()

print("""
                                 Synopsis: 

It's the year 2050. After the climate breakdown, life on the surface of the planet
became impossible ... Humans and cyborgs started to live in subterranean megacities where 
everyone struggles to survive. 
""")

lpause()

print("""
In this wicked world, you're a little girl called Valeria. You survive collecting and selling
junk, hacking machines and stealing Qtrits, the cryptocurrency that wealthy people uses in
the underground.  
""")

lpause()

print("""
One night you're coming back to your cabin to get some rest and you find a strange woman
waiting at the door of your block. She asks you for an adress. You try to run without
answering nothing but it's too late. A protocol droid appears from the shadows and grabs
you while the woman forces you to inhale some kind of substance ...
""")

lpause()

print("""
You fall asleep ... 
""")

three_blank_lines()

lpause()

print('''
              Instructions:

- Play with your keyboard. Enter commands in lower case.
- Available commands are:

'n' North    'i' Inventory    'music on'  
's' South    'a' Attack       'music off'
'e' East     'h' Heal
'w' West

Music:'Interception' by Kai Engel.
''')

three_blank_lines()

shpause()

print("""
You awake ... 
After opening your eyes you find yourself in an empty room.
""")

play()

