from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

import os
import csv

# Tworzymy globalny obiekt bazy danych (SQLAlchemy), ale jeszcze nie powiązujemy go z aplikacją Flask.
db = SQLAlchemy()

# Fabryka aplikacji – funkcja, która tworzy i konfiguruje aplikację Flask
def create_app():
    # Tworzymy instancję aplikacji
    app = Flask(__name__)

    # Konfiguracja aplikacji (m.in. połączenie do bazy danych)
    app.config.from_object(Config)  # Wczytanie konfiguracji z pliku config.py

    # Inicjalizacja rozszerzenia SQLAlchemy (podpięcie bazy do aplikacji Flask)
    db.init_app(app)

    from . import models
    
    # Rejestracja nowych blueprintów
    from .home.routes import home_bp
    from .users.routes import user_bp
    from .user_api.routes import user_api_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(user_api_bp)
    CORS(app, origins=["http://127.0.0.1:5000"])  # konfiguracja CORS
    # 🔹 Konfiguracja CORS (Cross-Origin Resource Sharing)
    # 
    # Przeglądarki blokują domyślnie zapytania AJAX (np. fetch, axios) wysyłane do innego źródła (domeny/protokołu/portu),
    # niż to, z którego została załadowana strona. To mechanizm bezpieczeństwa na poziomie przeglądarki.
    #
    # Dzięki CORS możemy zezwolić wybranym źródłom (origins) na dostęp do naszego API.
    # W tym przypadku umożliwiamy tylko zapytania pochodzące z aplikacji działającej lokalnie
    # pod adresem http://127.0.0.1:5000 (czyli z naszej własnej strony lokalnej).
    #
    # Jest to ważne, gdy np. formularz HTML lub JavaScript próbuje pobrać dane z API (np. /api/user/<name>/entries).
    # Bez tego wpisu przeglądarka zablokowałaby taki dostęp (błąd CORS).
    #
    # UWAGA: w aplikacjach produkcyjnych powinno się podawać konkretną domenę, np. "https://mojastrona.pl",
    # a nie ogólne ustawienie CORS(app) zezwalające na wszystko.
    
    # Wchodzimy w kontekst aplikacji, aby móc używać zasobów aplikacji takich jak baza danych
    
    return app


