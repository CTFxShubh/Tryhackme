from wtforms import Form, StringField, validators

class InputForm3(Form):
    xa = StringField(default=1,validators=[validators.InputRequired()])
    xb = StringField(default=3,validators=[validators.InputRequired()])
