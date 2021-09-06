import json
from Data import Data


def output():
    stats = []
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
            "L": 0,
            "SV": 0,
            "BAA": 9999,
            "ERA": 9999,
            "WHIP": 9999,
            "K9": 0,
        }

    for team in Data.teams:
        with open(f'OutputAgainst\\{team.replace(" ", "")}.json') as json_file:
            data = json.load(json_file)
            data['TEAM'] = team
            stats.append(data)

            # print(f"{team}\tH:{data['H']}"
            #       f"\tR:{data['R']}"
            #       f"\tHR:{data['HR']}"
            #       f"\tTB:{data['TB']}"
            #       f"\tRBI:{data['RBI']}"
            #       f"\tBB:{data['BB']}"
            #       f"\tK:{data['K']}"
            #       f"\tSB:{data['SB']}"
            #       f"\tAVG:{float('{:.3f}'.format(data['AVG']))}"
            #       f"\tOPS:{float('{:.3f}'.format(data['OPS']))}"
            #       f"\tIP:{float('{:.1f}'.format(data['IP']))}"
            #       f"\tHR:{data['HRG']}"
            #       f"\tQS:{data['QS']}"
            #       f"\tW:{data['W']}"
            #       f"\tL:{data['L']}"
            #       f"\tSV:{data['SV']}"
            #       f"\tBAA:{float('{:.3f}'.format(data['BAA']))}"
            #       f"\tERA:{float('{:.3f}'.format(data['ERA']))}"
            #       f"\tWHIP:{float('{:.3f}'.format(data['WHIP']))}"
            #       f"\tK9:{float('{:.3f}'.format(data['K9']))}")
            print(f"{team}\t{data['H']}"
                  f"\t{data['R']}"
                  f"\t{data['HR']}"
                  f"\t{data['TB']}"
                  f"\t{data['RBI']}"
                  f"\t{data['BB']}"
                  f"\t{data['K']}"
                  f"\t{data['SB']}"
                  f"\t{float('{:.3f}'.format(data['AVG']))}"
                  f"\t{float('{:.3f}'.format(data['OPS']))}"
                  f"\t{float('{:.1f}'.format(data['IP']))}"
                  f"\t{data['HRG']}"
                  f"\t{data['QS']}"
                  f"\t{data['W']}"
                  f"\t{data['L']}"
                  f"\t{data['SV']}"
                  f"\t{float('{:.3f}'.format(data['BAA']))}"
                  f"\t{float('{:.3f}'.format(data['ERA']))}"
                  f"\t{float('{:.3f}'.format(data['WHIP']))}"
                  f"\t{float('{:.3f}'.format(data['K9']))}")

    for s in stats:
        for key in Data.all_cats:
            if key == 'K' or key == 'HRB' or key == 'BAA' or key == 'ERA' or key == 'WHIP':
                if s[key] < highest_stats[key]:
                    highest_stats[key] = s[key]
            else:
                if s[key] > highest_stats[key]:
                    highest_stats[key] = s[key]

    for s in stats:
        points = 0
        for key in Data.all_cats:
            if key == 'ERA' or key == 'WHIP':
                pass
            else:
                if key == 'K' or key == 'HRB' or key == 'BAA' or key == 'ERA' or key == 'WHIP':
                    points = points + (highest_stats[key] / s[key])
                else:
                    points = points + s[key] / highest_stats[key]

        print(f"{s['TEAM']}\t{float('{:.3f}'.format(points))}")