from __future__ import unicode_literals, absolute_import

from django.db import models


class Fruit(models.Model):

    def __str__(self):
        return "{0}".format(self.fruit_type())

    def fruit_type(self):
        if hasattr(self, 'apple'):
            return 'apple'
        elif hasattr(self, 'pineapple'):
            return 'pineapple'
        elif hasattr(self, 'membrillo'):
            return 'membrillo'
        else:
            return 'fruit'


class Apple(Fruit):
    pass


class Pineapple(Fruit):
    pass


class Membrillo(Fruit):
    pass


class Pen(models.Model):

    def __str__(self):
        return "pen"


class Fusion(models.Model):

    left_hand = models.ForeignKey(Fruit, related_name='in_left_hands')
    right_hand = models.ForeignKey(Pen, related_name='in_right_hands')

    def __str__(self):
        return "fusion {0} - {1}".format(self.left_hand, self.right_hand)

    def __unicode__(self):
        return u"fusion {0} - {1}".format(self.left_hand, self.right_hand)
