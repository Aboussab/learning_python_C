import sys

"""this is a programe where we discover more about list
    we store it and organize it as a games scores:
    Calculate some basic stats on this list and  Handle the udge case
"""

if __name__ == '__main__':

    player_list = []
    try:
        print("=== Player Score Analytics ===")
        if (len(sys.argv) > 1):
            i = 1
            while (i < len(sys.argv)):
                player_list = player_list + [int(sys.argv[i])]
                i += 1
            print(f"Scores processed: {player_list}")
            print(f"Total players: {len(player_list)}")
            print(f"Total score: {sum(player_list)}")
            print(f"Average score: {sum(player_list)/len(player_list)}")
            print(f"High score: {max(player_list)}")
            print(f"Low score: {min(player_list)}")
            print(f"Score range: {max(player_list) - min(player_list)}")
        else:
            print("No scores provided. Usage: ", end='')
            print("python3 ft_score_analytics.py <score1> <score2> ...")
    except ValueError:
        print("oops, you have an value error.")
