import json
import random

with open('sorteo.json','r') as file:
    data = json.load(file)

participants = data['Participants']
last_host = data['Last_host']

print('Participantes: ', end = '' )
[print(x, end = ' ' ) for x in participants]

while True:
    random.shuffle(participants)
    if participants[0]!=last_host:
        break
    
data['Last_host'] = participants[0]

try:
    data['Times_being_host'][participants[0]] += 1 
except KeyError:
    data['Times_being_host'][participants[0]] = 1

print('\nSorteo:')

for i,j in enumerate(participants):    
    print( str(i+1) + "- " + j )

with open('sorteo.json','w') as file:
    json.dump(data,file,indent=4)
	
print('\nVersion:11.05.IvanP')