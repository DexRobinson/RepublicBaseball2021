import json
from Data import Data

all_stats = []
overall_highest_stats = \
        {
            "H": 0,
            "R": 0,
            "HR": 0,
            "TB": 0,
            "RBI": 0,
            "BB": 0,
            "K": 9999,
            "SB": 0,
            "AVG": 0,
            "OPS": 0,
            "IP": 0,
            "HRG": 9999,
            "QS": 0,
            "W": 0,
            "L": 9999,
            "SV": 0,
            "BAA": 9999,
            "ERA": 9999,
            "WHIP": 9999,
            "K9": 0,
        }
overall_lowest_stats = \
        {
            "H": 0,
            "R": 0,
            "HR": 0,
            "TB": 0,
            "RBI": 0,
            "BB": 0,
            "K": 9999,
            "SB": 0,
            "AVG": 0,
            "OPS": 0,
            "IP": 0,
            "HRG": 9999,
            "QS": 0,
            "W": 0,
            "L": 9999,
            "SV": 0,
            "BAA": 9999,
            "ERA": 9999,
            "WHIP": 9999,
            "K9": 0,
        }

for team in Data.teams:
    highest_stats = \
        {
            "H": 0,
            "R": 0,
            "HR": 0,
            "TB": 0,
            "RBI": 0,
            "BB": 0,
            "K": 9999,
            "SB": 0,
            "AVG": 0,
            "OPS": 0,
            "IP": 0,
            "HRG": 9999,
            "QS": 0,
            "W": 0,
            "L": 9999,
            "SV": 0,
            "BAA": 9999,
            "ERA": 9999,
            "WHIP": 9999,
            "K9": 0,
        }
    lowest_stats = \
        {
            "H": 9999,
            "R": 9999,
            "HR": 9999,
            "TB": 9999,
            "RBI": 9999,
            "BB": 9999,
            "K": 0,
            "SB": 9999,
            "AVG": 9999,
            "OPS": 9999,
            "IP": 9999,
            "HRG": 0,
            "QS": 9999,
            "W": 9999,
            "L": 0,
            "SV": 9999,
            "BAA": 0,
            "ERA": 0,
            "WHIP": 0,
            "K9": 9999,
        }

    points = 0
    with open(f'TeamOutput\\{team.replace(" ", "")}.json') as json_file:
        data = json.load(json_file)
        for week in range(Data.weeks):
            w = f"WEEK{week+1}"

            for p in Data.pos_cats:
                if float(data[w][p]) > float(highest_stats[p]):
                    highest_stats[p] = float(data[w][p])

                if float(data[w][p]) < float(lowest_stats[p]):
                    lowest_stats[p] = float(data[w][p])

            for n in Data.neg_cats:
                if float(data[w][n]) < float(highest_stats[n]):
                    highest_stats[n] = float(data[w][n])

                if float(data[w][n]) > float(lowest_stats[n]):
                    lowest_stats[n] = float(data[w][n])

        all_stats.append({team: highest_stats})
        all_stats.append({team: lowest_stats})

id = 0
for team in Data.teams:
    highest_stats = all_stats[id][team]
    id = id + 1
    lowest_stats = all_stats[id][team]
    id = id + 1

    for p in Data.pos_cats:
        if highest_stats[p] > overall_highest_stats[p]:
            overall_highest_stats[p] = highest_stats[p]
        if lowest_stats[p] > overall_lowest_stats[p]:
            overall_lowest_stats[p] = lowest_stats[p]

    for n in Data.neg_cats:
        if highest_stats[n] < overall_highest_stats[n]:
            overall_highest_stats[n] = highest_stats[n]
        if lowest_stats[n] < overall_lowest_stats[n]:
            overall_lowest_stats[n] = lowest_stats[n]

id = 0
for team in Data.teams:
    points = 0
    highest_stats = all_stats[id][team]
    id = id + 1
    lowest_stats = all_stats[id][team]
    id = id + 1

    for p in Data.pos_cats:
        points = points + (highest_stats[p] / overall_highest_stats[p])
        points = points + (lowest_stats[p] / overall_lowest_stats[p])

    for n in Data.neg_cats:
        if overall_highest_stats[n] == 0:
            overall_highest_stats[n] = 1
        if highest_stats[n] == 0:
            highest_stats[n] = 1

        points = points + (overall_lowest_stats[n] / lowest_stats[n])
        points = points + (overall_highest_stats[n] / highest_stats[n])

    print(f"{team}\t{highest_stats['H']}\t{highest_stats['R']}\t{highest_stats['HR']}\t{highest_stats['TB']}\t{highest_stats['RBI']}"
          f"\t{highest_stats['BB']}\t{highest_stats['K']}\t{highest_stats['SB']}\t{highest_stats['AVG']}"
          f"\t{highest_stats['OPS']}\t{highest_stats['IP']}\t{highest_stats['HRG']}\t{highest_stats['QS']}"
          f"\t{highest_stats['W']}\t{highest_stats['L']}\t{highest_stats['SV']}\t{highest_stats['BAA']}"
          f"\t{highest_stats['ERA']}\t{highest_stats['WHIP']}\t{highest_stats['K9']}\t{points}")

    print(f"{''}\t{lowest_stats['H']}\t{lowest_stats['R']}\t{lowest_stats['HR']}\t{lowest_stats['TB']}\t{lowest_stats['RBI']}"
          f"\t{lowest_stats['BB']}\t{lowest_stats['K']}\t{lowest_stats['SB']}\t{lowest_stats['AVG']}"
          f"\t{lowest_stats['OPS']}\t{lowest_stats['IP']}\t{lowest_stats['HRG']}\t{lowest_stats['QS']}"
          f"\t{lowest_stats['W']}\t{lowest_stats['L']}\t{lowest_stats['SV']}\t{lowest_stats['BAA']}"
          f"\t{lowest_stats['ERA']}\t{lowest_stats['WHIP']}\t{lowest_stats['K9']}")


