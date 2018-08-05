import json
from flask import (
    Blueprint, current_app, flash, g, render_template, request,
    session, url_for, send_file
)
from flask_babel import get_locale, gettext as _

main = Blueprint("showcase", __name__)

@main.route("/showcase", methods=["GET",])
def showcase():
    gallery = [
        ['1', 2450, 2450],
        ['2', 2221, 2509],
        ['3', 2101, 2536],
        ['4', 2348, 2722],
        ['5', 1804, 2745],
        ['6', 2897, 3307],
        ['7', 2239, 2321],
        ['8', 2419, 2470],
        ['9', 2602, 3307]]

    gallery = [{'src': url_for('static', filename='manual/%s.jpg' % idx),
                'w': w,
                'h': h } for idx, w, h in gallery]
    return render_template("showcase.html", gallery=gallery)
