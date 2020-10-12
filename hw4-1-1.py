# Kyle Bautista (AMDG) 10/12/20

team1win = int(input("How many wins for team 1? "))
team1draw = int(input("How many draws for team 1? "))
team1loss = int(input("How many losses for team 1? "))

team2win = int(input("How many wins for team 2? "))
team2draw = int(input("How many draws for team 2? "))
team2loss = int(input("How many losses for team 2? "))

if ((team1win * 3) + team1draw) > ((team2win * 3) + team2draw):
    print("Team 1 wins!")
else:
    print("Team 2 wins!")
