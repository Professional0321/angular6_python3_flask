from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from app.basemodels import db, CRUD_MixIn
from datetime import datetime



class Users(db.Model, CRUD_MixIn):
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(250), nullable=False,unique=True)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    createddate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    createdby = db.Column(db.String(250), nullable=False)
    updateddate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updatedby = db.Column(db.String(250), nullable=False)

    def __init__(self,  email,  password,  name,  createddate,  createdby,  updateddate,  updatedby, ):

        self.email = email
        self.password = password
        self.name = name
        self.createddate = createddate
        self.createdby = createdby
        self.updateddate = updateddate
        self.updatedby = updatedby


class UsersSchema(Schema):

    not_blank = validate.Length(min=1, error='Field cannot be blank')
    # add validate=not_blank in required fields
    id = fields.Integer(dump_only=True)

    email = fields.String(validate=not_blank)
    password = fields.String(validate=not_blank)
    name = fields.String(validate=not_blank)
    createddate = fields.Date(required=True)
    createdby = fields.String(validate=not_blank)
    updateddate = fields.Date(required=True)
    updatedby = fields.String(validate=not_blank)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/users/"
        else:
            self_link = "/users/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'users'
