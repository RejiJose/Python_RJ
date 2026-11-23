from microbit import *
from random import randint
import audio

hx = 2
hy = 2

ex = randint(0,4)
ey = 0

#Start Screen
gameover = False
while not gameover:
    display.scroll("Catch Em!")
    
    if button_a.was_pressed() or button_b.was_pressed():
        audio.play(Sound.TWINKLE)
        gameover = True
    
    sleep(100)

gameover = False
t = 0
damage = 0

while not gameover:
    display.clear()
    display.set_pixel(hx,hy,9)
    display.set_pixel(ex,ey,9 - damage)
    
    if accelerometer.get_x() > 400 and hx < 4:
        hx += 1
    elif accelerometer.get_x() < -400 and hx > 0:
        hx -= 1

    if accelerometer.get_y() > 400 and hy < 4:
        hy += 1
    elif accelerometer.get_y() < -400 and hy > 0:
        hy -= 1

    if ex == hx and ey == hy:
        audio.play(Sound.SAD, wait=False)
        damage += 1
        ey = randint(0,4)
        ex = randint(0,4)

    if damage == 5 or t > 100:
        gameover = True
        
    t+=1
    sleep(100)

if damage == 5:
    display.show(Image.HAPPY)
else:
    display.show(Image.SAD)