"""
    Copyright (c) 2018-2020 Elliott Pardee <me [at] srp [dot] life>
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

bp = flask.Blueprint("api", __name__, url_prefix="/api")


@bp.route("/")
def index():
    return flask.render_template("api.html")


@bp.route("/council/")
@bp.route("/council/<name>/")
@bp.route("/council/<name>/<option>/")
@bp.route("/council/<name>/<option>/<int:canon>/")
def council(name=None, option=None, canon=None):
    if name is None:
        return flask.jsonify({
            "ok": False,
            "msg": "Name not specified."
        })

    query = tinydb.Query()
    results = central.db.search(query.name == name)

    if not results:
        return flask.jsonify({
            "ok": False,
            "msg": f"No database entry for '{name}'."
        })

    if option == "history":
        if len(results[0]["history"]) > 0:
            return flask.jsonify({
                "ok": True,
                "obj": results[0]["history"]
            })
        else:
            return flask.jsonify({
                "ok": False,
                "msg": "No history provided."
            })
    elif option == "canons":
        return flask.jsonify({
            "ok": True,
            "obj": results[0]["canons"]
        })
    elif option == "canon":
        if canon is not None:
            try:
                canon = int(canon)
            except ValueError:
                return flask.jsonify({
                    "ok": False,
                    "msg": "Canon specified is not an integer."
                })

            canons = results[0]["canons"]

            if 0 < canon < len(canons):
                return flask.jsonify({
                    "ok": True,
                    "obj": canons[canon - 1]
                })
            else:
                return flask.jsonify({
                    "ok": False,
                    "msg": f"Canon specified is not between 0 and {str(len(canons))}."
                })

        else:
            return flask.jsonify({
                "ok": False,
                "msg": "Canon not specified."
            })
    else:
        return flask.jsonify({
            "ok": False,
            "msg": "Option not specified or invalid."
        })
