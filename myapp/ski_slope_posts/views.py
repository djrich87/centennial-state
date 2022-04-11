from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db
from myapp.models import SkiSlopePost
from myapp.ski_slope_posts.forms import SkiSlopePostsForm

ski_slope_posts = Blueprint('ski_slope_posts', __name__)