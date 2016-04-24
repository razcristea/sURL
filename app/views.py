from app import app, db
from app.models import Urls
from app.generators import generate_short_url
from app.validators import url_state, UrlForm
from datetime import datetime
from flask import abort
from flask import flash
from flask import redirect
from flask import render_template
from flask import request

db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = UrlForm(request.form)
        if form.validate():
            long_url = form.long_url.data
            if url_state(long_url) is True:
                short_url = generate_short_url(long_url)
                return render_template('index.html',
                                       form=form,
                                       short_url=short_url,
                                       year=datetime.now().year
                                       )
            else:
                flash('This URL cannot be reached for the moment or doesn\'t exists.')
                return render_template('index.html',
                                       form=form,
                                       year=datetime.now().year
                                       )
        else:
            flash('This is not a valid URL.')
            return render_template('index.html',
                                   form=form,
                                   year=datetime.now().year
                                   )

    else:
        return render_template('index.html', form=UrlForm(), year=datetime.now().year)


@app.route('/<string:short_url>')
def redirect_to_main_url(short_url):
    # When a short URL comes to this app, the short URL will be redirected to
    # the long URL, we mean main URL. This function does this important task.
    # If the short URL isn't in our database, then it throws 404 error
    # message.

    surl_query = Urls.query.filter_by(short_url=short_url).first()
    if surl_query is None:
        abort(404)
    else:
        return redirect(surl_query.long_url)


@app.errorhandler(404)
def page_not_found(e):
    """

    :type e: HTTPError
    """
    return render_template('404.html'), 404
