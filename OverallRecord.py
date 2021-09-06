import json
from Data import Data


def output():
    for team in Data.teams:
        with open(f'TeamOutput\\{team}.json') as json_file:
            data_team = json.load(json_file)
            json_file.close()

        wins = 0
        loses = 0
        ties = 0

        for w in range(Data.weeks):
            week = f"WEEK{w+1}"

            for t in Data.teams:
                if t != team:
                    with open(f'TeamOutput\\{t}.json') as opp_file:
                        opp_data = json.load(opp_file)[week]
                        opp_file.close()

                    for cat in Data.pos_cats:
                        if data_team[week][cat] > opp_data[cat]:
                            wins = wins + 1
                        elif data_team[week][cat] < opp_data[cat]:
                            loses = loses + 1
                        else:
                            ties = ties + 1

                    for cat in Data.neg_cats:
                        if data_team[week][cat] < opp_data[cat]:
                            wins = wins + 1
                        elif data_team[week][cat] > opp_data[cat]:
                            loses = loses + 1
                        else:
                            ties = ties + 1

        record = float('{:.3f}'.format(wins / (wins + loses + ties)))
        print(f"{team}\t{wins}\t{loses}\t{ties}\t{record}")
