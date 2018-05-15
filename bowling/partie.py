class Partie:

    def __init__(self, list_player=None):
        if list_player is None:
            self.list_player = []
        else:
            self.list_player = list_player

    def who_win(self):
        playerid_score = (0, 0)
        for id in range(len(self.list_player)):
            score_adv = self.list_player[id].calculer_score()
            if playerid_score[1] <= score_adv:
                playerid_score = (id, score_adv)
        return self.list_player[playerid_score[0]].nom

    def add_player(self, joueur):
        self.list_player.append(joueur)

    def print_score(self):
        for player in self.list_player:
            print('%s %d' % (player.nom, player.calculer_score()))
