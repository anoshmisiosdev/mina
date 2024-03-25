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

brain=Brain()
def pre_autonomous():
   # actions to do when the program starts
   brain.screen.clear_screen()
   brain.screen.print("pre auton code")
   left_piston.set(1)
   right_piston.set(1)
controller = Controller()
vision_6__BRIE = Signature(1, -6739, -4981, -5860,-3855, -1237, -2546,2.5, 0)
motor1 = Motor(Ports.PORT1, False)  # Front left, direction reversed
motor2 = Motor(Ports.PORT2, True)  # Front right
motor3 = Motor(Ports.PORT3, False) # Back left, direction reversed
motor4 = Motor(Ports.PORT4, True) # Back right
motor6 = Motor(Ports.PORT5, False)#mid left wheel
motor7 = Motor(Ports.PORT6, True)#mid right wheel
left_drive_smart = MotorGroup(motor1, motor3)
right_drive_smart = MotorGroup(motor2, motor4)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 342.9, 304.79999999999995, MM, 1)

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
    drivetrain.drive_for(FORWARD, 4, INCHES)
    drivetrain.drive_for(FORWARD, -4, INCHES)
    drivetrain.turn_for(45, DEGREES)
    drivetrain.drive_for(FORWARD, 5, INCHES)
    angleamt = 0
    while True:
        vision.take_snapshot(1)
        if vision.largest_object().width > 50:
            if vision.largest_object().centerX > 160 or vision.largest_object().centerX < 190:
                x = vision.largest_object().centerX
                finalinching = 0.000372882*x**2 - 0.230912*x+35.4519
                drivetrain.drive_for(finalinching, INCHES)
            elif vision.largest_object().centerX < 160:
                drivetrain.turn_for(15, DEGREES)
                angleamt = angleamt+15
                return
            elif vision.largest_object().centerX > 190:
                drivetrain.turn_for(-15, DEGREES)
                angleamt = angleamt-15
                return
        if vision.largest_object().height > 190:
            finalangle = 360-angleamt
            drivetrain.turn_for(finalangle, DEGREES)
            drivetrain.drive_for(5, INCHES)
            drivetrain.drive_for(-5, INCHES)
            



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
            # Apply a deadzone for precision controls
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





