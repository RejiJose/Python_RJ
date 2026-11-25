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
# start zombie at random location

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

    # make crosshair follow mouse position

    # update game
    game.update(30)
    # end of game loop

# quit game
game.quit()

'''
Lesson 4 Topics:
    Move object to given location: moveTo(x, y)
    Get coordinates of mouse object
    Make crosshair image follow mouse position
    Start zombie at random location
'''



