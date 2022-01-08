import random, string

amount = int(input('Amount of nitro codes to generate: '))
value = 1
while value <= amount:
	code = "https://discord.gift/" + ('').join(
	    random.choices(string.ascii_letters + string.digits, k=16))
	f = open('Codes by $MartoBossX.txt', "a+")
	f.write(f'{code}\n')
	f.close()
	print(f'{code}')
	value += 1
print("\n\n\nJoin in our discord https://discord.gg/AsN6tY3KMr")
