import random

file = open("phones.lst", 'w')
i = 0
kidomot = ("050", "051", "052", "053", "054", "055", "058", "059")
while i < 1000000:
    i += 1
    kidomet = random.choice(kidomot)
    number = str(random.randint(1000000, 9999999))
    file.write(kidomet+"-"+number+"\n")
file.close()