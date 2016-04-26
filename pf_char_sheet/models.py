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
    inventory = models.TextField(default="")
    GP = models.IntegerField(default=0)
    SP = models.IntegerField(default=0)
    CP = models.IntegerField(default=0)

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
    FORT = models.IntegerField(default=0, verbose_name="Base Fortitude")
    WILL = models.IntegerField(default=0, verbose_name="Base Will")
    REFLEX = models.IntegerField(default=0, verbose_name="Base Reflex")

    def _get_fort_save(self):
        return self.FORT + self.con_modifier
    fort_save = property(_get_fort_save)

    def _get_will_save(self):
        return self.WILL + self.wis_modifier
    will_save = property(_get_will_save)

    def _get_reflex_save(self):
        return self.REFLEX + self.dex_modifier
    reflex_save = property(_get_reflex_save)

    BAB = models.IntegerField(default=0, verbose_name="Base Attack Bonus")
    base_AC = models.IntegerField(default=0, verbose_name="Armor Bonuses")

    def _get_ac(self):
        return 10 + self.base_AC + self.size_modifier + self.dex_modifier
    AC = property(_get_ac)

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
        return self.BAB + self.str_modifier + self.size_modifier
    CMB = property(_get_cmb)

    def _get_cmd(self):
        return self.BAB + self.str_modifier + self.dex_modifier + self.size_modifier + 10
    CMD = property(_get_cmd)

    # SKILLS

    acrobatics = models.IntegerField(default=0)
    appraise = models.IntegerField(default=0)
    bluff = models.IntegerField(default=0)
    climb = models.IntegerField(default=0)
    diplomacy = models.IntegerField(default=0)
    disable_device = models.IntegerField(default=0)
    disguise = models.IntegerField(default=0)
    escape_artist = models.IntegerField(default=0)
    fly = models.IntegerField(default=0)
    handle_animal = models.IntegerField(default=0)
    heal = models.IntegerField(default=0)
    intimidate = models.IntegerField(default=0)
    knowledge_arcana = models.IntegerField(default=0)
    knowledge_dungeoneering = models.IntegerField(default=0)
    knowledge_engineering = models.IntegerField(default=0)
    knowledge_geography = models.IntegerField(default=0)
    knowledge_history = models.IntegerField(default=0)
    knowledge_nature = models.IntegerField(default=0)
    knowledge_nobility = models.IntegerField(default=0)
    knowledge_planes = models.IntegerField(default=0)
    knowledge_religion = models.IntegerField(default=0)
    linguistics = models.IntegerField(default=0)
    perception = models.IntegerField(default=0)
    ride = models.IntegerField(default=0)
    sense_motive = models.IntegerField(default=0)
    sleight_of_hand = models.IntegerField(default=0)
    spellcraft = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    swim = models.IntegerField(default=0)
    use_magic_device = models.IntegerField(default=0)