"""У кортежей две функции: использование в качестве неизменяемых
   списков и в качестве записей с неименован¬ ными полями."""

# Примеры неизменяемых списков:
lax_coordinates = (33.9425, -118.408056)  # Широта и долгота международного аэропорта Лос-Анджелеса.
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)  # Данные о Токио.
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]  # [(код_страны,номер_паспорта)].
for passport in sorted(traveler_ids):
	print('%s/%s' % passport)
for country, _ in traveler_ids:
	print(country)

# Cемантика каждого элемента данных определяется его позицией

"""Распаковка данных"""
# Параллельное присваивание
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates  # tuple unpacking
print(latitude, longitude)
t = (20, 8)
print(divmod(*t))

"""Использование * для выборки лишних элементов"""
a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)

a, *body, c = range(5)
print(a, body, c)

"""Распаковка вложенного кортежа"""
metro_areas = [
	('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
	('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
	('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
	('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
	('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
	if longitude <= 0:
		print(fmt.format(name, latitude, longitude))

# Именованные кортежи
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(type(tokyo))
print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)  # City(*delhi_data) делает то же самое
print(delhi._asdict())
for key, value in delhi._asdict().items():
	print(key + ':', value)
