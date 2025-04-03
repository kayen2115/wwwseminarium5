# Importujemy instancję SQLAlchemy z pliku app/__init__.py (tam jest db = SQLAlchemy())
from . import db

# 🏔️ Model reprezentujący szczyt górski (tabelę w bazie danych)
class Peak(db.Model):
    __tablename__ = 'peaks'  # Nazwa tabeli w bazie. Jeśli pominiemy, zostanie użyta 'peak' (z CamelCase → snake_case)

    # Kolumna 'id' – klucz główny (primary key), czyli unikalny identyfikator każdego rekordu
    id = db.Column(db.Integer, primary_key=True)

    # Kolumna 'name' – nazwa szczytu, np. "Rysy"
    # String(100) oznacza maksymalnie 100 znaków, nullable=False oznacza: nie może być pusta
    name = db.Column(db.String(100), nullable=False)

    # Kolumna 'height' – wysokość w metrach, także wymagana
    height = db.Column(db.Integer, nullable=False)

    # Kolumna 'voivodeship' – województwo, np. "Małopolskie" (może być pusta)
    voivodeship = db.Column(db.String(100))

    # Kolumna 'pasmo' – pasmo górskie, np. "Tatry" (również może być pusta)
    pasmo = db.Column(db.String(100))

    # Kolumna 'is_kgp' – czy szczyt należy do Korony Gór Polski
    # Domyślnie True – bo większość szczytów będzie z KGP
    is_kgp = db.Column(db.Boolean, default=True)

    # Nowa kolumna  'kraj' (również może być pusta)
    kraj = db.Column(db.String(100))
    
    # Relacja: jeden szczyt może pojawić się w wielu wpisach użytkowników
    entries = db.relationship('PeakEntry', backref='peak', lazy=True)
    
    # Specjalna metoda – sposób reprezentacji obiektu podczas drukowania/debugowania
    def __repr__(self):
        return f"<Peak {self.name} ({self.height} m)>"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Relacja do PeakEntry (1 użytkownik → wiele wejść)
    entries = db.relationship('PeakEntry', backref='user', lazy=True)

class PeakEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    peak_id = db.Column(db.Integer, db.ForeignKey('peaks.id'), nullable=False)
    # Kolumna 'date' – data wejścia na szczyt
    date = db.Column(db.Date)
    notes = db.Column(db.Text)