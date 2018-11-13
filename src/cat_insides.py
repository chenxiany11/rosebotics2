
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    mastermind = com.MqttClient()
    mastermind.connect_to_ev3()
    setup_gui(root, mastermind)

    root.mainloop()


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=20)
    frame.grid()

    meow_for_me = ttk.Button(frame, text="Meow Some More")
    meow_for_me.grid()
    meow_for_me['command'] = \
        lambda: dont_listen(mqtt_client)

    pat_a_cat = ttk.Button(frame, text="Let Me Pat")
    pat_a_cat.grid()
    pat_a_cat['command'] = \
        lambda: dont_touch(mqtt_client)


def dont_listen(mqtt_client):
    print('You really think a cat is going to listen to you?')
    mqtt_client.send_message('stop_that_noise')


def dont_touch(mqtt_client):
    print('Dont touch me with your filthy hands')
    mqtt_client.send_message('avoid_strangers')



main()
