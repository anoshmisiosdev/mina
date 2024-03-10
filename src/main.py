#region VEXcode Generated Robot Configuration
from vex import *


# Brain should be defined by default
brain=Brain()


# Robot configuration code




# wait for rotation sensor to fully initialize
wait(30, MSEC)




def play_vexcode_sound(sound_name):
   # Helper to make playing sounds from the V5 in VEXcode easier and
   # keeps the code cleaner by making it clear what is happening.
   print("VEXPlaySound:" + sound_name)
   wait(5, MSEC)


# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")


#endregion VEXcode Generated Robot Configuration


# ------------------------------------------
#
#   Project:
#   Author:
#   Created:
#   Configuration:
#
# -----------------------------------------

# Library imports
from vex import *


# Begin project code


def pre_autonomous():
   # actions to do when the program starts
   brain.screen.clear_screen()
   brain.screen.print("pre auton code")
   left_piston.set(1)
   right_piston.set(1)
controller = Controller()
vision_6__BRIE = Signature(1, -5735, 1, -2866,-7343, -3633, -5488,1.1, 0)
motor1 = Motor(Ports.PORT1, False)  # Front left, direction reversed
motor2 = Motor(Ports.PORT2, True)  # Front right
motor3 = Motor(Ports.PORT3, False) # Back left, direction reversed
motor4 = Motor(Ports.PORT4, True) # Back right
motor6 = Motor(Ports.PORT5, False)#mid left wheel
motor7 = Motor(Ports.PORT6, True)#mid right wheel
motor1.set_velocity(200, PERCENT)
motor2.set_velocity(200, PERCENT)
motor3.set_velocity(200, PERCENT)
motor4.set_velocity(200, PERCENT)
vision = Vision(Ports.PORT7, 50, vision_6__BRIE)
left_piston = DigitalOut(brain.three_wire_port.a)  # Adjust port as necessary
right_piston = DigitalOut(brain.three_wire_port.b)
   








wait(1, SECONDS)


def autonomous():
   brain.screen.clear_screen()
   brain.screen.print("autonomous code")
   # place automonous code here
   motor1.spin_for(FORWARD, 1036*2,DEGREES,wait=False)
   motor2.spin_for(FORWARD, 1036*2,DEGREES,wait=False)
   motor3.spin_for(FORWARD, 1036*2,DEGREES,wait=False)
   motor4.spin_for(FORWARD, 1036*2,DEGREES,wait=False)
   time.sleep(1)


   # part 2
   x = 0
   for x in range(16):
       # make sure that the 2nd block runs AFTER the first block
       dataset = vision.take_snapshot(1)
       if dataset is None:
           motor1.spin(FORWARD, 25, PERCENT)
           motor2.spin(REVERSE, 25, PERCENT)
           motor3.spin(FORWARD, 25, PERCENT)
           motor4.spin(REVERSE, 25, PERCENT)
           time.sleep(0.5)
           motor1.stop()
           motor2.stop()
           motor3.stop()
           motor4.stop()
           continue
          
       elif(vision.largest_object().centerX < 200 and vision.largest_object().centerX > 100):
           brain.screen.print(vision.largest_object().centerX)
           brain.screen.next_row()
           motor1.spin(FORWARD, 50, PERCENT)
           motor2.spin(FORWARD, 50, PERCENT)
           motor3.spin(FORWARD, 50, PERCENT)
           motor4.spin(FORWARD, 50, PERCENT)
       x+=1
       wait(1, SECONDS)


def user_control():
    brain.screen.clear_screen()
    # place driver control in this while loop
    left_piston.set(1)
    right_piston.set(1)
    while True:
        wait(20, MSEC)
        buttonmode = controller.buttonA.pressing()
        rpipestatemode = right_piston.value()
        lpipestatemode = left_piston.value()
        lbutton = controller.buttonB.pressing()
        # Reading joystick positions
        forward_backward = -1*(controller.axis1.position())  # Forward/Backward from the left joystick
        turn = controller.axis3.position()  # Turning from the right joystick
            # Apply a deadzone for precision control
        if abs(forward_backward) < 5:
            forward_backward = 0
        if abs(turn) < 5:
            turn = 0
            # Forward/backward movement speed calculation
        if forward_backward != 0:
            speed = (forward_backward / 127.0) ** 3 * 1000  # Cubic scaling for smooth acceleration
        else:
            speed = 0
            # Calculate turning effect
        turning_effect = (turn / 127.0) ** 3 * 1000  # Cubic scaling for smooth turning
            # Calculate final speed for each motor
        speed_left = speed - turning_effect
        speed_right = speed + turning_effect


            # Set motor speeds, considering the reversed directions
        motor1.spin(FORWARD, -speed_left, PERCENT)  # Reversed
        motor2.spin(FORWARD, speed_right, PERCENT)
        motor3.spin(FORWARD, -speed_left, PERCENT)  # Reversed
        motor4.spin(FORWARD, speed_right, PERCENT)
        if controller.buttonL2.pressing():
            motor6.spin(FORWARD, speed_right*200, PERCENT)
            motor7.spin(FORWARD, -speed_left*200,PERCENT)
                # Read the current state of the buttons
        # Read the current state of the button
        if lbutton == 1 or lbutton == True:
            if lpipestatemode == 0:
                left_piston.set(1)
                wait(500, MSEC)
            elif lpipestatemode == 1:
                left_piston.set(0)
                wait(500, MSEC)
        if buttonmode == True or buttonmode == 1:
            if rpipestatemode == 0:
                right_piston.set(1)
                wait(500, MSEC)
            elif rpipestatemode == 1:
                right_piston.set(0)
                wait(500, MSEC)


          










   # Small delay to prevent overwhelming the CPU
        wait(5, MSEC)
   #control_pistons()
   # Delay to prevent overwhelming the CPU
   # Check if the button is pressed


# create competition instance
comp = Competition(user_control, autonomous)
pre_autonomous()





