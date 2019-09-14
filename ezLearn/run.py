# Insert Run Command Here

from ezLearn.app import app
from ezLearn.app.models import db

# Insert code here for the online SQL database

if __name__ == "__main__":
    db.create_all()
    app.run()
