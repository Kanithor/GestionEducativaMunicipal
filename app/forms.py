from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired

class DocenteForm(FlaskForm):
    rut = StringField('Rut',
           [validators.Required(message = "Rut es requerido")])

    nombre = StringField('Nombre',
            [validators.Required(message = "Nombre es requerido.")])
    
    telefono = IntegerField('Telefono',
            [validators.Required(message = "Telefono es requerido."),
            validators.NumberRange(min=100000000, max=999999999, message="Ingrese un número de teléfono válido.")])

    email = StringField('email',
            [validators.Required(message = "email es requerido")])
    
    calificacion = FloatField('Calificacion',
           [validators.Required(message = "Calificacion es requerido"),
           validators.NumberRange(min=1.0, max=7.0, message="Ingrese una nota válida.")])
    
    direccion = StringField('Direccion',
           [validators.Required(message = "Direccion es requerido")])
    
    formacion = StringField('Formacion',
           [validators.Required(message = "Formacion es requerido")])
    
