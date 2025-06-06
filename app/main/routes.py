# routes.py w blueprintcie main
from flask import render_template, request, redirect, url_for
from . import main
from app import db
from app.models import Budynek, Sala

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@main.route('/budynki', methods=['GET', 'POST'])
def budynki():
    # return "<h>Hello World</h>"
    if request.method == 'POST':
        nazwa = request.form['nazwa']
        adres = request.form['adres']
        nowy_budynek = Budynek(nazwa_budynku=nazwa, adres=adres)
        db.session.add(nowy_budynek)
        db.session.commit()
        return redirect(url_for('main.budynki'))

    wszystkie_budynki = Budynek.query.all()
    return render_template('budynki.html', budynki=wszystkie_budynki)


@main.route('/budynki/usun/<int:id>', methods=['POST'])
def usun_budynek(id):
    budynek = Budynek.query.get_or_404(id)
    db.session.delete(budynek)
    db.session.commit()
    return redirect(url_for('main.budynki'))

@main.route('/sale', methods=['GET', 'POST'])
def sale():
    # return "<h>Sale</h>"
    if request.method == 'POST':
        nazwa = request.form['nazwa']
        rodzaj = request.form['rodzaj']
        liczba_miejsc = request.form['liczba_miejsc']
        wyposazenie = request.form['wyposażenie']
        nazwa_budynku = request.form['nazwa_budynku']

        # Wyszukiwanie budynku po nazwie
        budynek = Budynek.query.filter_by(nazwa_budynku=nazwa_budynku).first()

        # TODO: Zmien ta instrukcje warunkowa tak, aby wyświetlała okienko
        #       z komunikatem "Budynek o takiej nazwie nie istnieje" i dawało
        #       możliwość wpisania jeszcze raz nazwy budynku.
        #       Ewentualnie można też dodać przycisk przegladaj budynki,
        #       żeby użytkownik miał możliwość zobaczenia budynkow, ktore ma do wyboru
        if not budynek:
            return "Budynek o takiej nazwie nie istnieje", 400

        nowa_sala = Sala(nazwa_sali=nazwa,
                         rodzaj_sali=rodzaj,
                         liczba_miejsc=liczba_miejsc,
                         wyposazenie=wyposazenie,
                         id_budynku=budynek.id_budynku)
        db.session.add(nowa_sala)
        db.session.commit()
        return redirect(url_for('main.sale'))
    wszystkie_sale = Sala.query.all()
    return render_template('sale.html', sale=wszystkie_sale)

@main.route('/sale/usun/<int:id>', methods=['POST'])
def usun_sale(id):
    sala = Sala.query.get_or_404(id)
    db.session.delete(sala)
    db.session.commit()
    return redirect(url_for('main.sale'))

# TODO-1: Dodaj widoki dla Ról, Użytkowników, Przedmiotów, Rezerwacji i Grup Cyklicznych
#       Każdy widok będzie miał dwie funkcje: pierwsza do wyświetlania tabeli i dodawania, druga
#       do usuwania rekordu.
# TODO-2: Nastepnie w pliku models.py trzeba dodać klasy które odzwierciedlają tabele z bazy danych
# TODO-3: Dla każdej encji trzeba stworzyć odpowiedni plik html, ktory bedzie renderowany w widoku
# TODO-4: Dodanie przycisku dla każdego widoku do powrotu na strone główną