from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """king class"""

    def set_eyes(self, eyes):
        """sets eyes"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """sets hairs"""
        self.hairs = hairs

    def get_eyes(self):
        """return eyes"""
        return (self.eyes)

    def get_hairs(self):
        """return hairs"""
        return (self.hairs)
