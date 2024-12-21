#!/usr/bin/env python3
from flask import Flask, request, abort
import coffee_machine
import RPi.GPIO as GPIO
import threading
from time import sleep
import requests

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

@app.route('/coffee', methods=["GET"])
def on_coffee():
    print(request.data)
    coffee_machine.turn_on_off_coffee_machine()
    coffee_machine.start_making_coffee()
    coffee_machine.move_cup_under_nozzle()
    coffee_machine.wait_for_coffee()
    coffee_machine.move_cup_away_from_nozzle()
    return ''


@app.route('/ping', methods=["GET"])
def ping():
    print(request.data)
    return 'coffee pong'

print("starting server on custom thread")
threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8090, debug=True, use_reloader=False)).start()

@app.route('/proxy', methods=["GET"])
def proxy():
    host = request.args.get('host')
    bearer = request.args.get('bearer')
    if host is None or bearer is None:
        abort(404)
    headers = {"Content-Type": "application/json; charset=utf-8", "Authorization": 'Bearer ' + bearer}
    data = requests.get(host, headers=headers).content
    return data

print("starting btn trigger")
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    button_is_unpressed = GPIO.input(21)
    if button_is_unpressed == False:
        print('Coffee button is Pressed')
        coffee_machine.turn_on_off_coffee_machine()
        coffee_machine.start_making_coffee()
        coffee_machine.move_cup_under_nozzle()
        coffee_machine.wait_for_coffee()
        coffee_machine.move_cup_away_from_nozzle()
    sleep(0.5)

