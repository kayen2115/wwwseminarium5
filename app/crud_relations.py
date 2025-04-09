# uruchamy poleceniem: python -m app.crud_relations.py

from app import create_app, db
from app.models import User, Peak, PeakEntry
from datetime import date


# Tworzymy aplikację Flask za pomocą fabryki
app = create_app()

# Wchodzimy w kontekst aplikacji – wymagane, by móc korzystać z bazy danych i innych rozszerzeń
# Alternatywa: można użyć .push(), ale forma with ... jest bezpieczniejsza i czytelniejsza
with app.app_context():
    # Dodaj użytkowników (jeśli nie istnieją)
    def add_users():
        user1 = User.query.filter_by(username="kasia").first() # FROM User SELECT * WHERE username = "kasia" LIMIT 1
        if not user1:
            user1 = User(username="kasia", email="kasia@example.com")
            db.session.add(user1)

        user2 = User.query.filter_by(username="arek").first()
        if not user2:
            user2 = User(username="arek", email="arek@example.com")
            db.session.add(user2)

        db.session.commit()
    
    # Dodaj wpisy o zdobytych szczytach (zależne od istniejących użytkowników i szczytów)
    def add_entries():
        kasia = User.query.filter_by(username="kasia").first()
        arek = User.query.filter_by(username="arek").first()

        rysy = Peak.query.filter_by(name="Rysy").first()
        sniezka = Peak.query.filter_by(name="Śnieżka").first()

        if not kasia or not arek or not rysy or not sniezka:
            print("Brakuje użytkowników lub szczytów w bazie.")
            return

        # Dodaj wpisy tylko jeśli jeszcze nie istnieją
        existing = PeakEntry.query.filter_by(user_id=kasia.id, peak_id=rysy.id).first()
        if not existing:
            entry1 = PeakEntry(user_id=kasia.id, peak_id=rysy.id, date=date(2024, 8, 10), notes="Super pogoda!")
            entry2 = PeakEntry(user_id=kasia.id, peak_id=sniezka.id, date=date(2024, 9, 2), notes="Mgła jak mleko.")
            entry3 = PeakEntry(user_id=arek.id, peak_id=rysy.id, date=date(2024, 8, 1), notes="Tłoczno!")
            entry4 = PeakEntry(user_id=arek.id, peak_id=sniezka.id, date=date(2024, 8, 2), notes="Piękne widoki.")

            db.session.add_all([entry1, entry2, entry3, entry4])
            db.session.commit()
            print("Dodano nowe wpisy o zdobytych szczytach.")
        
    def some_queries():
        # Przykład zapytania do bazy danych  
        rysy = Peak.query.filter_by(name="Rysy").first()
        for entry in rysy.entries:
            print(f"{entry.user.username} był/była na Rysach dnia {entry.date} ({entry.notes})")    
        
        kasia = User.query.filter_by(username="kasia").first()
        if kasia:
            print(f"\nWejścia użytkownika: {kasia.username}")
            for entry in kasia.entries:
                print(f"- {entry.peak.name} ({entry.date}) - {entry.notes}")
    
    if __name__ == '__main__':
        add_users()
        add_entries()
        some_queries()
