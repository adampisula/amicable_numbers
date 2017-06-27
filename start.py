import math
import sys
import os

def divisors(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)

SUBJECT = "New_amicable_number!"

sums = []
amicable = []

i = 0

while i < 10000:
    div = list(divisors(i))
    divsum = 0

    for j in range(0, len(div) - 1):
        divsum += div[j]

    sums.append(divsum)

    for j in reversed(range(0, i)):
        if (i == sums[j]) and (j == sums[i]):
            if (str(i) + ":" + str(j)) not in amicable:
                amicable.append(str(i) + ":" + str(j))
                
                #SENDING MAIL
		#send_email.exe IS A C# PROGRAM WHICH SENDS EMAILS TO ME VIA A SPECIAL ACCOUNT - MAKE SUCH A SCRIPT YOURSELF AND USE IT AS send_email.exe OR DO IT WITH PYTHON
                os.system("mono send_email.exe " + SUBJECT + " " + str(amicable))

                print(amicable)
    i += 1
