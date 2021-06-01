import json
import random

#---------------------
#Load data
#---------------------
with open('sorteo.json','r') as file:
    data = json.load(file)

participants = data['Participants']
last_host = data['Last_host']
times_being_host = data['Times_being_host']

names = list(times_being_host.keys())
times = list(times_being_host.values())
probs = list(map(lambda x: int(max(times)-x), times))

print('Participantes: ', end = '' )
[print(x, end = ' ' ) for x in names]

#---------------------
#Select the Host
#---------------------
while True:
    win = random.choices(names, weights=probs)[0]
    if win!=last_host:
        break

#---------------------
#Shuffle the rest of participants, and add the host at the beginning
#---------------------
names.remove(win)
random.shuffle(names)
names.insert(0, win)

#---------------------
#Save and show results
#---------------------
data['Last_host'] = win

try:
    data['Times_being_host'][win] += 1 
except KeyError:
    data['Times_being_host'][win] = 1

print('\nSorteo:')

for i,j in enumerate(names):    
    print( str(i+1) + "- " + j )

with open('sorteo.json','w') as file:
    json.dump(data,file,indent=4)

print('\nVersion:01.06.2021.MeliS')