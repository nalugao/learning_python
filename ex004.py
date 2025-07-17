n = input('Insert something: ')
print(type(n))
print('Is it numeric? ', n.isnumeric()) #if the result is numeric
print('Is it numeric or a str? ', n.isalnum()) #if the result is a number or str
print('Is it a str? ', n.isalpha()) #if the result is a str
print('Is it in upper case? ', n.isupper()) #if the str is with caps look
print('Is it a title? ', n.istitle()) #if the str has upper letter and lower ones