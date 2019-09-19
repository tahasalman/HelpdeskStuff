from utils.util import true_or_false

# Dog Owners dictionary
# Key = Owner, Value = Dog
DOG_OWNERS = {
    'Frodo': 'Sam',
    'Robin': 'Ted',
    'Harry': 'Voldemort',
    'Gilmour': 'David'
}


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    @property
    def owner(self):
        '''
        sets self.owner to a string representing the owner of dog if exists otherwise None
        '''
        for owner_name, dog_name in DOG_OWNERS.items():
            if self.name == dog_name:
                return owner_name
        return None

    def owner_nearby(self):
        if not self.owner:
            return False
        return true_or_false()

    def talk(self, words):
        if self.owner_nearby():
            print(f'{self.name.upper()}: {Dog.encrypt(words)}')
        else:
            print(f'{self.name.upper()}: {words}')

    @staticmethod
    def encrypt(words):
        num_words = len(words.split())
        return 'WOOF ' * num_words


if __name__ == "__main__":
    dog = Dog("Sam")
    dog.talk(f'Hi my name is {dog.name}')

    dog = Dog("Rando")
    dog.talk(f'Hi my name is {dog.name}')

    dog = Dog('Voldemort')
    dog.talk("Let's take over the world!")