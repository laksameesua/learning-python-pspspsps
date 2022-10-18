gry = 'Gryffindor'
sly = 'Slytherin'
class student:
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house
        self.patronus = patronus

Harry = student('Harry', f'{gry}', 'Ott')
