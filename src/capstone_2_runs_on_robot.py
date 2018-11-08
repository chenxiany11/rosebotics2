"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Rachel Zhang.
"""

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():

    stalin = rb.Snatch3rRobot
    rc = RemoteControlEtc(stalin)
    mastermind = com.MqttClient(rc)
    mastermind.connect_to_pc()

    while True:
        if stalin.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()
        if stalin.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak('Hello. How are you?').wait()
        time.sleep(0.01) #For the delegate to do its work

class RemoteControlEtc(object):
    def __init__(self, stalin):
        """
        Stores the robot.
          :type   robot: rb.Snatch3rRobot
        """

        self.stalin = stalin

    def go_forward(self, gotta_go_fast):
        zoom = int(gotta_go_fast)
        print('zoom zoom')
        self.stalin.drive_system.start_moving(zoom, zoom)



main()