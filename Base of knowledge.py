# Сложение
print(1+2)
# Вычитание
print(2-1)
# Уиножение
print(2*2)
# Деление
print(4/2)
# Возведение в степень
print(3**2)
# Определение частного (выводит результат деления без остатка)
print(9//2)
# Деление по модулю (выводит остаток от деления)
print(9%2)
# Тип данных Integer целое число 
print(int(5))
# Тип данных Float дробное число
print(float(4))
# Тип данных String строки (какие-то данные)
print(str(5))
# Обратный слэш отмена последующего действия 
print('Hello \'World')
# Вывод текста на новую строку 
print('Новая \nстрока')
# Многострочный текст
print('''Многострочный 
	текст''')
# Разделителем земля _ можно разделять цифры в числах
x = 1234_5678_9012_3456
print( x )
# end='' переносит данные с разных строк в одну и можно добавить пробел запятую и другие разделители
for x in range( 3 ):
	print( x, end='')
# sep='' удаляет указанный элемент (можно удалить пробелы и запятые)
for x in range( 3 ):
	print( x, sep='_' )
# Функция Print вывода на экран
print('Hello World')
# Функция Input текст запроса
input('What is your name?: ')
# Переменная Test, переменная не может начинаться с цифр и спец символов
test=10
# Знак + в функции означает конкатенация (присоединение строк)
print('one'+'plus'+'3')
# Знак * в функции означает умножение строк
print('Hello'*3)
# Удалить переменную del
test=1
del test
# Метасинтаксические переменные foo bar
foo='bar'
# Уместный оператор += -= *= /= %=
test=1
test+=1
print(test)
# Булево значение
test=True
test2=False
# Сравнение значений == означает равно
print(10==10)
# Сравнение занчений != означает не равно
print(10!=11)
# Сравнение значений < означает меньше
print(1<2)
# Сравнение значений > означает больше
print(3>2)
# Сравнение значений <= означает меньше либо равно
print(3<=3)
# Сравнение значений > означает больше либо равно
print(4>=4)
# Лексиграфическое сравнение строк (сравнение по весу букв)
print('Test'<'Tesa')
# Функция сравнения if (если это то вот это)
test4='Hello'
if test4=='Hello':
	print('Hello')
# Функция сравнения elif (если не это то вот это)
test4='Hello'
if test4=='Hi':
	print('Hi')
elif test4=='Hello':
	print('Hello')
# Функция сравнения else (если не это и не это то вот это) 
test4='Hello'
if test4=='Hi':
	print('Hi')
elif test4=='Hi':
	print('Hi')
else:
	print('Nice day')
# Оператор not отрицание
test4='Hello'
if not test4=='Hi':
	print('Hello')
# Приорететность операций 
print(1+3*5/3**5)
# Функция цикл while (запускает бесконечный цикл)
test5=True
while test5:
	print('Цикл запущен и остановлен')
	test5=False
# Команда break заставляет цикл принудительно остановиться
i=1
while 1==1:
	print('Hello '+str(i))
	i+=1
	if i==5:
		break
# Команда continue заставляет цикл продолжить действие
number=0
while number<=10:
	number+=1
	if (number%2)!=0:
		continue;
	print('Четное число '+str(number))
# Обозначение списка []
test6=[1,2,3]
print(test6[2])
# Оператор in означает в
test=['Alex Mercer','Tony Stark','Lenny Flawes']
if 'Alex Mercer'in test:
	print('Alex Mercer is in list')
# Оператор (метод) .append означает добавить элемент в конец списка
test=[]
test.append('Hello')
print(test)
# Функция len подсчитывает количество элементов в списке
test=[5,3,2,5,6,7]
test.append('5')
print('В массиве test у нас находится '+str(len(test))+' элементов')
# Оператор (метод) remove убирает элемент из списка
test=[5,3,2,5,6,7]
test.remove(5)
print('В массиве test у нас находится '+str(len(test))+' элементов')
# Оператор (метод) insert означает добавить элемент в нужное место списка
test=[1,2,3]
test.insert(0,4)
print(test)
# Функция max выводит на экран наибольший элемент в списке
test=[1,2,3]
print('В списке максимальное значение '+str(max(test)))
# Функция min выводит на экран наименьший элемент в списке
test=[1,2,3]
print('В списке минимальное значение '+str(min(test)))
# Оператор (метод) .count для подсчета количества элементов в списке
test=[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
print( 'В списке всего ' + str( test.count( 4 ) ) + ' четверок' )
# Оператор (метод) reverse переворачивает список
test=[1,2,3,4,5]
test.reverse()
print(test)
# Функция range создает список определенного диапазона
numbers=range(10)
print(numbers)
# Функция list преобразует свой аргумент в список определенного диапазона
numbers=list(range(0,11,2))
print(numbers)
# Цикл for in означает для каждого элемента в списке
numbers=[1,2,3,4,5]
for element in numbers:
	print(str(element)+'!')
# Функция def определяет собственную функцию
def print_spam():
	print('spam')
	print('spam')
print_spam()
# Функция return возвращает определенный аргумент
def max(x,y):
	if x>y:
		return x
	else:
		return y
print(max(5,10))
# Описание функции обозначается '''Описание'''
def Howdy_ho():
	'''Описание функции'''
	print('Howdy_ho')
print(Howdy_ho.__doc__)
# Импортирование модуля import вызов рандомного числа методом random.randit
import random
print(random.randint(1,100))
# Модуль math нужен для работы с математикой
import math
# Импорт модуля с пометкой * извлекает все методы
import math*
# Виды ошибок (самый распространенный)
ImportError  - ошибка импорта (нет такого модуля)
IndexError   - ошибка нумерации индекса (ошибочный порядковый номер)
NameError    - ошибка имени переменной (не существует такой переменной)
SyntaxError  - ошибка синтаксиса ()
TypeError    - ошибка типа переменной (не тот тип переменной)
ValueError   - ошибка ввода переменной (не соответствие вводимой переменной)
# Функция try пробует выполнить действие, функция except определяет и делает исключение
try:
	print(7/0)
except ZeroDivisionError:                     # если не указывать вид исключения будут ловиться все виды исключений
	print('Зафиксировано деление на ноль')    # также можно пропустить исключение командой pass
finally:
	print('Конец проверки.')
print('Программы завершена!')
# Функция eval ищет в указанном блоке кода синтаксическую ошибку
eval('print(7/4)a')
# Функция raise выкидывает введенный нами тип исключения
pogoda = 'Bed'
if pogoda == 'Bed':
	raise TypeError('Тестовая ошибка')
# Функция assert добовляет условие при не соблюдении которого выбивает ошибку
if  test(number):
	assert number > 0, 'Number should be bigger than 0.'
	print(str(number))
test(-10)
# Функция open открывает файл в python
file = open('test.txt')
# Режимы чтения файлов
r - Чтение файла
w - Перезапись файла
a - Добавление файла
b - Binary mode
# Конструкция with позволяет создать в блоке собственную переменную
# и после выполнения закрывает файл
with open('test.txt','r') as f:
	print(f.read())
# Переменная None выводит ничего (всё равно что пусто или 0)
test = None
if(test == None):
	print(test)
# Dictionary - Словарь
test = {
	'ключ1':'значение1',
	'ключ2':'значение2',
}
print(test['ключ1'])
# Таким образом можно оформить красивую таблицу
test = {
	'ключ1':'значение1',
	'ключ2':'значение2',
}
for k, v in test.items():
    print('{0:20} - {1:10}'.format(k, v))
# Метод .get выдает искомое значение, в случае его отсутствия выдает None (не выдает ошибку)
contacts = {
	'Андрей Змеевский':'+153654665132',
	'Никита Хогвартс' :'+265465416351',
	'Роман Таненбаум' :'+151635415513'
}
print(contacts.get('Никита Хогвартс','Номер не найден!'))
# Функция pass пропускает бредыдущий блок кода
def main():
	pass
print('test')
# Тип данных Кортеж (Tuple) нельзя изменить можно указывать в скобках можно без
names = ('Jone','James','Jack')
names = 'Jone','James','Jack'
print(names[0])
# Индескация списка [List indexing] вывод определенной части списка
digits = [1,2,3,4,5,6,7,8,9,10]
digits2 = digits[2:5]
print(digits2)
# Вывод данных из серидины списка
sqs = [0,1,4,9,16,25,36,49,64]
print(sqs[4:7])
# Вывод с начала списка до заданного значения
sqs = [0,1,4,9,16,25,36,49,64]
print(sqs[:7])
# Вывод от заданного значения до конца списка
sqs = [0,1,4,9,16,25,36,49,64]
print(sqs[4:])
# Третий параметр индексирования это шаг индексирования
sqs = [0,1,4,9,16,25,36,49,64]
print(sqs[::2])
# Индексация списка с конца
digits = [1,2,3,4,5,6,7,8,9,10]
digits2 = digits[-3]
print(digits2)
# Реверсирование (разворот) списка
digits = [1,2,3,4,5,6,7,8,9,10]
digits2 = digits[::-1]
print(digits2)
# Форматирование строк
# первый метод % placeholder (знак процента)
# второй метод .format()

# Стандартный метод вывода без форматирования
name = 'Jone'
age = 21
print('Hello, ' + str(name) + '!\nYou are ' + str(age) + ' years old!')

# Форматирование с помощью % placeholder
name = 'Jone'
age = 21
print('Hello, %s!\nYou are %d years old!' % (name, age))
# %s - плэйсхолдер строки
# %d - плэйсхолдер числа
# %f - плэйсхолдер дроби

# Форматирование с помощью метода format()
name = 'Jone'
age = 21
print('Hello, {0}!\nYou are {1} years old!'.format(name, age))

# Персонализирование аргументов
person_name = 'Jone'
person_age = 21
print('Hello, {name}!\nYou are {age} years old!'.format(name = person_name, age = person_age))

# Фопматирование строки с использованием словаря
human = {
	'name':'Jone',
	'age': 21
}
print('Hello, {person[name]}!\nYou are {person[age]} years old!'.format(person = human))

# Фопматирование строки с применением заполнителя слева справа с центрирование текста
input_str = 'Jone'
print('{0:*^8}'.format(input_str))
print('{0:_<8}'.format(input_str))
print('{0:->8}'.format(input_str))
# Jone**** < заполнение справа
# ****Jone > заполнение слева
# **Jone** ^ заполненеие по центру

# Добавление заполнителя в случае не симметричного расположения текста (пример ***Jessy**)
input_str = 'Jessy'
length = 10
if(len(input_str) % 2):
	length += 1
print(('{0:*^' + str(length) +'}').format(input_str))
# Функции для работы со строками и числами
fruits = ['Лимоны', 'Яблоки', 'Киви', 'Ананас', 'Клубника']
members = 'James,Jonny,Jessie,Jack,John'
# join, replace, startswith, endswith, lower, upper, split, min, max, abs, sum
# Преобразование списка в строку с помощью метода .join с добавлением ','
print(','.join(fruits))
# Преобразование списка в строку с помощью метода .join с добавлением ' - '
print(' - '.join(fruits))
# Замена аргумента с помощью метода .replace
print('Привет, Петр!'.replace('Петр', 'Александр'))
# Сортировка с помощью метода .startswith
name = input('Введите Ваше имя: ')
if(name.startswith('А')):
	print('Добро пожаловать!\nВы находитесь в элитном клубе людей, имена которых начинаются с буквы "А"!')
else:
	print('Добро пожаловать!')
# Сортировка с помощью метода .startswith с применением метода .lower (не чувствительность к регистру)
name = input('Введите Ваше имя на любом языке: ')
if(name.lower().startswith('а') or name.lower().startswith('a')):
	print('Добро пожаловать!\nВы находитесь в элитном клубе людей, имена которых начинаются с буквы "А"!')
else:
	print('Добро пожаловать!')
# Пример работы метода .lower
input_str = input('Enter text: ')
print(input_str.lower())
# Применение метода .endwith
word = 'Hello drudving'
if(word.endswith('ing')):
	print('Hello ING!')
else:
	print('WTF!')
# Пример работы метода .upper
input_str = input('Enter text: ')
print(input_str.upper())
# Метод split разъединяет заданную строку (противоположно методу .join)
print(members.split(','))
# Функция min возвращает самое маленькое число из списка
print(min([5,10,8,65,233,4287,56,1,58]))
# Функция max возвращает самое большое число из списка
print(max([5,10,8,65,233,4287,56,1,58]))
# Функция abs передает абсолютное число (то есть число без знака)
print(abs(235))
print(abs(-325))
# Функция sum передает сумму всех элементов в списке
print(sum([5,15,8,65]))
# Пример из урока №1 Функции высшего порядка (функции принимают другие функции в качестве аргументов, либо возвращают их как результат)
def apply_twice(func, arg):
	return func(func(arg))
def add_five(x):
	return x + 5
print(apply_twice(add_five, 10))
# Пример из урока №2 (чистая функция возвращает значения только от своих аргументов)
def pure_function(x, y):
	temp = x + 2 * y
	return temp / (2 * x + y)
# функция impure не является чистой так как она изменила свое состояние some_list
some_list = []
def impure(arg):
	some_list.append(arg)
# named functuon именная функция
def polynomial(x):
	return x ** 2 + 5 * x + 4
print(polynomial(-4))
# lambda анонимная функция
print((lambda x: x ** 2 + 5 * x + 4)(-4))
# Пример №1 функция map применяет другую функцию к списку
def add_five(x):
	return x + 5
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)
# можно записать через ононимную функцию lambda
nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x + 5, nums))
print(result)
# Пример №2 функция filter удаляте элементы списка не подходящие под условие функции
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)
# Перевод чисел из одной системы исчисления в другую
print(0b111101)                 # запись в двоичной системе исчисления
print(0o0732)                   # запись в восьмеричной системе исчисления
print(0xfa0b)                   # запись в шестнадцатеричной системе исчисления
print(int('z3f', base = 36))    # запись в тридцатишестиричной системе исчисления
x = 127
print(bin(x))                   # перевод из десятеричной системы в двоичную
print(oct(x))                   # перевод из десятеричной системы в восьмеричную
print(hex(x))                   # перевод из десятеричной системы в шестнадцатиричную
# перевоод в любую систему исчисления, указать в base
base = 7
x = int(input())
while x > 0:
	digits = x % base
	print(digits, end = '') # число выводит задом наперед!!!
	x //= base
# Декораторы - декорирование функции без ее изменения
def decor(func):
	def wrap():
		print('============')
		func()
		print('============')
	return wrap
def print_text():
	print('Hello world!')
decorated = decor(print_text)
decorated()
# @decor декорирование функции компактный вариант
def decor(func):
	def wrap():
		print('============')
		func()
		print('============')
	return wrap
@decor
def print_text():
	print('Hello world!')
print_text()
# Множества set работают так же как и списки только данные не индексированы
num_set = {1, 2, 3, 4, 5}
word_set = set(['spam', 'eggs', 'sausage'])
print(3 in num_set)
print('spam' not in word_set)
# методы для работы с множествами
nums = {1, 2, 1, 3, 4, 5, 6}
nums.add(-7)                # метод .add добавляет элемент во множество
if -2 in nums:
	nums.remove(3)          # метод .remove удаляет указанный элемент из множества
elif 5 not in nums:
	nums.add(-5)
elif 9 in nums:
	nums.remove(4)
else:
	nums.add(8)
nums.pop()                  # метод .pop удаляет случайный элемент из множества
print(nums)
# Операторы для работы с множествами
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second)       # оператор обединения, объединяет два множества
print(first & second)       # оператор пересечения, возвращает только те элементы которые есть в обоих множествах
print(first - second)       # оператор разности, возвращает элементы только из первого множества
print(second - first)       # оператор разности, возвращает элементы только из первого множества
print(first ^ second)       # оператор симметрической разности, возвращает все элементы обоих множеств кроме пересекающихся
# Модуль itertools стандартная библиотека, один тип функций в этой библиотеке это бесконечные итераторы
from itertools import count                         # count выводит все элементы в соответствии с заданными параметрами
for i in count(3):
	print(i)
	if i >= 11:
		break

from itertools import accumulate, takewhile
nums = list(accumulate(range(8)))                   # accumulate выводит последовательную сумму всех элемнтов
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))      # takewhile выводит (циклически) значения

from itertools import takewhile
nums = [2, 4, 6, 7, 9, 8]
a = takewhile(lambda x: x % 2 == 0, nums)           # print[2, 4, 6] цифра 8 не входит в заданный диапазон, потому что цикл прерывается на цифре 7 (цикл выдает False и прерывается)
print(list(a))

from itertools import product, permutations
letters = ('A', 'B')
print(list(product(letters, range(2))))             # product комбинирует све заданные значния в соответствии с заданными условиями
print(list(permutations(letters)))                  # permutations комбинирует все заданные значения между собой
# Magic methods (dunders)
# __add__        - +
# __mul__        - -
# __truediv__    - *
# __floordiv__   - /
# __mod__        - %
# __pow__        - **
# __and__        - &
# __xor__        - ^
# __or__         - |

class Vector2D:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __add__(self, other):
		return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

class SpecialString:
	def __init__(self, cont):
		self.cont = cont

	def __truediv__(self, other):
		line = '=' * len(other.cont)
		return '\n'.join([self.cont, line, other.cont])

spam = SpecialString('spam')
hello = SpecialString('Hello world!')
print(spam/ hello)

# __it__      - <
# __le__      - <=
# __eq__      - ==
# __ne__      - !=
# __gt__      - >
# __ge__      - >=

class SpecialString:
	def __init__(self, cont):
		self.cont = cont

	def __gt__(self, other):
		for index in range(len(other.cont) + 1):
			result = other.cont[:index] + '>' + self.cont
			result += '>' + other.cont[index:]
			print(result)

spam = SpecialString('spam')
eggs = SpecialString('eggs')
spam > eggs

import random

class VagueList:
	def __init__(self, cont):
		self.cont = cont

	def __getitem__(self, index):
		return self.cont[index + random.randint(-1, 1)]

	def __len__(self):
		return random.randint(0, len(self.cont) * 2)

vague_list = VagueList(['A', 'B', 'C', 'D', 'E'])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
# Сокрытие данных
class Queue:
	def __init__(self, contents):
		self._hiddenlist = list(contents)

	def push(self, value):
		self._hiddenlist.insert(0, value)

	def pop(self):
		return self._hiddenlist.pop(-1)

	def __repr__(self):
		return 'Queue({})'.format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

# Методы класса (обычно оформляются с помощью декоратора @classmethod)
class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def calculate_area(self):
		return self.width * self.height

	@classmethod
	def new_square(cls, side_length):
		return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())
# Статический метод класса
class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings

	@staticmethod
	def validate_topping(topping):
		if topping == 'pineapple':
			raise ValueError('No pineapples!')
		else:
			return True

ingredients = ['cheese', 'onions', 'spam']
if all(Pizza.validate_topping(i) for i in ingredients):
	pizza = Pizza(ingredients)







































