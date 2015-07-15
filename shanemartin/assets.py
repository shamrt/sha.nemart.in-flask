# -*- coding: utf-8 -*-
from flask_assets import Bundle, Environment

css = Bundle(
    "css/main.scss",
    filters="scss",
    output="public/css/common.css"
)

js = Bundle(
    "js/script.js",
    filters='rjsmin',
    output="public/js/common.js"
)

assets = Environment()

assets.register("js_all", js)
assets.register("css_all", css)
