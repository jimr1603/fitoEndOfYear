import json

with open("fitocracyHistory.json") as f:
    encoded = f.readlines()
decoded = json.loads(encoded[0])

points = 0
kgs = 0
km = 0

for identifier in decoded:
    multiplier = 1
    if "dumb" in decoded[identifier]['name'].lower():
        multiplier = 2
    for item in decoded[identifier]['data']:
        if "2015" in item['date']:
            for item2 in item['actions']:
                reps=item2['effort1_metric_string']
                if type(reps) == str:
                    if 'reps' in reps:
                        reps = float(reps[0:-4])
                        weight = item2['effort0_string']
                        if type(weight) == str and 'kg' in weight:
                            weight=float(weight[0:-2])
                            kgs += weight * reps * multiplier
                    else:
                        if 'k' in reps:
                            reps = float(reps[0:-2])
                        else:
                            reps = (float(reps[0:-1]))/1000
                        km += reps
                
                points += item2['points']

print(str(points) + " points")
print("{0:.0f}".format(kgs) + " kgs")
print("{0:.2f}".format(km) + " km")
