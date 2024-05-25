from wtforms import Form, FloatField, validators

class InputForm1(Form):
    a = FloatField(default=1,validators=[validators.InputRequired()])
    b = FloatField(default=3,validators=[validators.InputRequired()])
    c = FloatField(default=1,validators=[validators.InputRequired()])
