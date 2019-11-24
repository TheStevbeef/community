#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from flask_sqlalchemy import SQLAlchemy


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Community Service'}, pythonic_params=True)

    # Init database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models/db.sqlite3'
    db = SQLAlchemy(app)

    app.run(port=8080)


if __name__ == '__main__':
    main()
