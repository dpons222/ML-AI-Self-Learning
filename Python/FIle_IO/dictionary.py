names = ['victor', 'diego', 'ara', 'julian', 'victor', 'angela', 'julian', 'victor', 'diego', 'angela', 'ara', 'julian', 'diego', 'victor', 'julian', 'angela', 'ara', 'victor', 'diego', 'ara', 'angela', 'julian', 'ara', 'victor', 'angela', 'julian', 'diego', 'ara', 'victor', 'angela']
counts = dict()

for name in names :
    counts[name] = counts.get(name,0) + 1

print(counts)