from wtforms import Form, FloatField, validators

class InputForm2(Form):
    number = FloatField(default=3,validators=[validators.InputRequired()])
