import random
import time
import teams_database


def arrange_fixture():
    team_list = list()
    with open('team_dict.txt','r') as file:
            for line in file:
                team_list.append(line.strip())

    time.sleep(1)
    for i in range(38):
        
        print("Week {}".format(i + 1))
        for i in range(10):
            or_list = teams_database.League().return_or(team_list[i],team_list[19 - i])

            total_ovr = abs(or_list[0] + or_list[1])
            tie_chance = total_ovr * (1/((abs(or_list[0] - or_list[1])) + 2))
            all_chances = tie_chance + total_ovr

            chance = random.random()
            if (chance <= or_list[0]/all_chances):
                print("[W]{} - {}[L]".format(team_list[i],team_list[19 - i]))
                teams_database.League().increase_win(team_list[i])
                teams_database.League().increase_lose(team_list[19 - i])

            elif (or_list[0]/all_chances <= chance <= (or_list[1]/all_chances + or_list[0]/all_chances)):
                print("[L]{} - {}[W]".format(team_list[i],team_list[19 - i]))
                teams_database.League().increase_win(team_list[19 - i])
                teams_database.League().increase_lose(team_list[i])

            elif ((or_list[1]/all_chances + or_list[0]/all_chances) <= chance):
                print("[D]{} - {}[D]".format(team_list[i],team_list[19 - i]))
                teams_database.League().increase_draw(team_list[19 - i])
                teams_database.League().increase_draw(team_list[i])
        
        team_list.insert(1,team_list[19])
        team_list.pop(20)
        print("*********************************")
        time.sleep(0.3)
    teams_database.League().calculate_points()

while True:
    print("""
    ***********************************
    Welcome to Football League Program
    ***********************************
    [1] Simulate a season
    [2] Inspect all seasons
    [3] Quit
    ***********************************
    """)
    input1 = input("Please enter number which you want to select:")

    if (input1 == "1"):
        teams_database.League().reset_database()
        arrange_fixture()
    elif (input1 == "2"):
        pass
    elif (input1 == "3"):
        print("Leaving from program...")
        time.sleep(1)
        break
    else:
        print("Please enter right number.")
        time.sleep(1)