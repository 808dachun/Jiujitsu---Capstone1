from flask import Flask, request,jsonify, render_template, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, phase, ground_position, move, standing
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL',"postgresql:///jiujitsu")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'hellosecret1')

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/', methods=['GET'])
def root():
    """Intro Page to Juijitsu, includes routes to the standing and ground position"""

    phases = phase.query.order_by(phase.name).all()

    return render_template('home.html', phases=phases)

@app.route('/Ground Position', methods=['GET'])
def groundPosition():
    """Show a page with info on Ground Position"""

    phases = phase.query.order_by(phase.name).all()
    
    ground_positions = ground_position.query.order_by(ground_position.name).all()
    
    return render_template('groundPosition.html', ground_positions=ground_positions)

@app.route('/Standing Position', methods=['GET'])
def standingPosition():
    """Show a page with info on Ground Position"""

    Standings = standing.query.order_by(standing.name).all()
    
    return render_template('standingPosition.html', Standings=Standings)

@app.route('/Back Mount', methods=['GET'])
def backMount():
    """Show a page with info on all Back Mount Moves"""

    Back_Mounts = move.query.filter_by(groundPositionCode='Back_Mount')
   
    return render_template('backMount.html', Back_Mounts = Back_Mounts)

@app.route('/Top Mount', methods=['GET'])
def topMount():
    """Show a page with info on all Top Mounts Moves"""
    Top_Mounts = move.query.filter_by(groundPositionCode='Top_Mount')

    return render_template('topMount.html', Top_Mounts = Top_Mounts )

@app.route('/Closed Guard', methods=['GET'])
def closedGuard():
    """Show a page with info on all Closed Guard Moves"""

    Closed_Guards = move.query.filter_by(groundPositionCode='Closed_Guard')
   
    return render_template('closedGuard.html', Closed_Guards = Closed_Guards)

@app.route('/Side Control', methods=['GET'])
def sideControl():
    """Show a page with info on all Side Control Moves"""

    Side_Controls = move.query.filter_by(groundPositionCode='Side_Control')
   
    
    return render_template('sideControl.html', Side_Controls = Side_Controls)

@app.route('/Half Guard', methods=['GET'])
def halfGuard():
    """Show a page with info on all Half Guard Moves"""

    Half_Guards = move.query.filter_by(groundPositionCode='Half_Guard')
   
    
    return render_template('halfGuard.html', Half_Guards = Half_Guards )

@app.route('/Open Guard', methods=['GET'])
def openGuard():
    """Show a page with info on all Open Guard Moves"""
   
    Open_Guards = move.query.filter_by(groundPositionCode='Open_Guard')
    
    return render_template('openGuard.html', Open_Guards=Open_Guards)
