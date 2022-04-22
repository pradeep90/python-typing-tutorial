# Basic creature types

import random

from typing import Union, List

class Creature:
    def __init__(self, name):
        self.name = name

    def meet(self, other):
        pass


class Person(Creature):
    def __init__(self, name: str) -> None:
        self.name = name
        self.pets = []
        self.friends = []

    def adopt(self, pet: Union[Cat, Dog]) -> None:
        self.pets.append(pet)


class Cat(Creature):
    def __init__(self, name: str) -> None:
        self.name = name
        self.friends = []
        self.enemies = []

    def make_friend(self, friend: Union[Person, Dog]) -> None:
        self.friends.append(friend)

    def make_enemy(self, enemy: Union[Person, Cat, Dog]) -> None:
        self.enemies.append(enemy)

    def meet(self, other: Union[Person, Cat, Dog]) -> None:
        if random.random() < 0.5:
            self.make_friend(other)
        else:
            self.make_enemy(other)


class Dog(Creature):
    def __init__(self, name: str) -> None:
        self.name = name
        self.friends = []
        self.enemies = []

    def make_friend(self, friend: Union[Person, Cat, Dog]) -> None:
        self.friends.append(friend)

    def meet(self, other: Union[Person, Cat, Dog]) -> None:
        self.make_friend(other)
