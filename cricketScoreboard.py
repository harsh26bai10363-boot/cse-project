def display_title():
    print("\n")
    print("=" * 60)
    print("                 CRICKET SCOREBOARD")
    print("=" * 60)
def display_menu():
    print("\n--------------- MAIN MENU ----------------")
    print("1. Add Player")
    print("2. Record Player Performance")
    print("3. View Scoreboard")
    print("4. View Team Statistics")
    print("5. Find Highest Scorer")
    print("6. Find Lowest Scorer")
    print("7. Search Player")
    print("8. Find Boundary Leader")
    print("9. Display Player List")
    print("10. Display Match Information")
    print("11. Reset Match")
    print("12. Exit")
    print("------------------------------------------")
def setup_match():
    print("\n========== MATCH SETUP ==========")
    match_info["team"] = input("Enter your team name: ")
    match_info["opponent"] = input("Enter opponent team name: ")
    print("\nAvailable overs:")
    print("1. 5 Overs")
    print("2. 10 Overs")
    print("3. 20 Overs")
    choice = input("Enter choice: ")
    if choice == "1":
        match_info["overs"] = 5
    elif choice == "2":
        match_info["overs"] = 10
    elif choice == "3":
        match_info["overs"] = 20
    else:
        print("Invalid choice. 10 overs selected.")
        match_info["overs"] = 10
    print("\nMatch setup completed.")
    print(match_info["team"], "vs", match_info["opponent"])
    print("Overs:", match_info["overs"])
def add_player():
    print("\n========== ADD PLAYER ==========")
    name = input("Enter player name: ")
    if name == "":
        print("Player name cannot be empty.")
        return
    if name in player_names:
        print("Player already exists.")
        return
    print("\nBatting Positions:")
    for i in range(len(batting_positions)):
        print(i + 1, ".", batting_positions[i])
    position_choice = input("Enter position number: ")
    if position_choice == "1":
        position = batting_positions[0]
    elif position_choice == "2":
        position = batting_positions[1]
    elif position_choice == "3":
        position = batting_positions[2]
    elif position_choice == "4":
        position = batting_positions[3]
    elif position_choice == "5":
        position = batting_positions[4]
    else:
        print("Invalid position. Lower Order selected.")
        position = batting_positions[4]
    players[name] = {
        "position": position,
        "runs": 0,
        "balls": 0,
        "fours": 0,
        "sixes": 0,
        "out": "Not Out"
    }
    player_names.add(name)
    player_order.append(name)
    print("\nPlayer added successfully!")
    print("Name:", name)
    print("Position:", position)
def record_performance():
    print("\n========== RECORD PERFORMANCE ==========")
    if len(player_names) == 0:
        print("No players have been added.")
        return
    print("\nPlayers:")
    for i in range(len(player_order)):
        print(i + 1, ".", player_order[i])
    name = input("Enter player name: ")
    if name not in player_names:
        print("Player not found.")
        return
    runs = int(input("Enter runs scored: "))
    balls = int(input("Enter balls faced: "))
    fours = int(input("Enter number of fours: "))
    sixes = int(input("Enter number of sixes: "))
    if runs < 0 or balls < 0 or fours < 0 or sixes < 0:
        print("Values cannot be negative.")
        return
    if fours * 4 + sixes * 6 > runs:
        print("Number of boundaries cannot be greater than total runs.")
        return
    players[name]["runs"] = runs
    players[name]["balls"] = balls
    players[name]["fours"] = fours
    players[name]["sixes"] = sixes
    out_choice = input("Is the player out? (yes/no): ").lower()
    if out_choice == "yes":
        players[name]["out"] = "Out"
    else:
        players[name]["out"] = "Not Out"
    print("\nPerformance recorded successfully!")
def calculate_total_runs():
    total = 0
    for name in player_order:
        total = total + players[name]["runs"]
    total = total + match_info["extras"]
    return total
def calculate_total_balls():
    total = 0
    for name in player_order:
        total = total + players[name]["balls"]
    return total
def calculate_total_fours():
    total = 0
    for name in player_order:
        total = total + players[name]["fours"]
    return total
def calculate_total_sixes():
    total = 0
    for name in player_order:
        total = total + players[name]["sixes"]
    return total
def calculate_wickets():
    wickets = 0
    for name in player_order:
        if players[name]["out"] == "Out":
            wickets = wickets + 1
    return wickets
def display_scoreboard():
    print("\n========== SCOREBOARD ==========")
    if len(player_names) == 0:
        print("No players have been added.")
        return
    print("\nTeam:", match_info["team"])
    print("Opponent:", match_info["opponent"])
    print("\n")
    print("Player".ljust(18), "Runs".ljust(8), "Balls".ljust(8),
          "4s".ljust(6), "6s".ljust(6), "Status")
    print("-" * 65)
    for name in player_order:
        print(
            name.ljust(18),
            str(players[name]["runs"]).ljust(8),
            str(players[name]["balls"]).ljust(8),
            str(players[name]["fours"]).ljust(6),
            str(players[name]["sixes"]).ljust(6),
            players[name]["out"]
        )
    print("-" * 65)
    print("Extras:", match_info["extras"])
    print("Total:", calculate_total_runs(), "/", calculate_wickets())
def team_statistics():
    print("\n========== TEAM STATISTICS ==========")
    if len(player_names) == 0:
        print("No player data available.")
        return
    total_runs = calculate_total_runs()
    total_balls = calculate_total_balls()
    total_fours = calculate_total_fours()
    total_sixes = calculate_total_sixes()
    wickets = calculate_wickets()
    player_count = len(player_names)
    batting_runs = 0
    for name in player_order:
        batting_runs = batting_runs + players[name]["runs"]
    average = batting_runs / player_count
    print("Team:", match_info["team"])
    print("Opponent:", match_info["opponent"])
    print("Overs Limit:", match_info["overs"])
    print("Total Runs:", total_runs)
    print("Wickets:", wickets)
    print("Total Balls Faced:", total_balls)
    print("Total Fours:", total_fours)
    print("Total Sixes:", total_sixes)
    print("Average Runs per Player:", average)
    if total_balls > 0:
        run_rate = total_runs / (total_balls / 6)
        print("Current Run Rate:", run_rate)
    else:
        print("Current Run Rate: 0")
def highest_scorer():
    print("\n========== HIGHEST SCORER ==========")
    if len(player_names) == 0:
        print("No players available.")
        return
    highest_name = player_order[0]
    for name in player_order:
        if players[name]["runs"] > players[highest_name]["runs"]:
            highest_name = name
    print("Player:", highest_name)
    print("Runs:", players[highest_name]["runs"])
    print("Balls:", players[highest_name]["balls"])
    print("Fours:", players[highest_name]["fours"])
    print("Sixes:", players[highest_name]["sixes"])
def lowest_scorer():
    print("\n========== LOWEST SCORER ==========")
    if len(player_names) == 0:
        print("No players available.")
        return
    lowest_name = player_order[0]
    for name in player_order:
        if players[name]["runs"] < players[lowest_name]["runs"]:
            lowest_name = name
    print("Player:", lowest_name)
    print("Runs:", players[lowest_name]["runs"])
    print("Balls:", players[lowest_name]["balls"])
    print("Fours:", players[lowest_name]["fours"])
    print("Sixes:", players[lowest_name]["sixes"])
def search_player():
    print("\n========== SEARCH PLAYER ==========")
    if len(player_names) == 0:
        print("No players available.")
        return
    search_name = input("Enter player name: ")
    if search_name in player_names:
        print("\nPlayer found!")
        print("Name:", search_name)
        print("Position:", players[search_name]["position"])
        print("Runs:", players[search_name]["runs"])
        print("Balls:", players[search_name]["balls"])
        print("Fours:", players[search_name]["fours"])
        print("Sixes:", players[search_name]["sixes"])
        print("Status:", players[search_name]["out"])
    else:
        print("Player not found.")
def boundary_leader():
    print("\n========== BOUNDARY LEADER ==========")
    if len(player_names) == 0:
        print("No players available.")
        return
    leader = player_order[0]
    for name in player_order:
        current_boundaries = players[name]["fours"] + players[name]["sixes"]
        leader_boundaries = players[leader]["fours"] + players[leader]["sixes"]
        if current_boundaries > leader_boundaries:
            leader = name
    total_boundaries = players[leader]["fours"] + players[leader]["sixes"]
    print("Player:", leader)
    print("Fours:", players[leader]["fours"])
    print("Sixes:", players[leader]["sixes"])
    print("Total Boundaries:", total_boundaries)
def display_players():
    print("\n========== PLAYER LIST ==========")
    if len(player_names) == 0:
        print("No players added.")
        return
    for i in range(len(player_order)):
        name = player_order[i]
        print(i + 1, ".", name, "-", players[name]["position"])
def display_match_information():
    print("\n========== MATCH INFORMATION ==========")
    print("Team:", match_info["team"])
    print("Opponent:", match_info["opponent"])
    print("Overs:", match_info["overs"])
    print("Players:", len(player_names))
    print("Extras:", match_info["extras"])
    if len(player_names) > 0:
        print("Current Score:", calculate_total_runs(), "/", calculate_wickets())
    else:
        print("Current Score: 0 / 0")
def reset_match():
    print("\n========== RESET MATCH ==========")
    confirmation = input(
        "Are you sure you want to delete all player data? (yes/no): "
    ).lower()
    if confirmation == "yes":
        players.clear()
        player_names.clear()
        player_order.clear()
        match_info["extras"] = 0
        print("Match data has been reset.")
    else:
        print("Reset cancelled.")
display_title()
setup_match()
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_player()
    elif choice == "2":
        record_performance()
    elif choice == "3":
        display_scoreboard()
    elif choice == "4":
        team_statistics()
    elif choice == "5":
        highest_scorer()
    elif choice == "6":
        lowest_scorer()
    elif choice == "7":
        search_player()
    elif choice == "8":
        boundary_leader()
    elif choice == "9":
        display_players()
    elif choice == "10":
        display_match_information()
    elif choice == "11":
        reset_match()
    elif choice == "12":
        print("\nThank you for using Cricket Scoreboard!")
        print("Goodbye!")
        break
    else:
        print("\nInvalid choice. Please enter a number from 1 to 12.")
