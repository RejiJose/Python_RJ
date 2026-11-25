# import game library
from gamelib import *

# create game variable: dimensions(w x h) and title
game = Game( 800, 600, "Zombie Thanksgiving" )

# create background image & resize to canvas dimensions
bk = Image("Zbk.jpg",game)
bk.resizeTo( 800, 600 )

# create zombie image, resize(%) & set speed values
zombie = Image("zombie.png", game)
zombie.resizeBy(-85)


# create turkey image, resize(%) & set speed values
turkey = Image("turkey.gif", game)
turkey.resizeBy(-50)


# create crosshair image, resize(%) & draw
crosshair = Image("crosshair.png", game)
crosshair.resizeBy(-70)


# game loop

    # process inputs
    
    # draw background & crosshair
    
    # move zombie & turkey. Ensure bounce
    

    # update game
    
    # end of game loop

# quit game


'''
Lesson 3 Topics:
    Make image move at a specified rate & direction: move( ), setSpeed(.. , ..)
    Make image bounce off screen edges: move(True)
    Game loop: while not game.over
    Process inputs
    game update (fps)
    quit the game
'''




