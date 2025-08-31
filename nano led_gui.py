import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import Tk

# GPIO setup
GPIO.setmode(GPIO.BCM)
led_1 = 17
led_2 = 22
led_3 = 27

GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)

# Function to turn on selected LED
def turn_on_led():
    selected = var.get()
    GPIO.output(led_1, selected == 1)
    GPIO.output(led_2, selected == 2)
    GPIO.output(led_3, selected == 3)

# Function to turn off all LEDs
def turn_off_leds():
    GPIO.output(led_1, False)
    GPIO.output(led_2, False)
    GPIO.output(led_3, False)

# GUI setup
root = Tk()
root.title("LED Control")

var = tk.IntVar()

tk.Label(root, text="Select an LED to turn on:").pack()

tk.Radiobutton(root, text="LED 1", variable=var, value=1, command=turn_on_led).pack()
tk.Radiobutton(root, text="LED 2", variable=var, value=2, command=turn_on_led).pack()
tk.Radiobutton(root, text="LED 3", variable=var, value=3, command=turn_on_led).pack()

tk.Button(root, text="Turn Off All LEDs", command=turn_off_leds).pack(pady=5)
tk.Button(root, text="Exit", command=lambda:(GPIO.cleanup(), root.destroy())).pack()

root.mainloop()