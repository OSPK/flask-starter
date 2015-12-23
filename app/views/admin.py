from flask import Blueprint, render_template

admin = Blueprint('admin', __name__)


@admin.route('/')
def dashboard():
    # Do some stuff
    return render_template('admin/index.html')
