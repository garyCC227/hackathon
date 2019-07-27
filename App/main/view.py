from flask import render_template, Blueprint,redirect,request,flash
from werkzeug import secure_filename
import os
from App import app


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
    return render_template('main/video.html')

@main_blueprint.route('/detail_recipe')
def detail_recipe():
    return render_template('main/recipe.html')

@main_blueprint.route('/')
def index():
    return render_template('main/main.html')

@main_blueprint.route('/temp')
def temp():
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