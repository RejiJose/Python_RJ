# bring in the game library
from gamelib import *

# create a variable, game, with game window dimensions(w x h) and title
game = Game( 800, 600, "Zombie Thanksgiving" )

# create a variable, bk for background image, resize & draw it
bk = Image("Zbk.jpg",game)
bk.resizeTo( 800, 600 )
bk.draw()

# draw zombie image, resize & draw it
zombie = Image("zombie.png", game)
zombie.resizeBy(-80)
zombie.draw()

# draw turkey image, resize & draw it


# draw crosshair image, resize & draw it


# update game
game.update()
