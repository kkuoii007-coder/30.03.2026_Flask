from app import app, db

with app.app_context():
    db.create_all()  # Создаёт БД при первом запуске

if __name__ == '__main__':
    app.run(debug=True)