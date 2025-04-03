🌐 Projekt "Korona Gór Polski" – Flask + SQLite

Ten projekt stanowi bazę do zajęć praktycznych dla studentów II roku kierunku Teleinformatyka na AGH.
W ramach kursu studenci uczą się podstaw obsługi relacyjnych baz danych w aplikacjach webowych z wykorzystaniem Flaska, SQLAlchemy i blueprintów.

🔄 Cel projektu

Projekt pokazuje, jak stworzyć aplikację internetową umożliwiającą:
    zarządzanie bazą danych szczytów Korony Gór Polski,
    rejestrowanie użytkowników i zdobytych przez nich gór,
    korzystanie z REST API i systemu szablonów HTML (Jinja2),
    rozdzielenie aplikacji na blueprinty: home, user_api, users

📂 Struktura projektu (fragment)

korona/
├── app/
│   ├── __init__.py          # fabryka aplikacji Flask
│   ├── models.py            # definicje tabel (User, Peak, PeakEntry)
│   ├── crud.py              # inicjacja tabeli Peak, przykładowe operacjie CRUD
│   ├── crud_relations.py    # inicjacja tabel User i PeakEntry, przykładowe operacjie CRUD
│   ├── home/                # blueprint: strona główna
│   ├── user_api/            # blueprint wykorzystujący REST API
│   ├── users/               # blueprint wykorzystujący renderowanie szablonów
│   ├── static/              # pliki CSS
│   └── templates/           # szablony HTML
├── instance/korona.db       # plik bazy danych SQLite
├── config.py                # konfiguracja Flask
├── run.py                   # uruchamianie aplikacji
├── requirements.txt         # zależności Pythona

🚀 Jak uruchomić projekt lokalnie

Stwórz środowisko wirtualne:

python -m venv venv
source venv/bin/activate      # (Linux/macOS)
venv\Scripts\activate         # (Windows)

Zainstaluj zależności:
pip install -r requirements.txt

Uruchom aplikację:
python run.py
Wejdź na: http://127.0.0.1:5000

Uruchamianie testowych aplikacji:
python -m app.crud
python -m app.crud_relations


📊 Tematy edukacyjne

W ramach projektu studenci poznają m.in.:
    relacyjne bazy danych i ORM (SQLAlchemy),
    migracje schematu (Flask-Migrate),
    blueprinty i organizacja kodu,
    obsługa formularzy i przesyłanie plików,
    bezpieczeństwo danych i walidacja wejścia,
    budowa i wykorzystanie REST API (GET, POST).
Projekt udostępniony do celów edukacyjnych – nie zawiera danych wrażliwych i może być rozwijany przez studentów.
W razie pytań proszę kontaktować się z prowadzeniem zajęć.

