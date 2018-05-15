import sys
import io

import pytest

from bowling.joueur import Joueur
from bowling.partie import Partie


def test_score():
    j1 = Joueur("Patrick")
    j1.ajouter_score_manche((1, 2))
    j1.ajouter_score_manche((3, 4))

    j2 = Joueur("Bob")
    j2.ajouter_score_manche((1, 2))
    j2.ajouter_score_manche((5, 4))

    p = Partie([j1, j2])

    assert p.who_win() == "Bob"

def test_print():
    j1 = Joueur("Patrick")
    j1.ajouter_score_manche((1, 2))
    j1.ajouter_score_manche((3, 4))

    j2 = Joueur("Bob")
    j2.ajouter_score_manche((1, 2))
    j2.ajouter_score_manche((5, 4))

    p = Partie([j1, j2])

    capturedOutput = io.StringIO()                # Create StringIO object
    sys.stdout = capturedOutput                   #  and redirect stdout.
    p.print_score()                                   # Call unchanged function.
    sys.stdout = sys.__stdout__                   # Reset redirect.

    assert capturedOutput.getvalue() == "Patrick 10\nBob 12\n"

def test_score_one_player():
    j1 = Joueur("Patrick")
    j1.ajouter_score_manche((1, 2))
    j1.ajouter_score_manche((3, 4))

    p = Partie([j1])

    assert p.who_win() == "Patrick"

def test_print_one_player():
    j1 = Joueur("Patrick")
    j1.ajouter_score_manche((1, 2))
    j1.ajouter_score_manche((3, 4))

    p = Partie([j1])

    capturedOutput = io.StringIO()                # Create StringIO object
    sys.stdout = capturedOutput                   #  and redirect stdout.
    p.print_score()                                   # Call unchanged function.
    sys.stdout = sys.__stdout__                   # Reset redirect.

    assert capturedOutput.getvalue() == "Patrick 10\n"

def test_add_player():
    j1 = Joueur("Patrick")
    j1.ajouter_score_manche((1, 2))
    j1.ajouter_score_manche((3, 4))
    j1.ajouter_score_manche((3, 4))
    j1.ajouter_score_manche((3, 4))
    j1.ajouter_score_manche((3, 4))
    j1.ajouter_score_manche((3, 4))

    j2 = Joueur("Bob")
    j2.ajouter_score_manche((1, 2))
    j2.ajouter_score_manche((5, 4))
    j2.ajouter_score_manche((5, 4))
    j2.ajouter_score_manche((5, 4))
    j2.ajouter_score_manche((5, 4))
    j2.ajouter_score_manche((5, 4))

    p = Partie()
    p.add_player(j1)
    p.add_player(j2)

    assert p.who_win() == "Bob"