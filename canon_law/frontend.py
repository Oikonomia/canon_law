"""
    Copyright (c) 2018-2019 Elliott Pardee <me [at] vypr [dot] xyz>
    This file is part of canon_law.

    canon_law is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    canon_law is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with canon_law.  If not, see <http://www.gnu.org/licenses/>.
"""

import flask
import tinydb
import random

from canon_law import central

bp = flask.Blueprint("frontend", __name__)

page_titles = {
    "apostles": "canons of the apostles",
    "1nicea": "first council of nicea (325)",
    "1const": "first council of constantinople (381)",
    "ephesus": "council of ephesus (431)",
    "chalcedon": "council of chalcedon (451)",
    "2const": "second council of constantinople (553)",
    "3const": "third council of constantinople (680-681)",
    "trullo": "council of trullo (quinisext) (692)"
}


@bp.route("/")
def index():
    return flask.render_template("index.html")


@bp.route("/c/<council>/")
def read_council(council=None):
    if council in page_titles.keys():
        title = page_titles[council]

        query = tinydb.Query()

        obj = central.db.search(query.name == council)[0]

        return flask.render_template("council.html", title=title, obj=obj)
    else:
        random_index = random.randint(0, (len(page_titles.keys()) - 1))

        random_council = list(page_titles.keys())[random_index]

        return flask.render_template("unknown_council.html", random_council=random_council)


@bp.route("/search/", methods=["GET", "POST"])
def search():
    query = flask.request.form["query"]
    results = central.search_canons(query)

    return flask.render_template("search.html", query=query, results=results)


@bp.route("/about/")
def about():
    return flask.render_template("about.html")


@bp.route("/disclaimer/")
def disclaimer():
    return flask.render_template("disclaimer.html")
