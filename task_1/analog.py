import tkinter as tk
import time
import math

root = tk.Tk()
root.geometry("400x400")

def update_clock():
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Update seconds hand
    seconds_angle = seconds * 6
    seconds_x = seconds_hand_length * math.sin(math.radians(seconds_angle)) + center_x
    seconds_y = -1 * seconds_hand_length * math.cos(math.radians(seconds_angle)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    # Update minutes hand
    minutes_angle = minutes * 6
    minutes_x = minutes_hand_length * math.sin(math.radians(minutes_angle)) + center_x
    minutes_y = -1 * minutes_hand_length * math.cos(math.radians(minutes_angle)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    # Update hours hand
    hours_angle = hours * 30 + 0.5 * minutes + 0.008 * seconds
    hours_x = hours_hand_length * math.sin(math.radians(hours_angle)) + center_x
    hours_y = -1 * hours_hand_length * math.cos(math.radians(hours_angle)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    root.after(1000, update_clock)

canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack(expand=True, fill='both')

# Use the same image for background and dial
dial_image = tk.PhotoImage(file='dial_400.png')
canvas.create_image(200, 200, image=dial_image)

# Create clock hands
center_x = 200
center_y = 200

seconds_hand_length = 95
minutes_hand_length = 80
hours_hand_length = 60

seconds_hand = canvas.create_line(200, 200, 200 + seconds_hand_length, 200 + seconds_hand_length, width=1.5, fill='blue')
minutes_hand = canvas.create_line(200, 200, 200 + minutes_hand_length, 200 + minutes_hand_length, width=2, fill='yellow')
hours_hand = canvas.create_line(200, 200, 200 + hours_hand_length, 200 + hours_hand_length, width=4, fill='green')

update_clock()

root.mainloop()
