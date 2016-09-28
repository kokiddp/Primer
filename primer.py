import math
import time
import os

n = 1000000

print('Looking for input file...')
ii = time.time()

if os.path.exists("./input.txt"):
    print('"input.txt found! This will speed things up!')
    print('Loading input file...')
    ip = open('input.txt', 'r')
    divisori = ip.readlines()
    pd = [int(x) for x in divisori if (int(x) < (math.sqrt(n) + 1))]
    pd.remove(1)
    ip.close()
else:
    print('"input.txt" not found.')
    print('I will be slower than ideal.')
    pd = range(2, int(math.sqrt(n)) + 1)


ti = (time.time()) - ii
print('Divisor list generation complete.')
print(len(pd), 'divisors generated in', round(ti, 5), 'seconds')

time.sleep(2)
print('I will begin calculating primes up to', n, 'in 3 seconds')
time.sleep(3)

primi = []
num = range(1, n)

io = time.time()
op = open('output.txt', 'w')

for i in num:
    flag = 1
    lim = (int(math.sqrt(i)) + 1)

    for y in pd:
        if y < lim:
            if (i % y) == 0:
                flag = 0
                break

    if flag == 1:
        primi.append(i)
        print('#', len(primi), ':', i)
        op.write(str(i) + '\n')

to = (time.time()) - io
print('Time elapsed calculating', len(primi),
      'prime numbers <', n, ':', round(to, 5), 'seconds')

op.close()
print('Press "Enter" to exit... ')
input()
