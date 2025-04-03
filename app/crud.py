# Ten plik służy do testowania operacji CRUD (Create, Read, Update, Delete) na modelu Peak,
# poza kontekstem aplikacji webowej (czyli bez uruchamiania serwera Flask)
# uruchamy go poleceniem: python -m app.crud

from app import create_app, db
from app.models import Peak
import os
import csv


# Tworzymy aplikację Flask za pomocą fabryki
app = create_app()

# Wchodzimy w kontekst aplikacji – wymagane, by móc korzystać z bazy danych i innych rozszerzeń
# Alternatywa: można użyć .push(), ale forma with ... jest bezpieczniejsza i czytelniejsza
with app.app_context():

    # Funkcja do dodania kilku przykładowych szczytów, jeśli baza jest pusta
    def add_new_peaks():
        peaks = [
            Peak(name="Wielki Kopieniec", height=1328, voivodeship="Małopolskie", pasmo="Tatry Wysokie", is_kgp=False),
            Peak(name="Jaworzyna Krynicka", height=1114, voivodeship="Małopolskie", pasmo="Beskid Sądecki", is_kgp=False),
            Peak(name="Nosal", height=1206, voivodeship="Małopolskie", pasmo="Tatry Zachodnie", is_kgp=False)
        ]
        added = len(peaks)
        db.session.add_all(peaks)
        db.session.commit()
        print(f"Dodano {added} nowe szczyty.")

    # Funkcja do wypisania szczytów z bazy
    def show_peaks():
        peaks = Peak.query.order_by(Peak.height.desc()).all()
        print("Lista szczytów:")
        for peak in peaks:
            print(f"- {peak.name} ({peak.height} m) - {peak.voivodeship}, {peak.pasmo}")
            
        print("\nSzczyty powyżej 2000 m:")
        high_peaks = Peak.query.filter(Peak.height > 2000).all()
        for peak in high_peaks:
            print(f"{peak.name} ({peak.height} m)")
            
    # Funkcja do usuwania wskazanych szczytów z bazy
    def delete_custom_peaks():
        # Lista nazw gór do usunięcia
        to_delete = ["Nosal", "Wielki Kopieniec", "Jaworzyna Krynicka"]
        deleted_count = 0

        for name in to_delete:
            peak = Peak.query.filter_by(name=name).first() # Daj jeden rekord nie listę
            if peak:
                db.session.delete(peak)
                deleted_count += 1

        db.session.commit()
        print(f"Usunięto {deleted_count} szczytów.")

    # Funkcja do wczytywania danych szczytów z pliku CSV
    def import_peaks_from_csv():
        from .models import Peak

        if Peak.query.count() == 0:  # jeśli baza jest pusta – załaduj dane
            print("Importuję dane z peaks.csv...")

            filepath = os.path.join(os.path.dirname(__file__), '..', 'data', 'peaks.csv')
            try:
                with open(filepath, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        peak = Peak(
                            name=row['name'],
                            height=int(row['height']),
                            voivodeship=row['voivodeship'],
                            pasmo=row['pasmo'],
                            is_kgp=row['is_kgp'].strip().lower() == 'true'
                        )
                        db.session.add(peak)
                    db.session.commit()
                    print("Zaimportowano szczyty.")
            except FileNotFoundError:
                print("Nie znaleziono pliku peaks.csv. Pomijam import.")

    
    # Uruchom funkcje testowe
    if __name__ == '__main__':
        import_peaks_from_csv()
        add_new_peaks()
        # delete_custom_peaks()
        show_peaks()


