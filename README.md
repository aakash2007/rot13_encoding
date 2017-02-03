# rot13_encoding

Requires Python3

Download the files and in the folder run:
```
	$ python3 main.py
```

It works on following logic:
```
d = {}

for c in (65,97):
	for i in range(26):
		d[chr(i+c)] = chr((i+13)%26 +c)

"".join([d.get(c, c) for c in s])
```
