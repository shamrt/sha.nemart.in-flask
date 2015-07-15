from flask_frozen import Freezer
from shanemartin import app

freezer = Freezer(app.create_app())
freezer.freeze()
