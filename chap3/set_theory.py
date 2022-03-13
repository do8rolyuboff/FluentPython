my_list = ['spam', 'spam', 'eggs', 'spam']
print(set(my_list))
print(list(set(my_list)))


needles = '12345'
haystack = '123456789'

found = len(set(needles) & set(haystack))
print(found)
found = len(set(needles).intersection(haystack))
print(found)
