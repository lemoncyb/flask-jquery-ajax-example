from flask import Flask

app = Flask(
        __name__,
        template_folder='templates',
        static_folder='assets',
    )
app.config.from_object('fjae.settings')

from fjae import views

