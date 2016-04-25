from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from random import randint
from math import floor

# Create your models here.

@python_2_unicode_compatible
class Character(models.Model):
    # Basic profile
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    character_class = models.CharField(max_length=50)
    alignment_choices = (
        ('LG', 'Lawful Good'),
        ('NG', 'Neutral Good'),
        ('CG', 'Chaotic Good'),
        ('LN', 'Lawful Neutral'),
        ('N', 'True Neutral'),
        ('CN', 'Chaotic Neutral'),
        ('LE', 'Lawful Evil'),
        ('NE', 'Neutral Evil'),
        ('CE', 'Chaotic Evil')
    )
    alignment = models.CharField(max_length=2, choices=alignment_choices)
    gender = models.CharField(max_length=50)
    race = models.CharField(max_length=75)
    size_choices = {
        ('f', 'Fine'),
        ('d', 'Diminutive'),
        ('t', 'Tiny'),
        ('s', 'Small'),
        ('m', 'Medium'),
        ('l', 'Large'),
        ('h', 'Huge'),
        ('g', 'Gargantuan'),
        ('c', 'Colossal')
    }
    size = models.CharField(max_length=1, choices=size_choices, default='m')
    #char_img = models.ImageField()

    # Stats
    def calculate_ability_modifier(self, ability):
        return int(floor((ability-10)/2.0))

    STR = models.IntegerField(default=10)
    DEX = models.IntegerField(default=10)
    CON = models.IntegerField(default=10)
    CHA = models.IntegerField(default=10)
    INT = models.IntegerField(default=10)
    WIS = models.IntegerField(default=10)

    def _get_str_modifier(self):
        return self.calculate_ability_modifier(self.STR)
    str_modifier = property(_get_str_modifier)

    def _get_dex_modifier(self):
        return self.calculate_ability_modifier(self.DEX)
    dex_modifier = property(_get_dex_modifier)

    def _get_con_modifier(self):
        return self.calculate_ability_modifier(self.CON)
    con_modifier = property(_get_con_modifier)

    def _get_cha_modifier(self):
        return self.calculate_ability_modifier(self.CHA)
    cha_modifier = property(_get_cha_modifier)

    def _get_int_modifier(self):
        return self.calculate_ability_modifier(self.INT)
    int_modifier = property(_get_int_modifier)

    def _get_wis_modifier(self):
        return self.calculate_ability_modifier(self.WIS)
    wis_modifier = property(_get_wis_modifier)

    HP = models.IntegerField(default=10)
    FORT = models.IntegerField(default=10)
    WILL = models.IntegerField(default=10)
    REFLEX = models.IntegerField(default=10)

    def _get_fort_save(self):
        return self.FORT + self.calculate_ability_modifier(self.CON)
    fort_save = property(_get_fort_save)

    def _get_will_save(self):
        return self.WILL + self.calculate_ability_modifier(self.WIS)
    will_save = property(_get_will_save)

    def _get_reflex_save(self):
        return self.REFLEX + self.calculate_ability_modifier(self.DEX)
    reflex_save = property(_get_reflex_save)

    BAB = models.IntegerField(default=10)

    def get_absolute_url(self):
        return '/%i/' % self.id

    def __str__(self):
        return self.name

    def _get_size_modifier(self):
        if self.size == 'c':
            return -8
        elif self.size == 'g':
            return -4
        elif self.size == 'h':
            return -2
        elif self.size == 'l':
            return -1
        elif self.size == 'm':
            return 0
        elif self.size == 's':
            return 1
        elif self.size == 't':
            return 2
        elif self.size == 'd':
            return 4
        elif self.size == 'f':
            return 8
    size_modifier = property(_get_size_modifier)

    def _get_cmb(self):
        return self.BAB + self.calculate_ability_modifier(self.STR) + self.size_modifier
    CMB = property(_get_cmb)

    def _get_cmd(self):
        return self.BAB + self.calculate_ability_modifier(self.STR) + self.calculate_ability_modifier(self.DEX) + self.size_modifier + 10
    CMD = property(_get_cmd)


    def roll_d20(self):
        return randint(1,20)