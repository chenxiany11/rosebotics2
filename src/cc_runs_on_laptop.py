
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    # Making a GUI
    root = tkinter.Tk()

    # mqtt stuff
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    # Setting up the GUI
    setup_gui(root, mqtt_client)

    # Running the GUI
    root.mainloop()


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=100)
    frame.grid()

    go_button = ttk.Button(frame, text="Go Forward")
    back_button = ttk.Button(frame, text="Go Backward")
    stop_button = ttk.Button(frame, text="Stop Moving")
    turn_left_button = ttk.Button(frame, text="Turn Left")
    turn_right_button = ttk.Button(frame, text="Turn Right")
    speed_entry_box = ttk.Entry(frame)
    gogogo_button = ttk.Button(frame, text="Go until find something")
    get_red_button = ttk.Button(frame, text="GET RED")

    speed_entry_box.grid(row=1, column=2)
    go_button.grid(row=5, column=2)
    stop_button.grid(row=10, column=2)
    back_button.grid(row=15, column=2)
    turn_left_button.grid(row=10, column=1)
    turn_right_button.grid(row=10, column=3)
    gogogo_button.grid(row=20, column=2)
    get_red_button.grid(row=25, column=2)

    go_button['command'] = \
        lambda: go_forward(speed_entry_box, mqtt_client)
    stop_button['command'] = \
        lambda: stop(mqtt_client)
    back_button['command'] = \
        lambda: go_backward(speed_entry_box, mqtt_client)
    turn_left_button['command'] = \
        lambda: turn_left(mqtt_client)
    turn_right_button['command'] = \
        lambda: turn_right(mqtt_client)
    gogogo_button['command'] = \
        lambda: gogogo(speed_entry_box, mqtt_client)
    get_red_button['command'] = \
        lambda: get_red(speed_entry_box, mqtt_client)


def go_forward(entry_box, mqtt_client):
    speed = int(entry_box.get())
    mqtt_client.send_message('go_forward', [speed])
    print('I am moving forward')


def stop(mqtt_client):
    mqtt_client.send_message('stop')
    print('Ok I will stop')


def go_backward(entry_box, mqtt_client):
    speed = int(entry_box.get())
    mqtt_client.send_message('go_backward', [speed])
    print('Ok I will go back')


def turn_left(mqtt_client):
    mqtt_client.send_message('turn_left')
    print('Turn left is right')


def turn_right(mqtt_client):
    mqtt_client.send_message('turn_right')
    print('Turn right is right')


def gogogo(entry_box, mqtt_client):
    speed = int(entry_box.get())
    mqtt_client.send_message('gogogo', [speed])
    print('I found something')


def get_red(entry_box, mqtt_client):
    speed = int(entry_box.get())
    mqtt_client.send_message('get_red', [speed])
    print('I found red!')


main()