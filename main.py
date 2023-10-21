import tkinter as tk
import subprocess

# Create a function to save the gesture mappings to a file
def save_mapping():
    # Collect user-selected gesture mappings
    changes = []
    for s in selected:
        changes.append(s.get())

    # Open the file for writing and save the changes
    f = open("GestureBinds.txt", "w")
    f.write("\n".join(changes))
    f.close()

    print("Changes saved")

# Create a function to load the gesture bindings from a file
def load_gesture_bindings():
    gesture_to_movement.clear()

    try:
        # Attempt to open and read the file
        f = open("GestureBinds.txt", "r")
        for i in range(6):
            gesture_to_movement.append((int)(f.readline()))

    except FileNotFoundError:
        print("GestureBinds.txt not found. Starting with an empty mapping.")

# Create a function to start the robotic arm control
def start_control():
    try:
        # Run the "Gesture.py" script
        subprocess.run(
            ["python3", "Gesture.py"], check=True
        )

    except Exception as e:
        print("Error:", str(e))

# Create a function to open a window for editing gesture bindings
def open_gesture_binding_window():
    binds = gesture_to_movement.copy()

    # Create a new window for editing gesture bindings
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

    # Create a button to save the mapping
    save_button = tk.Button(
        binding_window,
        text="Save Mapping",
        command=save_mapping,
        font=("Arial", 12),
        bg="green",
        fg="white",
    )

    save_button.pack()


if __name__ == "__main__":
    # Initialize lists and load gesture bindings
    selected = []
    gesture_to_movement = []
    load_gesture_bindings()

    # Create the main application window
    root = tk.Tk()
    root.title("Robotic Arm Control")

    # Create entrance_frame
    entrance_frame = tk.Frame(root, padx=20, pady=20)
    entrance_frame.pack()
    title_label = tk.Label(entrance_frame, text="Robotic Arm Control", font=("Arial", 24))
    title_label.pack()
    entrance_label = tk.Label(
        entrance_frame, text="The Reason for This Project", font=("Arial", 14)
    )
    entrance_label.pack()

    # Create binding_frame
    binding_frame = tk.Frame(root, padx=20, pady=20)
    binding_frame.pack()
    binding_label = tk.Label(binding_frame, text="Gesture Binding", font=("Arial", 14))
    binding_label.pack()

    # List of available gestures and movements
    gestures = [i for i in range(1, 11)]
    movements = [
        "X-Clockwise",
        "X-Anticlockwise",
        "Y-Clockwise",
        "Y-Anticlockwise",
        "Z-Clockwise",
        "Z-Anticlockwise",
    ]

    # Create button to edit gesture binding
    edit_button = tk.Button(
        binding_frame,
        text="Edit Gesture Binding",
        command=open_gesture_binding_window,
        font=("Arial", 12),
        bg="blue",
        fg="white",
    )
    edit_button.pack()

    # Create control_frame
    control_frame = tk.Frame(root, padx=20, pady=20)
    control_frame.pack()
    control_label = tk.Label(
        control_frame, text="Ready to Control the Robotic Arm?", font=("Arial", 16)
    )
    control_label.pack()

    # Create button to start robotic arm control
    start_button = tk.Button(
        control_frame,
        text="Start Control",
        command=start_control,
        font=("Arial", 14),
        bg="blue",
        fg="white",
    )
    start_button.pack()

    # Start the main application loop
    root.mainloop()
