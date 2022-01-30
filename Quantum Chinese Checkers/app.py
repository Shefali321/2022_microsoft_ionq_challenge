from flask import Flask, render_template, request, flash, redirect, url_for
from flask_socketio import SocketIO, send
from flask import jsonify
import os
app = Flask('app', static_folder="templates/images")
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
game_state = "new"
p1_game_history = {}
p2_game_history = {}
p = []
for i in range(0,6):
  p.append("/images/blue_piece.png")
for i in range(6,19):
  p.append("/images/hollow_circle.png")
for i in range(19, 25):
  p.append("/images/red_piece.png")
global turn


@app.route('/')
def hello_world():
  game_state = "new"
  return render_template('index.html')
  

@app.route('/player1')
def player1_turn():
  return render_template('player1.html', p=p, game_status="Welcome to Quantum Chinese Checkers!")

@app.route('/player2')
def player2_turn():
  return render_template('player2.html', p=p, game_status="Welcome to Quantum Chinese Checkers!")

"""
@app.route('/test')
def test_tourn():
  return flash('Sorry, not your turn.')

@socketio.on('message')
def handleMessage(user_input):
	pass
  #board_output
	#send(board_output, broadcast=True)
"""

@app.route('/player2', methods=["POST"])
def player1_move():
  
  
  si = request.form["si"]
  fi = request.form["fi"]
  qm = request.form["qm"]
  
  
  r1 = render_template("player1.html", p=p, game_status="Welcome to Quantum Chinese Checkers!")
  r2 = render_template("player2.html", p=p, game_status="Welcome to Quantum Chinese Checkers!")
  return (r1, r2)

  

@app.route('/player1', methods=["POST"])
def player2_move():
  si = request.form["si"]
  fi = request.form["fi"]
  qm = request.form["qm"]
  
  r1 = render_template("player1.html", p=p, game_status="Welcome to Quantum Chinese Checkers!")
  r2 = render_template("player2.html", p=p, game_status="Welcome to Quantum Chinese Checkers!")
  return (r1, r2)

app.run(host='0.0.0.0', port=8080)
