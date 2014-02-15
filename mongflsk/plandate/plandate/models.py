import datetime
from flask import url_for
from plandate import db


class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    phone = db.StringField(max_length=10, required=True)
    zipcode = db.StringField(max_length=5, required=True)

    def get_absolute_url(self):
        return url_for('post', kwargs={"phone": self.phone})

    def __str__(self):
        return self.phone

