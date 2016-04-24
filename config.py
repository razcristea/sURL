DEBUG = True
# Enables debug mode. To be set to False when deploying to production server!

SECRET_KEY = "The quick brown fox jumps over the lazy dog"

SQLALCHEMY_DATABASE_URI = r'sqlite:///C:\Users\Razvan Cristea\PycharmProjects\sURL\test.db'
# Path to database file to use

SQLALCHEMY_ECHO = True
# If set to True SQLAlchemy will log all the statements issued to stderr
# which can be useful for debugging.

SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and
# will be disabled by default in the future.  Set it to True to suppress this warning.

WTF_CSRF_ENABLED = True
# Disable/enable CSRF protection for forms. Default is True.

