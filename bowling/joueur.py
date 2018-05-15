class Joueur:
    def __init__(self, nom="Bernard", tab=None):
        self.nom = nom
        if tab is None:
            self.changer_tableau_score([])
        else:
            self.changer_tableau_score(tab)

    def ajouter_score_manche(self, tuple):
        if tuple[0] < 0 or tuple[1] < 0 or tuple[0] + tuple[1] > 10:
            raise TypeError("tuple faux")
        if len(self.tableau_score) == 12:
            raise TypeError("tab > 12")
        if len(self.tableau_score) == 11:
            if self.tableau_score[9][0] != 10 or self.tableau_score[10][0] != 10:
                raise TypeError("tab>11")
            if tuple[1] != 0:
                raise TypeError("input error")
        if len(self.tableau_score) == 10:
            if self.tableau_score[9][0] + self.tableau_score[0][1] != 10:
                raise TypeError("tab > 10")
        self.tableau_score.append(tuple)
        return

    def changer_tableau_score(self, tab):
        if len(tab) > 12:
            raise TypeError("tab > 12")
        if len(tab) > 11 and (tab[9][0] != 10 or tab[10][0] != 10):
            raise TypeError("tab > 10")
        # parcourt du tableau et utilisation de la fonction ajouter_score_manche pour centraliser les regles
        self.tableau_score = []
        for tuple in tab:
            self.ajouter_score_manche(tuple)
        return

    def calculer_score(self):
        # if len(self.tableau_score) > 12:
        #    raise TypeError("tab > 12")
        # if len(self.tableau_score) > 11 and (self.tableau_score[9][0] != 10 or  self.tableau_score[10][0] != 10):
        #    raise TypeError("tab > 10")
        sum = 0
        multiplicateur1 = 1
        multiplicateur2 = 1

        nb_tour = 0
        for (x, y) in self.tableau_score:
            nb_tour += 1
            #    if x < 0 or y < 0 or x + y > 10:
            #        raise TypeError("value error")

            sum += multiplicateur1 * x + multiplicateur2 * y

            if nb_tour >= 10:
                multiplicateur1 = multiplicateur2
                multiplicateur2 = 1
            elif x == 10:
                multiplicateur1 = multiplicateur2 + 1
                multiplicateur2 = 2
            elif x + y == 10:
                multiplicateur1 = 2
                multiplicateur2 = 1
            else:
                multiplicateur1 = 1
                multiplicateur2 = 1
        return sum
