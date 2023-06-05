from flask import Flask, request
from main import app
from controller import event_handler


@app.route('/add-event', methods=['POST'])
def add_event():
    event_data = request.get_json()
    name = event_data['name']
    date = event_data['date']
    event_handler.add_event(name, date)
    return "hello"
