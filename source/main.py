def function_somme_tupe(tab):
    if len(tab) > 12:
        raise TypeError("tab > 12")
    if len(tab) > 10 and tab[9][0] != 10:
        raise TypeError("tab > 10")
    sum = 0
    multiplicateur1 = 1
    multiplicateur2 = 1

    nb_tour = 0
    for (x, y) in tab:
        nb_tour += 1
        if x < 0 or y < 0 or x + y > 10:
            raise TypeError("value error")

        sum += multiplicateur1 * x + multiplicateur2 * y

        if nb_tour >= 10:
            multiplicateur1 = multiplicateur2
            multiplicateur2 = 1
        elif x == 10:
            multiplicateur1 = multiplicateur2+1
            multiplicateur2 = 2
        elif x + y == 10:
            multiplicateur1 = 2
            multiplicateur2 = 1
        else:
            multiplicateur1 = 1
            multiplicateur2 = 1
    return sum
