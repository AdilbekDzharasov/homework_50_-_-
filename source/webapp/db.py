import random
from random import randrange


class Cat:
    SLEEP_STAT = ['sleep', 'not sleeping']

    cat_dict = {
        'name': '',
        'age': 0,
        'happiness': 0,
        'satiety': 0,
        'state': random.choice(SLEEP_STAT)
    }

    @staticmethod
    def add(name):
        Cat.cat_dict['name'] = name
        Cat.cat_dict['age'] = randrange(1, 18)
        Cat.cat_dict['happiness'] = randrange(10, 100)
        Cat.cat_dict['satiety'] = randrange(10, 100)

    @staticmethod
    def feed():
        if Cat.cat_dict.get('state') == 'not sleeping':
            Cat.cat_dict['satiety'] += 15
            if Cat.cat_dict['satiety'] > 80:
                Cat.cat_dict['happiness'] -= 30
            else:
                Cat.cat_dict['happiness'] += 5
        else:
            return None

    @staticmethod
    def game():
        if Cat.cat_dict.get('state') == 'not sleeping':
            Cat.cat_dict['state'] = 'not sleeping'
            Cat.cat_dict['happiness'] -= 5
        else:
            Cat.cat_dict['happiness'] += 15
            Cat.cat_dict['satiety'] -= 10

    @staticmethod
    def state():
        if Cat.cat_dict.get('state') == 'not sleeping':
            Cat.cat_dict['state'] = 'sleep'
        else:
            Cat.cat_dict['state'] = 'not sleeping'

    @staticmethod
    def menu(action):
        if action == "game":
            Cat.game()
        elif action == "feed":
            Cat.feed()
        elif action == "state":
            Cat.state()

