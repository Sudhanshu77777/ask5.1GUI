# Importing necessary libraries
from tkinter import *  # Importing all Tkinter components for GUI
import tkinter.font as FONT  # Importing font handling from Tkinter
import RPi.GPIO as GPIO  # Importing RPi.GPIO to manage GPIO pins

# Setting the pin numbering system to use physical pin numbers on the board
GPIO.setmode(GPIO.BOARD)

# Define BOARD pins for each LED
red_led = 11
green_led = 13
blue_led = 15

# Suppress warnings from GPIO
GPIO.setwarnings(False)

# Set GPIO pins as outputs
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)

# Creating the main window for the GUI
win = Tk()
win.title("LED Controller")  # Setting the window title
myFont = FONT.Font(family='Times New Roman', size=14, weight='bold')  # Defining the font style and size

# Function to turn on the selected LED and turn off all others
def ledControl():
    # Get the selected option from the radio buttons
    selected_led = led_var.get()

    # Control LEDs based on the selected radio button
    if selected_led == 1:
        GPIO.output(red_led, GPIO.HIGH)  # Turn on the red LED
        GPIO.output(green_led, GPIO.LOW)  # Turn off the green LED
        GPIO.output(blue_led, GPIO.LOW)  # Turn off the blue LED
    elif selected_led == 2:
        GPIO.output(blue_led, GPIO.HIGH)  # Turn on the blue LED
        GPIO.output(red_led, GPIO.LOW)  # Turn off the red LED
        GPIO.output(green_led, GPIO.LOW)  # Turn off the green LED
    elif selected_led == 3:
        GPIO.output(green_led, GPIO.HIGH)  # Turn on the green LED
        GPIO.output(red_led, GPIO.LOW)  # Turn off the red LED
        GPIO.output(blue_led, GPIO.LOW)  # Turn off the blue LED

# Function to handle cleanup process and close the application
def close():
    # Turn off all LEDs before cleanup
    GPIO.output(red_led, GPIO.LOW)  # Turn off the red LED
    GPIO.output(green_led, GPIO.LOW)  # Turn off the green LED
    GPIO.output(blue_led, GPIO.LOW)  # Turn off the blue LED
    GPIO.cleanup()  # Clean up GPIO settings to free up resources
    win.quit()  # Close the Tkinter window and exit the application

# Create an IntVar to hold the selected LED value from radio buttons
led_var = IntVar()

# Creating radio buttons to select which LED to control
redRadioButton = Radiobutton(win, text="Red LED", font=myFont, variable=led_var, value=1, command=ledControl, bg='red', height=2, width=30)
redRadioButton.grid(row=0, column=1)  # Positioning the red LED radio button

blueRadioButton = Radiobutton(win, text="Blue LED", font=myFont, variable=led_var, value=2, command=ledControl, bg='blue', height=2, width=30)
blueRadioButton.grid(row=1, column=1)  # Positioning the blue LED radio button

greenRadioButton = Radiobutton(win, text="Green LED", font=myFont, variable=led_var, value=3, command=ledControl, bg='green', height=2, width=30)
greenRadioButton.grid(row=2, column=1)  # Positioning the green LED radio button

# Creating and placing the exit button to close the application
exitButton = Button(win, text="EXIT", font=myFont, command=close, bg='yellow', height=2, width=30)
exitButton.grid(row=3, column=1)  # Positioning the exit button

# Ensuring proper cleanup when the window's close button (X) is clicked
win.protocol("WM_DELETE_WINDOW", close)

# Starting the Tkinter event loop to display the GUI
win.mainloop()  # This line starts the Tkinter application loop
