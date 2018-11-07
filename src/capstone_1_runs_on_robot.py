"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Sybil Chen.
"""
# ------------------------------------------------------------------------------
# done: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this .
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# done: 2. With your instructor, review the "big picture" of laptop-robot
# done:    communication, per the comment in mqtt_sender.py.
# done:    Once you understand the "big picture", delete this .
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    # --------------------------------------------------------------------------
    # done: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()

    # --------------------------------------------------------------------------
    # done: 4. Add code that constructs a   com.MqttClient   that will
    # done:    be used to receive commands sent by the laptop.
    # :    Connect it to this robot.  Test.  When OK, delete this.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    # --------------------------------------------------------------------------
    # done: 5. Add a class for your "delegate" object that will handle messages
    #:    sent from the laptop.  Construct an instance of the class and
    # :    pass it to the MqttClient constructor above.  Augment the class
    # :    as needed for that, and also to handle the go_forward message.
    # :    Test by PRINTING, then with robot.  When OK, delete this.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # done: 6. With your instructor, discuss why the following WHILE loop,
    # :    that appears to do nothing, is necessary.
    # :    When you understand this, delete this.
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        # TODO: 7. Add code that makes the robot beep if the top-red button
        # TODO:    on the Beacon is pressed.  Add code that makes the robot
        # TODO:    speak "Hello. How are you?" if the top-blue button on the
        # TODO:    Beacon is pressed.  Test.  When done, delete this TODO.
        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work
        # waiting for the message from laptop
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()
            

class RemoteControlEtc(object):

    def __init__(self, robot):
        """
        Stores a robot.
            :type robot: rb.Snatch3rRobot

        """
        self.robot = robot

    def go_forward(self, speed_string):
        speed = int(speed_string)
        print('Robot should start moving')
        self.robot.drive_system.stop_moving(speed, speed)


main()