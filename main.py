from abc import ABC, abstractmethod


class Animal(ABC):
    hunger_status = 'хочет кушать'
    collect_status = ''
    # или 'Сыт(а)', если уже кормили
    weight = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = float(weight)  # кг

    @abstractmethod
    def feed(self):
        pass
        # self.hunger_status = 'Сыт(а)'

    @abstractmethod
    def collect(self):
        pass


class Bird(Animal):
    __name = ''
    collect_status = 'пора собирать яйца!'

    # или 'Яиц нет :(', если яиц нет

    def feed(self):
        self.hunger_status = 'сыт(а)'

    def collect(self):
        self.collect_status = 'яиц нет'


class Goose(Bird, Animal):
    __name = ''
    __voice = 'га-га-га!'


class Chicken(Bird, Animal):
    __name = ''
    __voice = 'клак, клак, КЛААААК!'


class Duck(Bird, Animal):
    __name = ''


class Milky(Animal):
    collect_status = 'пора доить!'

    # или 'Пока молока нет', если недавно доили

    def feed(self):
        self.hunger_status = 'сыт(а)'

    def collect(self):
        self.collect_status = 'молока нет'


class Cow(Milky, Animal):
    __name = ''
    __voice = 'мууу'


class Bleat(Animal):
    __voice = 'бэээ...мэээ'

    def feed(self):
        self.hunger_status = 'сыт(а)'


class Goat(Milky, Bleat, Animal):
    __name = ''


class Sheep(Bleat, Animal):
    __name = ''
    collect_status = 'пора стричь!'

    # или 'Шерсть ещё не отросла', если острижена

    def collect(self):
        self.collect_status = 'шерсть ещё не отросла'


def total_weight():
    total_weight = sum(name_plus_weight.values())
    print(f'Общий вес всех животных: {total_weight}')


def max_weight():
    max_value = max(name_plus_weight.values())
    for heaviest_animal, heaviest_weight in name_plus_weight.items():
        if heaviest_weight == max_value:
            print(f'Самое тяжелое животное на ферме - '
                  f'это {heaviest_animal} весом {heaviest_weight} кг!')


def animal_status():
    for animal in animals_list:
        print('{} {} и {}...'
              .format(animal.name,
                      animal.hunger_status,
                      animal.collect_status))


def main():
    print()
    print('Добро пожаловать на ферму!')
    print()
    print('s - проверить животных')
    print('f - покормить животных')
    print('c - собрать яйца / шерсть / подоить')
    print('tw - узнать вес всех животных')
    print('mw - узнать кто больше всех весит')
    print('q - уйти с фермы')
    while True:
        print()
        user_input = input('Что делаем? ')
        print()
        if user_input == 's':
            animal_status()
        elif user_input == 'f':
            for animal in animals_list:
                animal.feed()
            print('Животные покормлены!')
        elif user_input == 'c':
            for animal in animals_list:
                animal.collect()
            print('Всё собрали!')
        elif user_input == 'tw':
            total_weight()
        elif user_input == 'mw':
            max_weight()
        elif user_input == 'q':
            print('До встречи!')
            break
        else:
            print('Некорректная команда :(')


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

animals_list = [goose_1, goose_2,
                cow,
                sheep_1, sheep_2,
                chicken_1, chicken_2,
                goat_1, goat_2,
                duck]

name_plus_weight = {goose_1.name: goose_1.weight,
                    goose_2.name: goose_2.weight,
                    cow.name: cow.weight,
                    sheep_1.name: sheep_1.weight,
                    sheep_2.name: sheep_2.weight,
                    chicken_1.name: chicken_1.weight,
                    chicken_2.name: chicken_2.weight,
                    goat_1.name: goat_1.weight,
                    goat_2.name: goat_2.weight,
                    duck.name: duck.weight}

if __name__ == "__main__":
    main()
