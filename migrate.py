# migrate.py umieszczony w katalogu głównym projektu
# używając powershell należy ustawić zmienną środowiskową FLASK_APP na nazwę pliku: $env:FLASK_APP = "migrate.py
# można też ustawienie zmiannej doppisać do venv/Scripts/activate.bat

from flask_migrate import Migrate
from app import create_app, db
from app import models  # Flask-Migrate (Alembic) wykryje wszystkie modele w tym pliku

app = create_app()
migrate = Migrate(app, db)

# Wchodzimy w kontekst aplikacji – wymagane, by móc korzystać z bazy danych i innych rozszerzeń
if __name__ == '__main__':
    app.run()
    
# Kroki przeprowadzenia migracji:
# 1. pip install Flask-Migrate
# 2. Utwórz plik migrate.py z Migrate(app, db)
# 3. Uzywając powershell: ustaw FLASK_APP=migrate.py
# 4. powershell: flask db init       # raz
# 5. powershell: flask db migrate -m "Opis zmiany"
# 6. powershell: flask db upgrade