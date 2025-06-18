from abc import ABC, abstractmethod


class Character(ABC):
    """base class"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @classmethod
    @abstractmethod
    def die(cls):
        """function to die"""
        pass


class Stark(Character):
    """Your docstring for Class"""
    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
