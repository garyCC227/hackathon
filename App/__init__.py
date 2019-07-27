from flask import *
import os

app = Flask(__name__)
app.config['SECRECT_KEY'] = 'Strong'
app.secret_key = 'any random string'


from App.main.view import main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/main')



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 