import tkinter as tk
import subprocess

def save_mapping():
    changes = []
    for s in selected:
        changes.append(s.get())

    f = open("GestureBinds.txt", 'w')
    f.write("\n".join(changes))
    f.close()

    print("Changes saved")


def load_gesture_bindings():
    gesture_to_movement.clear()

    try:
        f = open("GestureBinds.txt", "r")
        for i in range(6): 
            gesture_to_movement.append((int)(f.readline()))

    except FileNotFoundError:
        print("GestureBinds.txt not found. Starting with an empty mapping.")


def start_control():
    try:
        subprocess.run(['python3', "/Users/tt/Desktop/RoboticArm/Gesture.py"], check=True)

    except Exception as e:
        print("Error:", str(e))


def open_gesture_binding_window():
    binds = gesture_to_movement.copy()
    #print(binds)

    binding_window = tk.Toplevel(root)

    binding_window.title("Edit Gesture Binding")

    for i in range(6):
        gesture_label = tk.Label(binding_window, text=movements[i], font=("Arial", 12))
        gesture_label.pack()

        var = tk.StringVar(root)
        var.set(str(binds[i]))
        gesture_dropdown = tk.OptionMenu(binding_window, var, *gestures)
        gesture_dropdown.pack()
        selected.append(var)

    save_button = tk.Button(
        binding_window,
        text="Save Mapping",
        command=save_mapping,
        font=("Arial", 12),
        bg="green",
        fg="white",
    )

    save_button.pack()


selected = []
gesture_to_movement = []

load_gesture_bindings()
#print(gesture_to_movement)

root = tk.Tk()

root.title("Robotic Arm Control")


entrance_frame = tk.Frame(root, padx=20, pady=20)

entrance_frame.pack()

title_label = tk.Label(entrance_frame, text="Robotic Arm Control", font=("Arial", 24))

title_label.pack()


entrance_label = tk.Label(
    entrance_frame, text="The Reason for This Project", font=("Arial", 14)
)

entrance_label.pack()


frame_a = tk.Frame()
label_a = tk.Label(master=frame_a, text="I am doing this project to create a gesture-controlled robotic arm for...\n")
label_a.pack()




binding_frame = tk.Frame(root, padx=20, pady=20)

binding_frame.pack()


binding_label = tk.Label(binding_frame, text="Gesture Binding", font=("Arial", 14))

binding_label.pack()


gestures = [i for i in range(1, 11)]

movements = ["X-Clockwise", "X-Anticlockwise", "Y-Clockwise","Y-Anticlockwise", "Z-Clockwise", "Z-Anticlockwise"]


edit_button = tk.Button(
    binding_frame,
    text="Edit Gesture Binding",
    command=open_gesture_binding_window,
    font=("Arial", 12),
    bg="blue",
    fg="white",
)

edit_button.pack()


control_frame = tk.Frame(root, padx=20, pady=20)

control_frame.pack()


control_label = tk.Label(
    control_frame, text="Ready to Control the Robotic Arm?", font=("Arial", 16)
)

control_label.pack()


start_button = tk.Button(
    control_frame,
    text="Start Control",
    command=start_control,
    font=("Arial", 14),
    bg="blue",
    fg="white",
)

start_button.pack()


root.mainloop()

