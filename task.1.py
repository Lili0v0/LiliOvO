from pprint import pprint
list = [{'dec': num, 'bin': bin(num), 'oct': oct(num), 'hex': hex(num)} for num in range(16)]
pprint(list)