# Write your solution here
import json


def read_data(file_name):
    with open(file_name, "r") as file:
        return json.load(file)


def search_by_name(data, name):
    for player in data:
        if player["name"] == name:
            return player
    return None


def list_teams(data):
    teams = sorted(set(player["team"] for player in data))
    return teams


def list_countries(data):
    countries = sorted(set(player["nationality"] for player in data))
    return countries


def players_in_team(data, team):
    return sorted([p for p in data if p["team"] == team], key=lambda x: (x["goals"] + x["assists"], x["goals"]), reverse=True)


def players_from_country(data, country):
    return sorted([p for p in data if p["nationality"] == country], key=lambda x: (x["goals"] + x["assists"], x["goals"]), reverse=True)


def most_points(data, n):
    return sorted(data, key=lambda x: (x["goals"] + x["assists"], x["goals"]), reverse=True)[:n]


def most_goals(data, n):
    return sorted(data, key=lambda x: (x["goals"], -x["games"]), reverse=True)[:n]


def print_player(player):
    print(f'{player["name"]:20} {player["team"]:3}  {player["goals"]:2} + {player["assists"]:2} = {player["goals"] + player["assists"]:3}')


file_name = input("file name: ")
data = read_data(file_name)
print(f"read the data of {len(data)} players")

print("\ncommands:")
print("0 quit")
print("1 search for player")
print("2 teams")
print("3 countries")
print("4 players in team")
print("5 players from country")
print("6 most points")
print("7 most goals")

while True:
    command = int(input("command: "))

    if command == 0:
        break
    elif command == 1:
        name = input("name: ")
        player = search_by_name(data, name)
        if player:
            print_player(player)
        else:
            print("Player not found.")
    elif command == 2:
        for team in list_teams(data):
            print(team)
    elif command == 3:
        for country in list_countries(data):
            print(country)
    elif command == 4:
        team = input("team: ")
        for player in players_in_team(data, team):
            print_player(player)
    elif command == 5:
        country = input("country: ")
        for player in players_from_country(data, country):
            print_player(player)
    elif command == 6:
        n = int(input("how many: "))
        for player in most_points(data, n):
            print_player(player)
    elif command == 7:
        n = int(input("how many: "))
        for player in most_goals(data, n):
            print_player(player)