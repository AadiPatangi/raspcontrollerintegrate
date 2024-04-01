#import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event9')

#button code variables (change to suit your device)


up = 307
down = 304
left = 308
right = 305

rfront = 311
lfront = 310

lTrig = 312
rTrig = 313

#prints out device info at start
print(gamepad)

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
          

            if event.code == up:
                print("up")
            elif event.code == down:
                print("down")
            elif event.code == left:
                print("left")
            elif event.code == right:
                print("right")

            elif event.code == rfront:
                print("start")
            elif event.code == lfront:
                print("select")

            elif event.code == lTrig:
                print("left bumper")
            elif event.code == rTrig:
                print("right bumper")