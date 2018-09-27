"""
    Copyright (c) 2018 Elliott Pardee <me [at] vypr [dot] xyz>
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

from canon_law import central

bp = flask.Blueprint("frontend", __name__)


@bp.route("/")
def index():
    return flask.render_template("index.html")


@bp.route("/apostles/")
def apostles():
    title = "canons of the apostles"

    query = tinydb.Query()

    obj = central.db.search(query.name == "apostles")[0]

    return flask.render_template("council.html", title=title, name=title, obj=obj)


@bp.route("/1nicea/")
def f_nicea():
    title = "first council of nicea (325)"

    query = tinydb.Query()

    obj = central.db.search(query.name == "1nicea")[0]

    return flask.render_template("council.html", title=title, name=title, obj=obj)


@bp.route("/1const/")
def f_const():
    title = "first council of constantinople (381)"

    query = tinydb.Query()

    obj = central.db.search(query.name == "1const")[0]

    return flask.render_template("council.html", title=title, name=title, obj=obj)


@bp.route("/ephesus/")
def ephesus():
    title = "council of ephesus (431)"

    query = tinydb.Query()

    obj = central.db.search(query.name == "ephesus")[0]

    return flask.render_template("council.html", title=title, name=title, obj=obj)


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
