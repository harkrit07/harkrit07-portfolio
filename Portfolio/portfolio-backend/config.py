# import os
# from dotenv import load_dotenv

# load_dotenv()  # reads .env if present

# class Config:
#     SQLALCHEMY_DATABASE_URI        = os.getenv("DATABASE_URL", "sqlite:///contacts.db")
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

#     # OPTIONAL email (leave blanks to disable)
#     MAIL_SERVER   = os.getenv("MAIL_SERVER", "smtp.gmail.com")
#     MAIL_PORT     = int(os.getenv("MAIL_PORT", 465))
#     MAIL_USERNAME = os.getenv("MAIL_USERNAME")      # blank disables emailing
#     MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
#     TO_EMAIL      = os.getenv("TO_EMAIL", MAIL_USERNAME)
