from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "uploads")
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # max 16 MB

    from .routes.routes import main

    app.register_blueprint(main)

    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])

    return app


# import os
# from flask import Flask
# from app.routes.routes import main

# def create_app():
#     app = Flask(__name__)

#     # Buat folder uploads jika belum ada
#     os.makedirs("uploads", exist_ok=True)

#     app.config["UPLOAD_FOLDER"] = "uploads"

#     app.register_blueprint(main)

#     return app
