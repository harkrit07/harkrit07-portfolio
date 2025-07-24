# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from smtplib import SMTP_SSL
# import ssl
# import re
# from pathlib import Path
# from flask import send_from_directory, render_template
# from model import db, Contact  # ← POINTS TO models.py
# from config import Config


# app = Flask(__name__)
# app.config.from_object(Config)

# CORS(app, resources={r"/api/*": {"origins": "*"}})

# FRONTEND_DIR = Path(__file__).resolve().parent.parent
# # ---------- DB init ----------
# db.init_app(app)
# with app.app_context():
#     db.create_all()

# EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

# # ---------- Health ----------


# @app.route("/api/health", methods=["GET"])
# def health():
#     return jsonify({"status": "ok"}), 200


# @app.route("/")
# def root():
#     """Serve the main index.html"""
#     return send_from_directory(FRONTEND_DIR, "index.html")


# @app.route("/<path:asset>")
# def serve_assets(asset):
#     # any other path (css, images, js) -> same directory
#     return send_from_directory(FRONTEND_DIR, asset)

# # ---------- Contact ----------


# @app.route("/api/contact", methods=["POST"])
# def contact():
#     data = request.get_json(force=True) or {}

#     # 1. Validate
#     name = data.get("name", "").strip()
#     email = data.get("email", "").strip()
#     phone = data.get("phone", "").strip()
#     message = data.get("message", "").strip()

#     if not name or not email or not message:
#         return jsonify({"error": "Name, email, and message are required"}), 400
#     if not EMAIL_REGEX.match(email):
#         return jsonify({"error": "Invalid email format"}), 400

#     # 2. Save
#     db.session.add(Contact(name=name, email=email,
#                    phone=phone, message=message))
#     db.session.commit()

#     # 3. Email (optional)
#     try:
#         if Config.MAIL_USERNAME and Config.MAIL_PASSWORD:
#             _send_mail(name, email, phone, message)
#     except Exception as e:
#         app.logger.error("Mail error: %s", e)       # do not crash API

#     return jsonify({"status": "ok"}), 201


# def _send_mail(name, email, phone, message):
#     subject = f"Portfolio Contact: {name}"
#     body = f"""Name: {name}
# Email: {email}
# Phone: {phone}

# {message}
# """
#     msg = f"Subject: {subject}\n\n{body}"
#     context = ssl.create_default_context()
#     with SMTP_SSL(Config.MAIL_SERVER, Config.MAIL_PORT, context=context) as smtp:
#         smtp.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
#         smtp.sendmail(Config.MAIL_USERNAME, Config.TO_EMAIL, msg)


# # ---------- Run ----------
# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)


# app.py  – stays in portfolio-backend/  (or wherever it already lives)
# from pathlib import Path
# import os
# import re
# import ssl
# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# from smtplib import SMTP_SSL

# from model import db, Contact
# from config import Config

# # ──────────────────────────────────────────────────
# #  🔸  create app & serve *frontend* from the repo root
# #      (index.html, style.css, images/, … all live there)
# # ──────────────────────────────────────────────────
# # one level up from backend dir
# REPO_ROOT = Path(__file__).resolve().parent.parent
# # point to the folder that holds index.html
# FRONT_FILES = REPO_ROOT

# app = Flask(__name__,
#             # let Flask find *.css / images automatically
#             static_folder=str(FRONT_FILES),
#             static_url_path="")                        # so  /style.css   just works

# app.config.from_object(Config)
# CORS(app, resources={r"/api/*": {"origins": "*"}})

# # ─── DB ─────────────────────────────────────────────
# db.init_app(app)
# with app.app_context():
#     db.create_all()

# EMAIL_RE = re.compile(r"[^@]+@[^@]+\.[^@]+")

# # ─── HEALTH ─────────────────────────────────────────


# @app.route("/api/health")
# def health():
#     return {"status": "ok"}, 200


# # ─── FRONTEND  ( /  +  any asset that isn't /api/* ) ─
# @app.route("/")
# def index():
#     return send_from_directory(FRONT_FILES, "index.html")


# @app.route("/<path:path>")
# def static_proxy(path):
#     """
#     Anything that’s not /api/* is treated as a static asset request
#     (style.css, images/xxx.png, script.js, …)
#     """
#     return send_from_directory(FRONT_FILES, path)


# # ─── CONTACT API ────────────────────────────────────
# @app.route("/api/contact", methods=["POST"])
# def contact():
#     payload = request.get_json(force=True) or {}

#     name, email, phone, message = (
#         payload.get("name", "").strip(),
#         payload.get("email", "").strip(),
#         payload.get("phone", "").strip(),
#         payload.get("message", "").strip()
#     )

#     if not (name and email and message):
#         return {"error": "Name, email and message are required."}, 400
#     if not EMAIL_RE.match(email):
#         return {"error": "Invalid email format."}, 400

#     db.session.add(Contact(name=name, email=email,
#                    phone=phone, message=message))
#     db.session.commit()

#     if Config.MAIL_USERNAME and Config.MAIL_PASSWORD:
#         try:
#             _send_mail(name, email, phone, message)
#         except Exception as exc:
#             app.logger.error("Mail error: %s", exc)

#     return {"status": "ok"}, 201


# def _send_mail(name, email, phone, message):
#     subject = f"Portfolio Contact: {name}"
#     body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}"
#     msg = f"Subject: {subject}\n\n{body}"

#     with SMTP_SSL(Config.MAIL_SERVER, Config.MAIL_PORT, context=ssl.create_default_context()) as smtp:
#         smtp.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
#         smtp.sendmail(Config.MAIL_USERNAME, Config.TO_EMAIL, msg)


# # ─── LOCAL / RENDER ENTRYPOINT ──────────────────────
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))           # Render injects PORT
#     app.run(host="0.0.0.0", port=port, debug=True)


from flask import Flask, send_from_directory, render_template

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')  # Your HTML with the button

# @app.route('/download-cv')
# def download_cv():
#     return send_from_directory('static', 'pdf/cv.pdf', as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
