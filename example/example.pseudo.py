
class Reifen:
    def __init__(self, Hersteller, Bemerkung=None, Druck=None):
        self.validate_Hersteller(Hersteller)
        self.validate_Bemerkung(Bemerkung)
        self.validate_Druck(Druck)
        self._Hersteller = Hersteller
        self._Bemerkung = Bemerkung
        self._Lookup = ('mtb', 'strasse', 'trekking')
        self._Druck = Druck

    @property
    def Hersteller(self):
        return self._Hersteller

    @property
    def Bemerkung(self):
        return self._Bemerkung

    @property
    def Lookup(self):
        return self._Lookup

    @property
    def Druck(self):
        return self._Druck

    @Hersteller.setter
    def Hersteller(self, value):
        self.validate_Hersteller(value)
        self._Hersteller = value

    @Bemerkung.setter
    def Bemerkung(self, value):
        self.validate_Bemerkung(value)
        self._Bemerkung = value

    @Druck.setter
    def Druck(self, value):
        self.validate_Druck(value)
        self._Druck = value

    def validate_Hersteller(self, value):
        if value is None:
            raise AttributeError()
        if not isinstance(value, str):
            raise AttributeError()
        if len(value) > 40:
            raise AttributeError()

    def validate_Bemerkung(self, value):
        if value is not None:
            if not isinstance(value, str):
                raise AttributeError()
            if len(value) > 80:
                raise AttributeError()

    def validate_Druck(self, value):
        if value is not None:
            if not isinstance(value, float):
                raise AttributeError()
            if value < 0.0 or value > 10.0:
                raise AttributeError()


class Velo:
    def __init__(self, Position, RahmenHoehe, Vorderrad=None, Hinterrad=None):

        self._Position = Position
        # Composition
        self._Rahmen = Rahmen(RahmenHoehe)
        # Aggregation/Association
        self._Vorderrad = Vorderrad
        # Aggregation/Association
        self._Hinterrad = Hinterrad

    @property
    def Position(self, value):
        return self._Position

    @Position.setter
    def Position(self, value):
        self.validate_Position(value)
        # TODO: Set value in the respect of circular data type!
        self._Position = value

    def validate_Position(self, value):
        if value is None:
            raise AttributeError()
        if not isinstance(value, list):
            raise AttributeError()
        if len(value) != 3:
            raise AttributeError()
        if value[0] < -90.0 or value[0] > 90.0:
            raise AttributeError()
        if value[1] < -90.0 or value[1] > 359.99999:
            raise AttributeError()
        if value[0] < -2000.0 or value[0] > 9000.0:
            raise AttributeError()


class Rahmen:
    def __init__(self, Hoehe):
        self.validate_Hoehe(Hoehe)
        self._Hoehe = Hoehe

    @property
    def Hoehe(self):
        return self._Hoehe

    @Hoehe.setter
    def Hoehe(self, value):
        self.validate_Hoehe(value)
        self._Hoehe = value

    def validate_Hoehe(self, value):
        if value is None:
            raise AttributeError()
        if not isinstance(value, int):
            raise AttributeError()
        if value < 10 and value > 80:
            raise AttributeError()
