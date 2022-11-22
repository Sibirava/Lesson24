from model.player import FootballPlayer

class Manager:
    @staticmethod
    def give_golden_ball(players):
        if not isinstance(players, (list, tuple)):
            return

        iplayer = 0
        for index in range(1, len(players)):
            current = players[index].goal * 2 + players[index].assist
            max = players[iplayer].goal * 2 + players[iplayer].assist

            if ((current > max)
                    or (current == max and players[index].goal > players[iplayer].goal)):
                iplayer = index

        return players[iplayer]