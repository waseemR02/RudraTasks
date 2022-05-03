"""Task is to imitate a module like the zen module(Import this) """

s = """Unfuhyudsu yd Hkthq

Jycu yd Hkthq xqi ruud luho fhetksjylu.Qtqhix rxqy yi qd unsubbudj juqsxuh.
Jxekwx yj sqd ru xusjys qj jycui,y udzeo jxu jycu jxuhu buqhdydw dum jxydwi
qdt tyisyfbydu.Qbie co fuuhi qhu huqbbo weet qdt admbutwuqrbu jxqj y wuj je buqhd q bej vhec
jxuc. Y xefu y sqd sedjydku je ru yd jxyi juqc veh cehu jxqd 2 muuai

"""

d = {}

for smallCaps in (65,97):
	for char in range(26):
		d[chr(char + smallCaps)] = chr((char + 10) % 26 + smallCaps)

print(''.join([d.get(char,char) for char in s]))
