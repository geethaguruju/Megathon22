from flask import render_template, request, Blueprint, jsonify
from app.api_call_pred import api_call
import datetime
import json
import traceback
import pandas as pd
from app.main import blueprint
from flask_login import (login_required, current_user)

# home page
@blueprint.route("/")
@blueprint.route("/home")
@login_required
def home():
    return render_template('index.html')



@blueprint.route("/preview",methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset)
    return render_template('preview.html',df_view = df)

@blueprint.route("/exploration")
@login_required
def exploration():
    return render_template('exploration.html')

    

@blueprint.route("/interaction")
@login_required
def interaction():
    return render_template('interaction.html')

@blueprint.route("/map")
@login_required
def map():
    return render_template('predictionmap.html')

@blueprint.route("/month")
@login_required
def month():
    return render_template('1month.html')

@blueprint.route("/hour")
@login_required
def hour():
    return render_template('2hour.html')

@blueprint.route("/vehicles")
@login_required
def vehicles():
    return render_template('3vehicles.html')

@blueprint.route("/casualties")
@login_required
def casualties():
    return render_template('4casualties.html')

@blueprint.route("/boroughs")
@login_required
def boroughs():
    return render_template('5boroughs.html')
	
@blueprint.route("/london")
@login_required
def london():
    return render_template('6london.html')


#API to get user inputs
@blueprint.route('/prediction', methods=['POST'])
def prediction():
    try:
        req_data = request.get_json()
        origin = req_data['origin']
        destination = req_data['destination']
        date_time = req_data['datetime']

        #process time
        tm = datetime.datetime.strptime(date_time,'%Y/%m/%d %H:%M').strftime('%Y-%m-%dT%H:%M')

        out = api_call(origin, destination, tm)

        return json.dumps(out)

    except:

        return jsonify({'trace': traceback.format_exc()})

