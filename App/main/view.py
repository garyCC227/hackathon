from flask import render_template, Blueprint,redirect,request,flash
from werkzeug import secure_filename
import os
from App.api.foodAPI import Food
from App.implement import *

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


@main_blueprint.route('/detail_recipe')
def detail_recipe():
		
    return render_template('main/recipe.html')


@main_blueprint.route('/')
def index():
    return render_template('main/main.html')

# for survey form
@main_blueprint.route('/temp')
def temp():
	print(data)
	write_to_json_file('data.json', data)
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

		print(name, age, weight, gender, diet, height)
		
	return render_template('main/temp.html')


@main_blueprint.route('/upload', methods=["POST"])
def send_files():
	if request.method == 'POST':
		if 'file' in request.files:
			f = request.files['file']
			if f and allowed_file(f.filename):
				filename = secure_filename(f.filename)
				f.save(os.path.join(UPLOAD_FOLDER+'/',filename))
			else:
				return "bad"
	return "successful_upload"


def allowed_file(filename):
    return '.' in filename and \
					filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
