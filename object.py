

class Item:

    def __init__(self, date=None, time=None, place=None,
                 teamName=None, scored=None, missed=None):
        self.date = date
        self.time = time
        self.place = place
        self.teamName = teamName
        self.scored = scored
        self.missed = missed

    def __str__(self):
        return f'{self.date} , {self.time} , {self.place} , {self.teamName} , {self.scored} , {self.missed}'

