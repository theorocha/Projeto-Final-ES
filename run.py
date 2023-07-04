from app import app,db
from app.models.tables import User

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

