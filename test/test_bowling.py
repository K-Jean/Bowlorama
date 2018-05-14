import pytest

from bowling.joueur import Joueur


def test_tuple():
    j1 = Joueur("Patrick")
    j1.ajouter_score_manche((1, 2))
    j1.ajouter_score_manche((3, 4))
    assert j1.calculer_score() == 10
    #assert function_somme_tupe([(1, 2), (3, 4)]) == 10


def test_limite_zero():
    j1 = Joueur("Patrick")
    j1.ajouter_score_manche((1, 0))
    assert j1.calculer_score() == 1
    #assert function_somme_tupe([(1, 0)]) == 1


def test_spare():
    j1 = Joueur("Patrick")
    j1.ajouter_score_manche((5, 5))
    j1.ajouter_score_manche((5, 2))
    assert j1.calculer_score() == 22
    #assert function_somme_tupe([(5, 5), (5, 2)]) == 22


def test_strike():
    j1 = Joueur()
    j1.ajouter_score_manche((10, 0))
    j1.ajouter_score_manche((5, 2))
    assert j1.calculer_score() == 24
    #assert function_somme_tupe([(10, 0), (5, 2)]) == 24


def test_chain_strike():
    j1 = Joueur("Patrick")
    j1.ajouter_score_manche((10, 0))
    j1.ajouter_score_manche((10, 0))
    j1.ajouter_score_manche((10, 0))
    j1.ajouter_score_manche((10, 0))
    j1.ajouter_score_manche((10, 0))
    j1.ajouter_score_manche((5, 2))
    assert j1.calculer_score() == 139
    #assert function_somme_tupe([(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (5, 2)]) == 139


def test_chain_strike_2():
    j1 = Joueur("TOTO")
    j1.ajouter_score_manche((10, 0))
    j1.ajouter_score_manche((10, 0))
    j1.ajouter_score_manche((10, 0))
    j1.ajouter_score_manche((2, 0))
    assert j1.calculer_score() == 66
#    assert function_somme_tupe([(10, 0), (10, 0), (10, 0), (2, 0)]) == 66


def test_full_strike():
    j1 = Joueur("Patrick")
    j1.changer_tableau_score([(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0),
         (10, 0)])
    assert j1.calculer_score() == 300
    #assert function_somme_tupe(
    #    [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0),
    #     (10, 0)]) == 300


def test_spare_coup():
    j1 = Joueur("Eric")
    j1.changer_tableau_score(
        [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (5, 5)])
    assert j1.calculer_score() == 285
    #assert function_somme_tupe(
    #    [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (5, 5)]) == 285


def test_limite_dix():
    j1 = Joueur("Eric",[(10,0)])
    assert j1.calculer_score() == 10
    #assert function_somme_tupe([(10, 0)]) == 10

def test_ajout_tuple_negatif():
    with pytest.raises(TypeError):
        j1 = Joueur("Titeuf")
        j1.ajouter_score_manche((1,-2))
        #function_somme_tupe([(1, -2), (3, 4)])

def test_ajout_tuple_hors_limite():
    with pytest.raises(TypeError):
        j1 = Joueur("Bertrand",[(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,0)])
        j1.ajouter_score_manche((2,3))

def test_changer_score_negatif():
    with pytest.raises(TypeError):
        j1 = Joueur("Kevin")
        j1.changer_tableau_score([(1,1),(-2,3),(4,4)])

def test_ajout_Joueur_score_negatif():
    with pytest.raises(TypeError):
        j1 = Joueur("Kevin",[(1,-1),(4,3)])

def test_ajout_Joueur_score_grand():
    with pytest.raises(TypeError):
        j1 = Joueur("Kevin",[(1,1),(4,3),(1,1),(4,3),(1,1),(4,3),(1,1),(4,3),(1,1),(4,0),(4,0),(3,0)])

def test_ajout_Joueur_score_grand2():
    with pytest.raises(TypeError):
        j1 = Joueur("Kevin",[(1,1),(4,3),(1,1),(4,3),(1,1),(4,3),(1,1),(4,3),(10,0),(10,0),(4,0),(4,0),(4,0)])

def test_ajout_score_grand():
    with pytest.raises(TypeError):
        j1 = Joueur("Patrick")
        j1.changer_tableau_score(
            [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0),
             (10, 0)])
        j1.ajouter_score_manche((10,0))

def test_ajout_score_error():
    with pytest.raises(TypeError):
        j1 = Joueur("Patrick")
        j1.changer_tableau_score(
            [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0),
             (5, 0)])
        j1.ajouter_score_manche((10,0))

def test_ajout_score_error2():
    with pytest.raises(TypeError):
        j1 = Joueur("Patrick")
        j1.changer_tableau_score(
            [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0),
             (10, 0)])
        j1.ajouter_score_manche((5,5))

#def test_nb_tuple_sup_douze():
#    with pytest.raises(TypeError):
#        function_somme_tupe(
#            [(1, 2), (3, 4), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2),
#             (1, 2), (1, 2), (1, 2)])


#def test_tuple_sup_dix():
#    with pytest.raises(TypeError):
#        function_somme_tupe([(1, 20), (3, 4)])


#def test_nb_tuple_sup_dix():
#    with pytest.raises(TypeError):
#        function_somme_tupe(
#            [(1, 3), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4), (3, 4)])
