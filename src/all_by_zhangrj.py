"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    # sprint_1()
    # sprint_2()


def sprint_1():
    lenin = rb.Snatch3rRobot()
    print('Test: Stop at red')
    lenin.color_sensor.go_until_color_is(lenin, rb.Color.RED.value)  # (line 416)
    print('Red means stop.')
    print('Test finished!')


def sprint_2():
    # Refer to rosebotics_new --> class ArmAndClaw (line 731)
    # This is a test for the ArmAndClaw
    stalin = rb.Snatch3rRobot()  # Makes the robot

    print('Test: Rise and Shine!')
    stalin.arm.raise_arm_and_close_claw()  # (line 777)
    print('Test finished!')

    print('Test: Calibrating')
    stalin.arm.calibrate()  # (line 754)
    print('Test finished!')

    print('Test: Move arm to different positions')
    stalin.arm.move_arm_to_position(2000)  # (line 794)
    time.sleep(1)
    stalin.arm.move_arm_to_position(4000)
    print('Test finished!')


main()
