#!/usr/bin/env python
"""
Simple check file hash sum
Based on the python facade pattern and hashlib
Hash algorithms: md5, sha1, sha256, sha384, sha512
"""
import hashlib
import re

print ('''___ __ ___  _  _ ____ ____ _  _
[_  |_  |   |__| |__| |__  |__|    
|_] [_  |   |  | |  | ___] |  |  v1.0.1\n''')

alg = {"md5": 1, "sha1": 2, "sha256": 3, "sha384": 4, "sha512": 5}
printinline = ', \n'.join(f'{key}: {value}' for key, value in alg.items())
print(printinline)

_input = int(input('\nInput hash algorithm value: '))
fileNameWithPath = input('Input file with full path: ')
file = open(fileNameWithPath, 'rb').read()

pattern = r'([^/\\]+$)'
text = re.search(pattern, fileNameWithPath, flags=0).group()

class MD5:
	def md5(self):
		print(f'\nHash sum file "{text}"', hashlib.md5(file).hexdigest())

class SHA1:
	def sha1(self):
		print(f'\nHash sum file "{text}"', hashlib.sha1(file).hexdigest())

class SHA256:
	def sha256(self):
		print(f'\nHash sum file "{text}"', hashlib.sha256(file).hexdigest())

class SHA384:
	def sha384(self):
		print(f'\nHash sum file "{text}"', hashlib.sha384(file).hexdigest())

class SHA512:
	def sha512(self):
		print(f'\nHash sum file "{text}"', hashlib.sha512(file).hexdigest())

class hashFunction():
	def __init__(self):
		self.md5hash = MD5()
		self.sha1hash = SHA1()
		self.sha256hash = SHA256()
		self.sha384hash = SHA384()
		self.sha512hash = SHA512()

	def calculate(self):
		for _ in alg.items():
			if _input == 1:
				return self.md5hash.md5()
			elif _input == 2:
				return self.sha1hash.sha1()
			elif _input == 3:
				return self.sha256hash.sha256()
			elif _input == 4:
				return self.sha384hash.sha384()
			elif _input == 5:
				return self.sha512hash.sha512()
			else:
				print('incorrect input')

def main():
	"""
	main
	"""

if __name__ == '__main__':
	h = hashFunction()
	h.calculate()
