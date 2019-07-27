from flask import render_template, Blueprint,redirect,request,flash
from werkzeug import secure_filename
import os
from App.api.foodAPI import Food
from App.implement import *

import backend.google_vision
import backend.analyze
import backend.classification
import sys
import numpy as np

f = Food()
data = f.generate_recipe_card()

main_blueprint = Blueprint(
    'main',
    __name__,
    static_folder = 'static',
    template_folder = 'templates'
)

UPLOAD_FOLDER = './App/main/static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@main_blueprint.route('/result')
def result():
    return render_template('main/result.html', datas=data) 


@main_blueprint.route('/detail_recipe', methods=['POST','GET'])
def detail_recipe():
	if request.method == 'POST':
		recipe_name = request.form.get('recipe_name')
		recipe_id = request.form.get('recipe_id')
		ids = f.get_video_id(recipe_name)

		urls = []
		for id in ids:
			urls.append("https://www.youtube.com/embed/"+id["youTubeId"])
		
		# detail 
		html_nutri = f.visualize_nutrition(recipe_id)
		html_ingre = f.visualize_ingredient(recipe_id)
		html_equip = f.visualize_equipment(recipe_id)
		
		return render_template('main/recipe.html', links = urls, nutri=html_nutri, ingre=html_ingre, equip=html_equip)
	
	return render_template('main/result.html', datas=data)

# for survey form
@main_blueprint.route('/')
def index():
	return render_template('main/temp.html')


@main_blueprint.route('/submit_survey', methods=['POST','GET'])
def submit_survey():
	if request.method == 'POST':
		input = request.form
		# user input
		name = input.get('name')
		age = input.get('age')
		weight = input.get('weight')
		gender = input.get('gender')
		diet = input.get('diet')
		height = input.get('height')

		if 'file' in request.files:
			f = request.files['file']
			if f and allowed_file(f.filename):
				filename = secure_filename(f.filename)
				f.save(os.path.join(UPLOAD_FOLDER+'/',filename))
		
		# image file image
		fn = f.filename
		print(fn)
		# print(name, age, weight, gender, diet, height)
		
	return render_template('main/temp.html')



def allowed_file(filename):
    return '.' in filename and \
					filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
