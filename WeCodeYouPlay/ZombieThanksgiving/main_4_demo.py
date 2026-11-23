# bring in the game library
from gamelib import *

# create a variable, game, with game window dimensions(w x h) and title
game = Game( 800, 600, "Zombie Thanksgiving" )

# create a variable, bk for background image, resize
bk = Image("Zbk.jpg",game)
bk.resizeTo( 800, 600 )

# draw zombie image, resize & set speed
zombie = Image("zombie.png", game)
zombie.resizeBy(-85)
# set zombie speed
zombie.setSpeed(2,60)

# draw turkey image, resize & set speed
turkey = Image("turkey.gif", game)
turkey.resizeBy(-50)
# set turkey speed
turkey.setSpeed(3,-45)

# draw crosshair image, resize & draw it
crosshair = Image("crosshair.png", game)
crosshair.resizeBy(-70)
crosshair.draw()

# game loop
while not game.over:
    # process inputs
    game.processInput()
    # draw background
    bk.draw()
    # move zombie & turkey
    zombie.move(True)
    turkey.move(True)

    # update game
    game.update(30)
    # end of game loop

# quit game
game.quit()




