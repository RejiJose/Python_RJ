# link game library to main
from gamelib import *

# create game variable with window dimensions(w x h) and game title
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