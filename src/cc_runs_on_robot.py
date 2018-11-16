import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3

def main():

    robot = rb.Snatch3rRobot()
    rc = RemoteControl(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
    while True:
        if robot.beacon_button_sensor.is_bottom_red_button_pressed():
            ev3.Sound.beep().wait()
        time.sleep(0.01)

class RemoteControl(object):
    def __init__(self, robot):
        self.robot = robot
        pass

    def go_forward(self, speed):
        self.robot.drive_system.start_moving(speed, speed)
        # ev3.Sound.speak('ha ha ha').wait()

    def go_backward(self, speed):
        self.robot.drive_system.start_moving(-speed, -speed)
        # ev3.Sound.speak('I do not want to go back').wait()

    def stop(self):
        self.robot.drive_system.stop_moving()
        # ev3.Sound.speak('What do you want me to do?').wait()

    def turn_left(self):
        self.robot.drive_system.spin_in_place_degrees(-90)
        # ev3.Sound.speak('I should do right thing').wait()

    def turn_right(self):
        self.robot.drive_system.spin_in_place_degrees(90)
        # ev3.Sound.speak('I am right').wait()

    def gogogo(self, speed):
        self.robot.drive_system.start_moving(speed, speed)
        while True:
            print(self.robot.proximity_sensor.get_distance_to_nearest_object())
            if self.robot.proximity_sensor.get_distance_to_nearest_object() < 15:
                self.robot.drive_system.stop_moving()
                ev3.Sound.speak('Something is in front of me, I am scared').wait()

    def get_red(self, speed):
        self.robot.drive_system.start_moving(speed, speed)
        print(self.robot.color_sensor.get_value)
        self.robot.color_sensor.go_until_color_is(self.robot, rb.Color.RED.value)
        ev3.Sound.speak('I found red').wait()

main()