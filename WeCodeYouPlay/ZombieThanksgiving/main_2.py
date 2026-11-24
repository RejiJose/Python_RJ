# bring in the game library
from gamelib import *

# create a variable, game, with game window dimensions(w x h) and title
game = Game( 800, 600, "Zombie Thanksgiving" )

# create a variable, bk for background image
bk = Image("Zbk.jpg",game)
# resize bk image
bk.resizeTo( 800, 600 )
# draw background
bk.draw()
# create zombie image, resize & draw it
zombie = Image("zombie.png", game)
zombie.resizeBy(-80)
zombie.draw()

# update game
game.update()