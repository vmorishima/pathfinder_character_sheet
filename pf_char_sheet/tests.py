from django.test import TestCase
from .models import Character

# Create your tests here.
class TestStats(TestCase):
    def setUp(self):
        # we make a character
        Character.objects.create(
            name='test', character_class='test', alignment='N', gender='f', race='n'
        )

    def test_ability_modifier_10(self):
        c = Character.objects.get(name='test')
        c.STR = 10
        assert c.calculate_ability_modifier(c.STR) == 0

    def test_ability_modifier_11(self):
        c = Character.objects.get(name='test')
        c.STR = 11
        assert c.calculate_ability_modifier(c.STR) == 0

    def test_ability_modifier_12(self):
        c = Character.objects.get(name='test')
        c.STR = 12
        assert c.calculate_ability_modifier(c.STR) == 1

    def test_ability_modifier_9(self):
        c = Character.objects.get(name='test')
        c.STR = 9
        assert c.calculate_ability_modifier(c.STR) == -1

    def test_ability_modifier_8(self):
        c = Character.objects.get(name='test')
        c.STR = 8
        assert c.calculate_ability_modifier(c.STR) == -1

    def test_ability_modifier_1(self):
        c = Character.objects.get(name='test')
        c.STR = 1
        assert c.calculate_ability_modifier(c.STR) == -5

    def test_cmd(self):
        c = Character.objects.get(name='test')
        c.BAB = 1
        c.STR = 13
        c.DEX = 15
        c.size = 'c'
        assert c.CMD == 6

    def test_size_f(self):
        c = Character.objects.get(name='test')
        c.size = 'f'
        assert c.size_modifier == 8

    def test_size_d(self):
        c = Character.objects.get(name='test')
        c.size = 'd'
        assert c.size_modifier == 4

    def test_size_t(self):
        c = Character.objects.get(name='test')
        c.size = 't'
        assert c.size_modifier == 2

    def test_size_s(self):
        c = Character.objects.get(name='test')
        c.size = 's'
        assert c.size_modifier == 1

    def test_size_m(self):
        c = Character.objects.get(name='test')
        c.size = 'm'
        assert c.size_modifier == 0

    def test_size_l(self):
        c = Character.objects.get(name='test')
        c.size = 'l'
        assert c.size_modifier == -1

    def test_size_h(self):
        c = Character.objects.get(name='test')
        c.size = 'h'
        assert c.size_modifier == -2

    def test_size_g(self):
        c = Character.objects.get(name='test')
        c.size = 'g'
        assert c.size_modifier == -4

    def test_size_c(self):
        c = Character.objects.get(name='test')
        c.size = 'c'
        assert c.size_modifier == -8