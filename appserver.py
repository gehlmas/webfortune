from flask import Flask, render_template, request, session, redirect, url_for, jsonify, abort
import os 
import subprocess

app = Flask(__name__)
app.secret_key = b'ljsdg;sfdgm&@($&ksdGNFJA@($*&HFSKFj'

@app.route('/')
def index():
    return redirect(url_for('fortune'))


@app.route('/fortune/')
def fortune():
    fortune = subprocess.run(['fortune'],stdout=subprocess.PIPE)
    output = fortune.stdout.decode()
    return '<pre>' + output + '</pre>'


@app.route('/cowsay/<message>/')
def cowsay(message):
    fortune = subprocess.run(['cowsay', message],stdout=subprocess.PIPE)
    output = fortune.stdout.decode()
    return '<pre>' + output + '</pre>'


@app.route('/cowfortune/')
def cowfortune():
    fortune = subprocess.run(['fortune'],stdout=subprocess.PIPE)
    fortune_output = fortune.stdout.decode()
    
    cowsay_fortune = subprocess.run(['cowsay', fortune_output],stdout=subprocess.PIPE)
    output = cowsay_fortune.stdout.decode()
    return '<pre>' + output + '</pre>'
