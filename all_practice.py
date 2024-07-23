drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = {key:value for key, value in zip(drinks, caffeine)}
print(zipped_drinks)    