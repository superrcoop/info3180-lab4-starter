
from flask_wtf import FlaskForm , RecaptchaField
from flask_wtf.file import FileField, FileAllowed, FileRequired


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

class UploadForm(FlaskForm):
    upload = FileField('Upload', validators=[
        FileRequired(),
        FileAllowed(ALLOWED_EXTENSIONS, 'Images only!')
    ])