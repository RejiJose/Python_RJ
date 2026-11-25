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
zombie.setSpeed(2,60)

# create turkey image, resize(%) & set speed values
turkey = Image("turkey.gif", game)
turkey.resizeBy(-50)
turkey.setSpeed(3,-45)

# create crosshair image, resize(%) & draw
crosshair = Image("crosshair.png", game)
crosshair.resizeBy(-70)


# game loop
while not game.over:
    # process inputs
    game.processInput()
    # draw background & crosshair
    bk.draw()
    crosshair.draw()
    # move zombie & turkey. Ensure bounce
    zombie.move(True)
    turkey.move(True)

    # update game
    game.update(30)
    # end of game loop

# quit game
game.quit()

'''
Lesson 3 Topics:
    Make image move at a specified rate & direction: move( ), setSpeed(.. , ..)
    Make image bounce off screen edges: move(True)
    Game loop: while not game.over
    Process inputs
    game update (fps)
    quit the game
'''