from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField, BooleanField, \
    SelectMultipleField
from wtforms.validators import DataRequired, Length


class JuriForm(FlaskForm):
    body = TextAreaField("Введите данные", default='''{
    "date": {
        "data": <1674594000>,
        "description": "<Татьянин день>"
    },
    "rooms_count": {
        "data": <3>,
        "description": "Количество комнат на этаже"
    },
    "windows_for_room": {
        "data": <[3, ... 1]>,
        "description": "Количество окон в каждой из комнат на этаже слева направо"
    },
    "windows": {
        "data": {
            "floor_1": <[false, true, false, true, false, false]>,
            ...
            "floor_n": <[false, true, false, true, false, false]>
        },
        "description": "Окна по этажам, в которых горит свет"
    }
}''', validators=[DataRequired()])
    submit = SubmitField('Отправить')
