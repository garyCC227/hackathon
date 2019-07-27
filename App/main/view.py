from flask import render_template, Blueprint,redirect,request,flash

main_blueprint = Blueprint(
    'main',
    __name__,
    static_folder = 'static',
    template_folder = 'templates'
)


@main_blueprint.route('/')
def index():
    return render_template('main/main.html')
