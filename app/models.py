from app import db

class Budynek(db.Model):
    __tablename__ = 'BUDYNKI'

    id_budynku = db.Column("ID_BUDYNKU",db.Integer, primary_key=True)
    nazwa_budynku = db.Column("NAZWA_BUDYNKU", db.String(30), nullable=False)
    adres = db.Column("ADRES", db.String(50), nullable=False)

    def __repr__(self):
        return f"<Budynek {self.nazwa_budynku}>"

class Sala(db.Model):
    __tablename__ = 'SALE'

    id_sali = db.Column("ID_SALI",db.Integer, primary_key=True)
    nazwa_sali = db.Column("NAZWA_SALI", db.String(30), nullable=False)
    rodzaj_sali = db.Column("RODZAJ_SALI", db.String(30), nullable=False)
    liczba_miejsc = db.Column("LICZBA_MIEJSC", db.Integer, nullable=False)
    wyposazenie = db.Column("WYPOSAŻENIE", db.String(200), nullable=False)
    id_budynku = db.Column(db.Integer, db.ForeignKey('BUDYNKI.ID_BUDYNKU'), nullable=False)

    budynek = db.relationship('Budynek', backref='sale')

    def __repr__(self):
        return f"<Sala {self.nazwa_sali}>"