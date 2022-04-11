from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db
from myapp.models import SkiSlopePost
from myapp.ski_slope_posts.forms import SkiSlopePostForm, SkiSlopePostsForm

ski_slope_posts = Blueprint('ski_slope_posts', __name__)

@ski_slope_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
  form = SkiSlopePostForm()
  if form.validate_on_submit():
    ski_slope_post = SkiSlopePost (title=form.title.data, text=form.text.data, user_id=current_user.id)
    db.session.add(ski_slope_post)
    db.session.commit()
    flash('Ski Slope Post Created')
    print('Ski Slope Post was Created')
    return redirect(url_for('core.index'))
  return render_template('create_post.html', form=form)

@ski_slope_posts.route('/<int:ski_slope_post_id>')
def ski_slope_post(ski_slope_post_id):
  ski_slope_post = SkiSlopePost.query.get_or_404(ski_slope_post_id)
  return render_template('ski_slope_post.html', title=ski_slope_post.title, date=ski_slope_post.date, post=ski_slope_post)