# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import SkiSlopePost

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    ski_slope_posts = SkiSlopePost.query.order_by(SkiSlopePost.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', ski_slope_posts=ski_slope_posts)

@core.route('/info')
def info():
    return render_template('info.html')