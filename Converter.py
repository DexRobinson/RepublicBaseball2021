import json
from Data import Data


def output():
    for w in range(Data.weeks):
        week = w + 1
        f = open(f"WeekData\\Week{week}.txt", "r")
        data = f.read()
        split = str(data).split('\n')

        for x in range(10):
            offset = 21 * x
            if x % 2 == 0:
                opp = 21+offset
            else:
                opp = offset - 21
            team_info = {
                f"WEEK{week}":
                    {
                        "TEAM": split[0+offset],
                        "H": split[1+offset],
                        "R": split[2+offset],
                        "HR": split[3+offset],
                        "TB": split[4+offset],
                        "RBI": split[5+offset],
                        "BB": split[6+offset],
                        "K": split[7+offset],
                        "SB": split[8+offset],
                        "AVG": split[9+offset],
                        "OPS": split[10+offset],
                        "IP": split[11+offset],
                        "HRG": split[12+offset],
                        "QS": split[13+offset],
                        "W": split[14+offset],
                        "L": split[15+offset],
                        "SV": split[16+offset],
                        "BAA": split[17+offset],
                        "ERA": split[18+offset],
                        "WHIP": split[19+offset],
                        "K9": split[20+offset],
                        "OPP": split[opp],
                }
            }

            # need to add the data to the output
            team = team_info[f"WEEK{week}"]['TEAM']
            if w == 0:
                with open(f'TeamOutput\\{team}.json', 'w') as outfile:
                    json.dump(team_info, outfile, indent=4)
            else:
                with open(f'TeamOutput\\{team}.json', "r+") as file:
                    data = json.load(file)
                    data.update(team_info)
                    file.seek(0)
                    json.dump(data, file, indent=4)
