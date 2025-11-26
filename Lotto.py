#5-ös lottó
print('Köszöntelek az 5-ös lottó játákban.')
print('Írd le a szelvényed tippjeit ez az üzenet alá, vesszőkkel elválasztva.')
tipp = input()

nyeroszelveny = []

helyes_tippek = []

import random

for i in range(5):
    i = random.randint(1,90)
    nyeroszelveny.append(i)

for szam in tipp:
    if szam in nyeroszelveny:
        helyes_tippek.append(szam)

print(f'Ez volt a nyerő szelvény:{nyeroszelveny})

print(f'Ez volt a te tipped : {tipp})


print(f'Ennyi helyes tipped volt {len(helyes_tippek)}')