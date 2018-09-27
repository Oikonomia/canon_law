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

import os
import tinydb

dir_path = os.path.dirname(os.path.realpath(__file__))

from canon_law.extensions.vylogger import VyLogger

logger = VyLogger("default")

db = tinydb.TinyDB(f"{dir_path}/databases/db")


def log_message(level, sender, source, msg):
    message = f"<{sender}@{source}> {msg}"

    if level == "warn":
        logger.warning(message)
    elif level == "err":
        logger.error(message)
    elif level == "info":
        logger.info(message)
    elif level == "debug":
        logger.debug(message)


def import_dataset(file_name, history=None):
    name = file_name
    dataset = open(f"{dir_path}/datasets/{name}.txt")
    lines = dataset.readlines()
    canons = []

    for line in lines:
        split = line.split(" - ")
        canon = int(split[0])
        text = split[1]

        canons.append({"canon": canon, "text": text})

    if history is None:
        history = ""

    db.insert({"name": name, "history": history, "canons": canons})

    print("Done.")


def search_canons(query):
    return "nope."
