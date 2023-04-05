class BallPlayer:
    def __init__(self, nimi: str, number: int, goals: int, passes: int, minutes: int):
        self.nimi = nimi
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(nimi={self.nimi}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')

    

# Write your solution here
def most_goals(players : list):
    lista = sorted(players, key = lambda player: player.goals, reverse=True)
    return lista[0].nimi

def most_points(players):
    list = []
    for player in players:
        total_points = player.goals + player.passes
        list.append((player, total_points))
    
    lista = sorted(list, key = lambda player: player[1], reverse=True)
    return (lista[0][0].nimi,lista[0][0].number)

def least_minutes(players):
    list = []
    for player in players:
        list.append((player, player.minutes))
    
    lista = sorted(list, key = lambda player: player[1])
    return (lista[0][0])
