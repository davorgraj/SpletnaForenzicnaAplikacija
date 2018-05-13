# -*- coding: utf-8 -*-


def check_hair_color(character):
    black = 'CCAGCAATCGC'
    brown = 'GCCAGTGCCG'
    orange = 'TTAGCTATCGC'
    if character.find(black) != -1:
        return "črno"
    elif character.find(brown) != -1:
        return "rjavo"
    elif character.find(orange) != -1:
        return "oranžno"
    else:
        return "neznano"


def check_face_shape(character):
    square = 'GCCACGG'
    round = 'ACCACAA'
    oval = 'AGGCCTCA'
    if character.find(square) != -1:
        return "kvadraten"
    elif character.find(round) != -1:
        return "okrogel"
    elif character.find(oval) != -1:
        return "ovalen"
    else:
        return "neznan"


def check_eyes_color(character):
    blue = 'TTGTGGTGGC'
    green = 'GGGAGGTGGC'
    brown = 'AAGTAGTGAC'
    if character.find(blue) != -1:
        return "modre"
    elif character.find(green) != -1:
        return "zelene"
    elif character.find(brown) != -1:
        return "rjave"
    else:
        return "neznane"


def check_gender(character):
    male = 'TGCAGGAACTTC'
    female = 'TGAAGGACCTTC'
    if character.find(male) != -1:
        return "moški"
    elif character.find(female) != -1:
        return "ženski"
    else:
        return "neznan"


def check_race(character):
    white = 'AAAACCTCA'
    black = 'CGACTACAG'
    asian = 'CGCGGGCCG'
    if character.find(white) != -1:
        return "bele"
    elif character.find(black) != -1:
        return "črne"
    elif character.find(asian) != -1:
        return "azijske"
    else:
        return "neznane"
