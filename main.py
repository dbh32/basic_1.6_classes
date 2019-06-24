class Animal:
    hunger_status = 'Нужно покормить!'
    # или 'Сыт(а)', если уже кормили
    weight = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = float(weight)  # кг

    def feed(self):
        self.hunger_status = 'Сыт(а)'


class Bird(Animal):
    __name = ''
    eggs_status = 'Время собирать яйца!'

    # или 'Яиц нет :(', если яиц нет

    def eggs_collect(self):
        self.eggs_status = 'Яиц нет :('


class Goose(Bird, Animal):
    __name = ''
    __voice = 'Га-га-га!'


class Chicken(Bird, Animal):
    __name = ''
    __voice = 'клак, клак, КЛААААК!'


class Duck(Bird, Animal):
    __name = ''


class Milky(Animal):
    milk_status = 'Пора доить!'

    # или 'Пока молока нет', если недавно доили

    def milk_collect(self):
        self.milk_status = 'Пока молока нет'


class Cow(Milky, Animal):
    __name = ''
    __voice = 'Мууу'


class Bleat(Animal):
    __voice = 'Бэээ...Мэээ'


class Goat(Milky, Bleat, Animal):
    __name = ''


class Sheep(Bleat, Animal):
    __name = ''
    __wool_status = 'Пора стричь!'
    # или 'Шерсть ещё не отросла', если острижена


goose_1 = Goose('Серый', 9.2)
goose_2 = Goose('Белый', 7.5)
cow = Cow('Манька', 478)
sheep_1 = Sheep('Барашек', 44.5)
sheep_2 = Sheep('Кудрявый', 72.1)
chicken_1 = Chicken('Ко-Ко', 1)
chicken_2 = Chicken('Кукареку', 1.3)
goat_1 = Goat('Рога', 42)
goat_2 = Goat('Копыта', 37.5)
duck = Duck('Кряква', 4.8)

name_plus_weight = {goose_1.name: goose_1.weight,
                    goose_2.name: goose_2.weight,
                    cow.name: cow.weight,
                    sheep_1.name: sheep_1.weight,
                    sheep_2.name: sheep_2.weight,
                    chicken_1.name: chicken_1.weight,
                    chicken_2.name: chicken_2.weight,
                    goat_1.name: goat_1.weight,
                    goat_2.name: goat_2.weight,
                    duck.name: duck.weight
                    }

total_weight = sum(name_plus_weight.values())
print(f'Общий вес всех животных: {total_weight}')

max_value = max(name_plus_weight.values())
for heaviest_animal, heaviest_weight in name_plus_weight.items():
    if heaviest_weight == max_value:
        print(f'Самое тяжелое животное на ферме - '
              f'это {heaviest_animal} весом {heaviest_weight} кг!')
