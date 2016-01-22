import json

def get_subtotals(exercise):
    points = 0
    kgs = 0
    km = 0
    for workout_set in exercise:
        points += workout_set['points']
        try:
            unit = workout_set['effort1_metric_unit']['name']
        except TypeError:   # first key was None
            continue
        if unit == 'Reps':
            weight = 0 if not workout_set['effort0_metric'] else workout_set['effort0_metric']
            reps = workout_set['effort1']
            multiplier = workout_set['action']['multiplier']
            kgs += weight * reps * multiplier
        elif unit == 'Kilometers':
            km += workout_set['effort1_metric']
        elif unit == 'Meters':
            km += workout_set['effort1_metric'] / 1000.0
        else:
            print('unexpected unit: {}'.format(unit))
    return {"points": points, "kgs": kgs, "km": km}

try:
    myHistoryFile = "fitocracyHistory.json"
    with open(myHistoryFile) as file:
        decoded = json.load(file)

    year = "2015"
    totals = {"points": 0, "kgs": 0, "km": 0}
    for identifier in decoded:
        for item in decoded[identifier]['data']:
            if year in item['date']:
                subtotals = get_subtotals(item['actions'])
                totals = {key: totals[key] + subtotals[key] for key in totals}

    print("{} totals:\n".format(year))            
    print("{} points".format(totals["points"]))
    print("{0:.0f} kgs".format(totals["kgs"]))
    print("{0:.2f} km".format(totals["km"]))
    
finally:
    import sys
    if sys.stdout.isatty():
        input("\npress is tty enter to continue")
    else:
        print('bla')
