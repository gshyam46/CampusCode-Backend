# backend/routes/sample.py
from flask import Blueprint

sample_bp = Blueprint('sample', __name__)

@sample_bp.route('/sample')
def get_sample_data():
    return {'message': 'This is a sample route.'}
