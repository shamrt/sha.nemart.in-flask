# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from collections import OrderedDict
from datetime import date
import yaml
from flask import (Blueprint, request, render_template, flash, url_for,
                    redirect, session)

from shanemartin.utils import flash_errors

blueprint = Blueprint('public', __name__, static_folder="../static")


def import_yaml(file_path):
    with open(file_path, 'r') as f:
        y = yaml.load(f)
        return OrderedDict(reversed(sorted(y.items(), key=lambda t: t[0])))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    experience = import_yaml('data/experience.yaml')

    print experience
    profile = yaml.load(open('data/profile.yaml', 'r'))
    profile['meta']['years_of_work'] = date.today().year - profile['meta']['year_started_work']

    return render_template("public/home.html", xp=experience, pf=profile)
