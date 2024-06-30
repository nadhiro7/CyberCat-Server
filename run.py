from waitress import serve
from app import app,db  # Import your Flask app here

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    serve(app, host='0.0.0.0', port=3800)
