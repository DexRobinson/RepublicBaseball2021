import json
from Data import Data


def output():
    for team in Data.teams:
        with open(f'TeamOutput\\{team}.json') as json_file:
            data_team = json.load(json_file)
            json_file.close()

        for w in range(Data.weeks):
            week = f"WEEK{w+1}"

            opp = data_team[week]['OPP']
            with open(f'TeamOutput\\{opp}.json') as opp_file:
                opp_data = json.load(opp_file)[week]
                opp_file.close()

            opp_json = {
                "H": opp_data['H'],
                "R": opp_data['R'],
                "HR": opp_data['HR'],
                "TB": opp_data['TB'],
                "RBI": opp_data['RBI'],
                "BB": opp_data['BB'],
                "K": opp_data['K'],
                "SB": opp_data['SB'],
                "AVG": opp_data['AVG'],
                "OPS": opp_data['OPS'],
                "IP": opp_data['IP'],
                "HRG": opp_data['HRG'],
                "QS": opp_data['QS'],
                "W": opp_data['W'],
                "L": opp_data['L'],
                "SV": opp_data['SV'],
                "BAA": opp_data['BAA'],
                "ERA": opp_data['ERA'],
                "WHIP": opp_data['WHIP'],
                "K9": opp_data['K9']
            }
            if w == 0:
                with open(f'OutputAgainst\\{team}.json', 'w') as outfile:
                    json.dump(opp_json, outfile, indent=4)
                    outfile.close()
            else:
                with open(f'OutputAgainst\\{team}.json', "r+") as file:
                    data = json.load(file)
                    combo_data = {
                        "H": float(opp_data['H']) + float(data['H']),
                        "R": float(opp_data['R']) + float(data['R']),
                        "HR": float(opp_data['HR']) + float(data['HR']),
                        "TB": float(opp_data['TB']) + float(data['TB']),
                        "RBI": float(opp_data['RBI']) + float(data['RBI']),
                        "BB": float(opp_data['BB']) + float(data['BB']),
                        "K": float(opp_data['K']) + float(data['K']),
                        "SB": float(opp_data['SB']) + float(data['SB']),
                        "AVG": (float(opp_data['AVG']) + float(data['AVG'])) / 2,
                        "OPS": (float(opp_data['OPS']) + float(data['OPS'])) / 2,
                        "IP": float(opp_data['IP']) + float(data['IP']),
                        "HRG": float(opp_data['HRG']) + float(data['HRG']),
                        "QS": float(opp_data['QS']) + float(data['QS']),
                        "W": float(opp_data['W']) + float(data['W']),
                        "L": float(opp_data['L']) + float(data['L']),
                        "SV": float(opp_data['SV']) + float(data['SV']),
                        "BAA": (float(opp_data['BAA']) + float(data['BAA'])) / 2,
                        "ERA": (float(opp_data['ERA']) + float(data['ERA'])) / 2,
                        "WHIP": (float(opp_data['WHIP']) + float(data['WHIP'])) / 2,
                        "K9": (float(opp_data['K9']) + float(data['K9'])) / 2
                    }

                    file.seek(0)
                    json.dump(combo_data, file, indent=4)
                    file.truncate()
