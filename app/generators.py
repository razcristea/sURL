import random
import string
from app import db
from app.models import Urls
from flask import request


def generate_random_string(length):
    random_string = ''.join(random.choice(
        string.ascii_letters + string.digits) for i in range(length))
    return random_string
# Function to generate a random string.


def generate_short_url(long_url):
    db_query_long = Urls.query.filter_by(long_url=long_url).first()
    if db_query_long is None:
        for i in range(4, 10):
            short_url = generate_random_string(i)
            db_query_short = Urls.query.filter_by(short_url=short_url).first()
            if db_query_short is None:
                data = Urls(long_url, short_url)
                db.session.add(data)
                db.session.commit()
                return request.url_root + short_url
    else:
        return request.url_root + db_query_long.short_url
# Main function that generates shortened URL and adds pair (long+short) into database.