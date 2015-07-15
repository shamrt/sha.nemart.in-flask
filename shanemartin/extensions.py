# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located
in app.py
"""

from flask_cache import Cache
cache = Cache()

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()

from flask_misaka import Misaka
markdown = Misaka()

from flask_frozen import Freezer
freezer = Freezer()
