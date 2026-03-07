import random

teams = {
    "LOUD": ["ERDE", "CAUANZIN", "VIRTYY", "LUKXO", "DARKER"],
    "MIBR": ["ASPAS", "TEX", "MAZINO", "VERNO", "ZEKKEN"],
    "FURIA": ["ALYM", "KOALANOOB", "EEIU", "ARTZIN", "NERVE"],
    "PAPER REX": ["D4V4I", "FORSAKEN", "SOMETHING", "INVY", "JINGG"]
}

score = {
    "LOUD": 0,
    "MIBR": 0,
    "FURIA": 0,
    "PAPER REX": 0
}


def save_score():
    file = open("scoreboard.txt", "w")

    for team, wins in score.items():
        file.write(team + ":" + str(wins) + "\n")

    file.close()


while True:

    print("\n=== VALORANT TOURNAMENT MENU ===")
    print("1 - Show teams")
    print("2 - Show players")
    print("3 - Simulate match")
    print("4 - Show scoreboard")
    print("5 - Save scoreboard")
    print("6 - Exit")

    option = input("Choose an option: ")

    if option == "1":

        print("\nTeams in the tournament:")
        for team in teams:
            print("-", team)

    elif option == "2":

        team_choice = input("Type the team name: ").upper()

        if team_choice in teams:

            print("\nPlayers from", team_choice)

            for player in teams[team_choice]:
                print("-", player)

        else:
            print("Team not found")

    elif option == "3":

        team1 = input("Team 1: ").upper()
        team2 = input("Team 2: ").upper()

        if team1 in teams and team2 in teams:

            winner = random.choice([team1, team2])
            print("\nWinner:", winner)

            score[winner] += 1

        else:
            print("Invalid teams")

    elif option == "4":

        print("\n=== SCOREBOARD ===")

        for team, wins in score.items():
            print(team, "-", wins, "wins")

    elif option == "5":

        save_score()
        print("Scoreboard saved to file!")

    elif option == "6":

        print("Exiting program...")
        break

    else:
        print("Invalid option")