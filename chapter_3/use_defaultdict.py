"""Строит индекс, отображающий слово на список его вхождений"""

import sys
import re
import collections
from use_get import zen


def use_defaultdict(zen: str):
	index = collections.defaultdict(list)
	for line_no, line in enumerate(zen.split('\n'), 1):
		for match in re.compile('\w+').finditer(line):
			word = match.group()
			column_no = match.start() + 1
			location = (line_no, column_no)
			index[word].append(location)

	for word in sorted(index, key=str.upper):
		print(word, index[word])


if __name__ == '__main__':
	use_defaultdict(zen)
