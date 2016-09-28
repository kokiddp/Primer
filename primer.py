import math
import time

n = 10000000

print('Caricamento lista numeri primi...')
ii = time.time()

ip = open('primi.txt', 'r' )
divisori = ip.readlines()
pd = [int(x) for x in divisori if (int(x) < (math.sqrt(n)+1))]
pd.remove(1)
ip.close()

ti = (time.time()) - ii
print('Caricamento completato. Tempo richiesto:',ti,'secondi')

time.sleep(2)
print('Inizio calcolo numeri primi minori di', n,'fra 3 secondi')
time.sleep(3)

primi = []
num = range(1,n)

io = time.time()
op = open('primer.txt','w')

for i in num:
	flag = 1
	lim = (int(math.sqrt(i)) + 1)
	#dp = [d for d in pd if (d < lim)]

	#for y in range(2, lim):
	for y in pd:
		if y < lim:
			if (i%y) == 0:
				flag = 0
				break

	if flag == 1:
		primi.append(i)
		print('#',len(primi),':', i)
		op.write(str(i) + '\n')
		
to = (time.time()) - io
print('Tempo necessario per calcolare',len(primi),'numeri primi minori di',n,':',to,'secondi')
op.write('Tempo totale: ' + str(to) + ' secondi')

op.close()
print('Premere "Invio" per uscire')
input()