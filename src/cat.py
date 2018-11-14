
import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import random


def main():

    cat = rb.Snatch3rRobot()
    rc = MindControl(cat)
    mastermind = com.MqttClient(rc)
    mastermind.connect_to_pc()

    while True:
        MindControl.meow_for_momma()


class MindControl(object):
    def __init__(self, cat):
        self.cat = cat
        self.meow = 0

    def meow_for_momma(self):
        if self.meow == 0:
            ev3.Sound.speak('Meow')
            time.sleep(1)
        else:
            ev3.Sound.speak('I am not listening to you')

    def stop_that_noise(self):
        self.meow = 1

    def avoid_strangers(self):
        cat = rb.Snatch3rRobot()
        shoo = [300, 600, 800, 900, 1200, 1500, 1800]
        count = 0
        comments = ['shoo', 'so dirty', 'do not touch me human','try that again I dare you', 'hiss']
        while True:
            if count < 10:
                cat.arm.move_arm_to_position(random.choice(shoo))
                print(random.choice(comments))
                time.sleep(1)
                cat.arm.go_back()
                count += 1
            else:
                break







main()