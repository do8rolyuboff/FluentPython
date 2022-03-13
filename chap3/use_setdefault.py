"""Строит индекс, отображающий слово на список его вхождений"""
import re
from use_get import zen

index = {}


def use_setdefault(zen: str):
	for line_no, line in enumerate(zen.split('\n'), 1):
		for match in re.compile('\w+').finditer(line):
			word = match.group()
			column_no = match.start() + 1
			location = (line_no, column_no)
			index.setdefault(word, []).append(location)

	for word in sorted(index, key=str.upper):
		print(word, index[word])


if __name__ == '__main__':
	use_setdefault(zen)
