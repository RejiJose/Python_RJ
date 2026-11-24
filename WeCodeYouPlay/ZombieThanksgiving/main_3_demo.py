# bring in the game library
from gamelib import *

# create a variable, game, with game window dimensions(w x h) and title
game = Game( 800, 600, "Zombie Thanksgiving" )

# create a variable, bk for background image, resize & draw it
bk = Image("Zbk.jpg",game)
bk.resizeTo( 800, 600 )
bk.draw()

# create zombie image, resize & draw it
zombie = Image("zombie.png", game)
zombie.resizeBy(-80)
zombie.draw()

# create turkey image, resize & draw it
turkey = Image("turkey.gif", game)
turkey.resizeBy(-50)
turkey.draw()

# create crosshair image, resize & draw it
crosshair = Image("crosshair.png", game)
crosshair.resizeBy(-70)
crosshair.draw()


# update game
game.update()

'''
Lesson 3 Topics:
    
'''