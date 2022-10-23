# FootballLeague

## **Features:**
+This program is simulating a single season each time
+Teams are based on Premiere League 22/23 season teams
+The program reads the text file of teams and appending to list which is using in program lately
+The program fixturing matches depends on "Round-robin tournament circle method"
+There is some attributes for teams like budget(it does not affect for now) and overall
+These attributes are affecting team wining chances.

#### Calculating Chances:
*Theses calculations can be silly because I made up all of it.*

(overall - 70) is overall_rate
total_overallrate = overall_rate1 + overall_rate2
tie_chance = total_overallrate * 1/(abs(overall_rate1 - overall_rate2) + 2)
all_chances = total_overallrate + tie_chance

team1_win = overall_rate1/all_chances * 100
team2_win = overall_rate2/all_chances * 100
tie = tie_chance/all_chances * 100

+After match, the program saves the results and points to database which made for teams.
(I did not add right now but at the end of season, the program will save the champion,2nd and third. Also team_dict.txt will be modified by end season standings not by alphabetic.)
