#!/usr/bin/env python
import json
from kafka import KafkaProducer
from flask import Flask, request

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:29092')


def log_to_kafka(topic, event):
    event.update(request.headers)
    producer.send(topic, json.dumps(event).encode())


@app.route("/")
def default_response():
    default_event = {'event_type': 'default'}
    log_to_kafka('events', default_event)
    return "This is the default response!\n"


@app.route("/purchase_a_sword")
def purchase_a_sword():
    purchase_sword_event = {'event_type': 'purchase_sword'}
    log_to_kafka('events', purchase_sword_event)
    return "Sword Purchased!\n"

@app.route("/purchase_a_knife")
def purchase_a_knife():
    purchase_knife_event = {'event_type': 'purchase_knife','description': 'very sharp knife'}
    log_to_kafka('events', purchase_knife_event)
    return "Knife Purchased!\n"

@app.route("/purchase_a_shield")
def purchase_a_shield():
    purchase_shield_event = {'event_type': 'purchase_shield','description': 'very protective shield'}
    return "Shield Purchased!\n"

@app.route("/join_a_guild")
def join_a_guild():
    join_guild_event = {'event_type': 'join_guild','description': 'large guild'}
    log_to_kafka('events', join_guild_event)
    return "Guild Joined!\n"
    
@app.route("/declare_ones_fealty")
def declare_ones_fealty():
    declare_fealty_event = {'event_type': 'declare_fealty','description': 'great leader'}
    log_to_kafka('events', declare_fealty_event)
    return "Fealty declared!\n"
    
@app.route("/declare_a_war")
def declare_a_war():
    declare_war_event = {'event_type': 'declare_war','description': 'bloody war'}
    log_to_kafka('events', declare_war_event)
    return "War declared!\n"

