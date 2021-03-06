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

import os
import flask
import werkzeug

from canon_law import central


def create_app():
    app = flask.Flask("canon_law", instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import api, frontend
    app.register_blueprint(api.bp)
    app.register_blueprint(frontend.bp)

    app.register_error_handler(werkzeug.exceptions.HTTPException, frontend.error_page)

    return app
