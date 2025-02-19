from gpiozero import AngularServo
from time import sleep
import RPi.GPIO as GPIO

TIME_COFFEE_MACHINE_STARTUP_SEC = 70
TIME_MAKING_COFFEE_SMALL_SEC = 35.5  # 40
TIME_MOVE_CUP_SEC = 4
TIME_PRESSING_BUTTON_SEC = 0.5

GPIO_SERVO = 18
GPIO_COFFEE_MACHINE_SWITCH = 15
GPIO_COFFEE_MACHINE_COFFEE_SMALL = 14


##
# simulate button on/off
# wait TIME_COFFEE_MACHINE_STARTUP_SEC sec for cleaning procedure
#
def turn_on_off_coffee_machine():
    print(f'turn_on_off_coffee_machine')
    GPIO.setup(GPIO_COFFEE_MACHINE_SWITCH, GPIO.OUT)
    sleep(TIME_PRESSING_BUTTON_SEC)
    GPIO.setup(GPIO_COFFEE_MACHINE_SWITCH, GPIO.HIGH)
    sleep(TIME_COFFEE_MACHINE_STARTUP_SEC)


##
# simulate button for making coffee
#
def start_making_coffee():
    print(f'start_making_coffee')
    GPIO.setup(GPIO_COFFEE_MACHINE_COFFEE_SMALL, GPIO.OUT)
    sleep(TIME_PRESSING_BUTTON_SEC)
    GPIO.setup(GPIO_COFFEE_MACHINE_COFFEE_SMALL, GPIO.HIGH)


##
# wait TIME_MAKING_COFFEE_SMALL_SEC sec for coffee
#
def wait_for_coffee():
    print(f'make_coffee')
    sleep(TIME_MAKING_COFFEE_SMALL_SEC)


##
# move servo in one direction to move coffee under the nozzle
#
def move_cup_under_nozzle():
    print(f'move_cup_under_nozzle')
    servo = AngularServo(GPIO_SERVO, min_pulse_width=0.0006, max_pulse_width=0.0023)
    servo.angle = 90
    sleep(TIME_MOVE_CUP_SEC)
    servo.angle = 0


##
# move servo in one direction to move coffee away from the nozzle
#
def move_cup_away_from_nozzle():
    print(f'move_cup_away_from_nozzle')
    servo = AngularServo(GPIO_SERVO, min_pulse_width=0.0006, max_pulse_width=0.0023)
    servo.angle = -90
    sleep(TIME_MOVE_CUP_SEC)
    servo.angle = 0
