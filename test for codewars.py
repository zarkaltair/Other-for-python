# def accum(s):
#     st = []
#     z = 1
#     for i in s:
#         x = i * z + '-'
#         z += 1
#         st.append(x.capitalize())
#     tt = st[-1].replace('-', '')
#     st[-1] = tt
#     return ''.join(st)
# print(accum('ZpglnRxqenU'))


# n = [ 1, 5, 4, 3, 8, 12]
# n.sort()
# print(n)


# s = 'pexrgm'
# s = 'abcdef'
# s = 'gnlyvknjga'
# s = 'slhacx'
# s = 'jpipe'
# sum = 0
# for i in s:
#     sum += ord(i)
# print(sum)


# def cake(candles, debris): 871 1083
#     sum = 0
#     for i in debris:
#         sum += ord(i)
#     if sum >= candles * 0.7:
#         return 'Fire!'
#     else:
#         return 'That was close!'


# s = ['ninja', 'samurai', 'ronin']
# print(', '.join(s))
# print('{}, {} & {}'.format(s))


# num = 654654215

# s = str(num)
# s = list(s)
# s = sorted(s)
# s = reversed(s)
# s = ''.join(s)
# print(s)


# num = 9119
# arr = [i for i in str(num)]
# for i in str(num):
# 	arr += i


# print(arr)

# print(int(x) * int(x) for x in [i for i in str(num)])

# def square_digits(num):
#     return int(''.join([str(int(x) ** 2) for x in [i for i in str(num)]]))

# print(square_digits(9119))

# import string

# s = "How Can Mirrors Be Real If Our Eyes Aren'T Real"

# print(string.capwords(s))


# P = 100
# X = 17
# Y = 34
# sum1 = round(X * 100 * (P * 0.01 + 1))
# sum2 = Y * (P * 0.01 + 1)
# sum = sum1 + sum2
# print(int(sum // 100))
# print(int(sum % 100))
# # print(sum)
# print(sum1)


# s = 'alpha'
# b = 'beta'

# def greek_comparator(lhs, rhs):
#     if len(lhs) - len(rhs) < 0:
#         return 'result should be negative'
#     elif len(lhs) - len(rhs) == 0:
#         return 0
#     else:
#         return 'result should be positive'

# print(greek_comparator('alpha', 'beta')


# arr = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

# from collections import Counter

# def find_it(seq):
#     c = Counter(seq)
#     for key in c:
#         if c[key] % 2 != 0:
#             print(key)

# find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])


# n = 39

# n = [int(i) for i in str(n)]
# n = str(tuple(n))
# nn = n.replace(',', '*')
# print(eval(nn))


# def persistence(n):
# 	if n < 10:
# 		return 1
# 	else:
# 		arr = []
# 		for i in str(n):
# 			arr.append(int(i))
# 		x = 1
# 		for i in arr:
# 			x *= i
# 		arr1 = []
# 		for i in str(x):
# 			arr1.append(int(i))
# 		y = 1
# 		for i in arr1:
# 			y *= i

# 		print(y)


# def persistence(n):
# 	if n < 10:
# 		return 1
# 	else:
# 		while :
			
# persistence(39)



# n = 246

# def digit(n):
# 	arr = [int(i) for i in str(n)]
# 	z = []
# 	while len(arr) > 1:
# 		# for i in arr:
		
# 		# z.append(i)
# 	print(len(arr))

# digit(246)


# from collections import Counter
# def duplicate_count(text):
#     arr = [i for i in text]
#     c = Counter(arr)
#     print(c)

# duplicate_count('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')



# def iq_test(numbers):
# 	arr = [int(i) for i in numbers.split(' ')]
# 	even = 0
# 	odd = 0
# 	for i in arr:
# 		if i % 2 == 0:
# 			even += 1
# 		else:
# 			odd += 1
# 	if even == 1:
# 		for i in arr:
# 			if i % 2 == 0:
# 				print(arr.index(i) + 1)
# 	else:
# 		for i in arr:
# 			if i % 2 != 0:
# 				print(arr.index(i) + 1)

# # iq_test([2, 4, 7, 8, 10]) # not
# # iq_test([1, 2, 2]) # yes
# iq_test("88 96 66 51 14 88 2 92 18 72 18 88 20 30 4 82 90 100 24 46")


# my_list = [2, 4, 6]
# # while len(my_list) != 1:
# # 	averages = [(x + y) / 2.0 for (x, y) in zip(my_list[:-1], my_list[1:])]
# print(len(my_list))


# def digits_average(input):
# 	arr = [int(i) for i in str(input)]
# 	z = ''
# 	if input < 10:
# 		return input
# 	else:
# 		for x, y in zip(arr[:-1], arr[1:]):
# 			z.join(str((x + y) / 2))
# 		print(int(x))

# digits_average(246)


# def scramble(s1, s2):
#     arr1 = [i for i in s1]
#     arr2 = [i for i in s2]
#     x = []
#     for i in arr2:
#         if i in arr1:
#             x.append(i)
#             arr1.remove(i)
#     return True if x == arr2 else False

# scramble('scriptingjav', 'javascript')


# def scramble(s1, s2):
#     for i in s2:
#         if i in s1:
#             s1 = s1.replace(i, '', 1)
#             s2 = s2.replace(i, '', 1)
#     print(True if s2 == '' else False)

# scramble('scriptingjav', 'javascript')


# def scramble(s1, s2):
#     i = 0
#     q = True
#     while i < len(s2):
#         if s2.count(s2[i]) <= s1.count(s2[i]):
#             q = True
#         else:
#             q = False
#             return q
#         i += 1
#     return True

# scramble('scriptingjav', 'javascript')


# def scramble(s1, s2):
#     arr1 = [i for i in s1]
#     arr2 = [i for i in s2]
#     for i in arr2:
#         if i in arr1:
#             arr1[arr1.index(i)] = ''
#             arr2[arr2.index(i)] = ''
#     return True if arr2.count('') == len(arr2) else False

# scramble('scriptingjav', 'javascript')


# def scramble(s1, s2):
#     if len(s2) <= len(s1):
#         return True
#     else:
#         return False


# s = 'Hello'
# for i in s:
#     if s.index(i) % 3 == 0:
#         s = s.replace(i, '0')
# print(s.replace('0', ''))


# def how_much_i_love_you(nb):
#     if nb % 6 == 1:
#         return 'I love you'
#     elif nb % 6 == 2:
#         return 'a little'
#     elif nb % 6 == 3:
#         return 'a lot'
#     elif nb % 6 == 4:
#         return 'passionately'
#     elif nb % 6 == 5:
#         return 'madly'
#     elif nb % 6 == 0:
#         return 'not at all'


# def dig_pow(n, p):
#     arr = [int(i) for i in str(n)]
#     x = 0
#     s = 0
#     for i in arr:
#         x += i ** (p + s)
#         s += 1
#     k = x / n
#     if n * p == x:
#         return 1
#     elif n * p < x:
#         if k == round(k):
#             return k
#         else:
#             return -1
#     else:
#         return -1


# return int(''.join([str(int(x) ** 2) for x in [i for i in str(n)]]))


# s = eval('*'.join([i for i in str(35)]))

# print(s)


# def persistence(n):
#     if n < 10:
#         return 0
#     else:
#         y = 0
#         while len(str(n)) != 1:
#             n = eval('*'.join([i for i in str(n)]))
#             y += 1
#             print(n)
#         print(y)

# persistence(39)

# from math import *
# arr = [int(i) for i in str(89)]
# while len(arr) != 1:
# 	arr = [ceil((x + y) / 2) for x, y in zip(arr[:-1], arr[1:])]

# print(arr[0])


# def song_decoder(song):
#     s = song.split('WUB')
#     for i in s:
#         s.remove('')
#     print(' '.join(s))

# song_decoder("AWUBWUBWUBBWUBWUBWUBC")


# import numpy as np
# def persistence(n):
#     if n < 10:
#         return 0
#     else:
#         while n > 10:
#             print(n)
#             print([int(i) for i in str(n)])
#             n = np.prod(np.array([int(i) for i in str(n)]))
#             print(n)
#             print([int(i) for i in str(n)])
#         print(n)

# persistence(99)


# def evaporator(content, evap_per_day, threshold):
#     day = 0
#     while content > content * threshold / 100:
#         print(content)
#         content = content - content * evap_per_day / 100
#         day += 1
#     print(day)

# evaporator(10, 10, 10)


# s = ''.join(["NORTH", "SOUTH"])

# print(s)


# def dirReduc(arr):
# 	arr = ''.join(arr)
# 	n = ''.join(["NORTH", "SOUTH"])
# 	s = ''.join(["SOUTH", "NORTH"])
# 	w = ''.join(["WEST", "EAST"])
# 	e = ''.join(["EAST", "WEST"])
# 	while n in arr or s in arr or w in arr or e in arr:
# 		if n in arr:
# 			arr = arr.replace(n, '')
# 		elif s in arr:
# 			arr = arr.replace(s, '')
# 		elif w in arr:
# 			arr = arr.replace(w, '')
# 		else:
# 			arr = arr.replace(e, '')
# 	if 'ST' in arr or 'TH' in arr:
# 		if 'ST' in arr:
# 			arr = arr.replace('ST', 'ST,')
# 			if 'TH' in arr:
# 				arr = arr.replace('TH', 'TH,')
# 		else:
# 			arr = arr.replace('TH', 'TH,')
# 			if 'ST' in arr:
# 				arr = arr.replace('ST', 'ST,')
# 	print(arr.split(','))

# dirReduc(['EAST', 'NORTH', 'WEST', 'WEST', 'EAST', 'EAST', 'NORTH', 'EAST', 'NORTH', 'WEST', 'EAST', 'NORTH', 'NORTH', 'WEST'])


# def ip(n):
# 	x = bin(n)
# 	x = str(x[2:])
# 	x0 = str(int(x[: -24], 2))
# 	x1 = str(int(x[-24: -16], 2))
# 	x2 = str(int(x[-16: -8], 2))
# 	x3 = str(int(x[-8:], 2))
# 	y = [x0, x1, x2, x3]
# 	z = '.'.join(y)
# 	print(z)

# ip(196816426) # 11.187.46.42


# n = '1011101110110010111000101010' # 1011 10111011 00101110 00101010

# print(n[-8:])


# n = 263
# x = [int(i) for i in str(n)]
# arr = list(str(n))
# arr = [int(x) * int(y) for x, y in zip(arr[:-1], arr[1:])]
# print(x + arr)


# n = 'hello'
# x = [n.title()]
# y = 1
# while y != len(n):
# 	x.append(n)
# 	y += 1
# print(x)


# def persistence(n):
#     n = [int(i) for i in str(n)]
#     x = 0
#     while len(n) != 1:
#         arr = [x * y for (x, y) in zip(n[:-1], n[1:])]
#         print(arr)
#         n = [int(i) for i in str(arr[0])]
#         print(n)
#         x += 1
#     print(x)

# persistence(999)


# n = 999
# x = 0
# while len(str(n)) != 1:
# n = [i for i in str(n)]
# n = int(eval('*'.join(n)))
# x += 1
# print(x)


# def find_even_index(arr):
# 	x = 0
# 	for i in range(len(arr)):
# 		while sum(arr[:i]) == sum(arr[i + 1:]):
# 			print(i)
# 			x += 1
# 			break
# 	if x == 0:
# 		print(-1)


# find_even_index([1,2,3,4,5,6])


# def mx(a1, a2):
# 	return -1 if a1 == [] and a2 == [] else max([abs(len(x) - len(y)) for x in a1 for y in a2])

# print(mx(
# 	a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"],
#     a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
# ))


# a = [1, 2, 3, 4, 5]
# b = [1, 1, 0, 0, 2, 2, 3, 3,]

# print(a[b])


# class C:
# 	def __init__(s, a):
# 		s.a = a
# 	def print_a(s):
# 		print(s.a)
# c = C(10)
# c.print_a()


# a = 50

# print(a ** 2)

# sum = 1 ** 2 + 3 ** 2 + 5 ** 2 + 8 ** 2 + 49 ** 2
# sum = 1 + 9 + 25 + 64 + 2401
# print(sum)

# x = (a ** 2 - (a - 1) ** 2) - 8 ** 2 - 5 ** 2 - 3 ** 2 - 1 ** 2
# print(x)


# def quicksum(packet):
#     alphabet = {' ': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
#     sum = 0
#     for i in packet:
#         sum += (packet.index(i) + 1) * alphabet[i]
#         print(packet)
#         packet = packet.replace(i, ' ', 1)
#         print(packet)
#         print(sum)
#     return sum

# print(quicksum("BBC"))


# from collections import Counter
# def mix(s1, s2):
#     c1 = Counter(s1)
#     c2 = Counter(s2)
#     cc1 = {}
#     cc2 = {}
#     for key in c1:
#         if key.islower() and c1[key] > 1:
#             cc1[key] = c1[key]
#     for key in c2:
#         if key.islower() and c2[key] > 1:
#             cc2[key] = c2[key]
#     sum = ''
#     for key in cc1:
#         if cc1[key] > cc2[key]:
#             sum += '1:' + key * cc1[key] + '/'
#         else:
#             sum += '2:' + key * cc2[key]
#     return sum
# print(mix("A aaaa bb c", "& aaa bbb c d")) # "1:aaaa/2:bbb"


# from collections import Counter
# def mix(s1, s2):
#     c1 = Counter(s1)
#     c2 = Counter(s2)
#     cc1 = {}
#     cc2 = {}
#     for key in c1:
#         if key.islower() and c1[key] > 1:
#             cc1[key] = c1[key]
#     for key in c2:
#         if key.islower() and c2[key] > 1:
#             cc2[key] = c2[key]
#     sum = ''
#     for key in cc1:
#         if cc1[key] > cc2[key]:
#             sum += '1:' + key * cc1[key] + '/'
#         else:
#             sum += '2:' + key * cc2[key]
#     return sum
# print(mix("Are they here", "yes, they are here")) # '2:eeeee/2:yy/=:hh/=:rr'


# def summation(num):
#     return eval('+'.join([str(x) for x in range(1, num + 1)]))

# print(summation(10))


# def find_outlier(arr):
#     odd = 0
#     even = 0
#     for i in arr:
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     if odd == 1:
#         for i in arr:
#             if i % 2 != 0:
#                 return i
#     elif even == 1:
#         for i in arr:
#             if i % 2 == 0:
#                 return i


# find_outlier([2, 4, 6, 8, 10, 3])


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr1 = [8, 9]
# length = len(arr1)
# print(arr[-length:])


def tick_toward(start, target):
    if start == target:
        return [start, target]
    elif start[0] != target[0] and start[1] == target[1]:
        y = target[0] - start[0]
        arr = []
        x = 0
        if y >= 0:
            while len(arr) < y + 1:
                z = (start[0] + x, start[1])
                arr.append(z)
                x += 1
            return arr
        else:
            while x > y - 1:
                z = (start[0] + x, start[1])
                arr.append(z)
                x -= 1
            return arr
    elif start[0] == target[0] and start[1] != target[1]:
        y = target[1] - start[1]
        arr = []
        x = 0
        if y >= 0:
            while len(arr) < y + 1:
                z = (start[0], start[1] + x)
                arr.append(z)
                x += 1
            return arr
        else:
            while x > y - 1:
                z = (start[0], start[1] + x)
                arr.append(z)
                x -= 1
            return arr
    else:
        y1 = target[0] - start[0]
        y2 = target[1] - start[1]
        arr = []
        x = 0
        y = 0
        if y1 == y2:
            while y1 != x - 1:
                z = (start[0] + x, start[1] + y)
                x += 1
                y += 1
                arr.append(z)
        elif y1 > y2:
            while y2 != y:
                z = (start[0] + x, start[1] + y)
                x += 1
                y += 1
                arr.append(z)
            while y1 != x - 1:
                z = (start[0] + x, start[1] + y)
                x += 1
                arr.append(z)
        else:
            while y1 != x:
                z = (start[0] + x, start[1] + y)
                x += 1
                y += 1
                arr.append(z)
            while y2 != y - 1:
                z = (start[0] + x, start[1] + y)
                y += 1
                arr.append(z)
        return arr

# print(tick_toward((1, 1), (2, 2)))


# arr = [int(x) for x in string if int(x) % 2 != 0]


# def comp(a1, a2):
#     if a1 is None or a2 is None:
#         return False
#     else:
#         a3 = []
#         for i in a2:
#             a3.append(i ** 0.5)
#         a1 = sorted(a1)
#         print(a1)
#         a3 = sorted(a3)
#         print(a3)
#         return a1 == a3

# a1 = [30]
# a2 = [901]
# print(comp(a1, a2))


# def camel_case(string):
#     return string.title().replace(' ', '')

# print(camel_case("test case"))


# from itertools import combinations as comb


# def choose_best_sum(t, k, ls):
#     return max(sorted([sum(i) for i in comb(ls, k) if sum(i) <= t]), default=None)

# xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# print(choose_best_sum(430, 8, xs))


# def square_digits_sequence(n):
#     arr = []
#     while n not in arr:
#         arr.append(n)
#         n = eval('+'.join([str(int(i) ** 2) for i in str(n)]))
#     arr.append(n)
#     return len(arr)

# print(square_digits_sequence(16))


