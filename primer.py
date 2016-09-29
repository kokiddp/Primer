import math
import time
import os

n = eval(input('Insert a number. I will calculate prime numbers up to that.'))

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
    if pd[len(pd) - 1] < math.sqrt(n):
        print('WARNING: Input file inufficient, it will not be used')
        print('The biggest number on list (', pd[len(
            pd) - 1], ') needs to be equal or greater than the square root of the inserted number (', int(math.sqrt(n)) + 1, ')')
        print('Hint: calculate primes up to', (int(math.sqrt(n)) + 1),
              'and rename output.txt to input.txt')
        for q in range(len(pd), int(math.sqrt(n)) + 1):
            pd.append(q)
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
num = range(2, n)

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
