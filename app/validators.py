from flask_wtf import Form
from wtforms.fields.html5 import URLField
import wtforms.validators
from urllib.request import urlopen, HTTPError


class UrlForm(Form):
    long_url = URLField(validators=[wtforms.validators.url()])
# We validate user input in form as URL


def url_state(long_url):
    try:
        if urlopen(long_url).getcode() >= 400:
            return False
        else:
            return True
    except HTTPError:
        return False
# We test URL to see if valid