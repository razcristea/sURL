from app import db


class Urls(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String)
    short_url = db.Column(db.String(100))
    
    def __init__(self, long_url, short_url):
        """

        :type short_url: <class 'str'>
        """
        self.long_url = long_url
        self.short_url = short_url
