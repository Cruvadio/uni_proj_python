__count_randint__ = True
__a__= 0
__b__= 0
__d__= 0
__res_randrange__ = 0
__count_randrange__ = 0


def randint(a, b):
	global __count_randint__
	__count_randint__ = not __count_randint__
	if __count_randint__:
		return b
	else:
		return a
	
	
def randrange(a, *args):
	global __count_randrange__
	global __res_randrange__ 
	global __a__
	global __b__
	global __d__
	
	if len(args) < 1:
		b, a , d = a, 0, 1
	elif len(args) < 2:
		b, d = args[0], 1
	else:
		b, d = args[0], args[1]
	if a == __a__ and b == __b__ and d == __d__:
		if (__res_randrange__   + d < b and d > 0 or __res_randrange__ + d > b and d < 0 )and __count_randrange__:
			__res_randrange__   += d
		else:
			__res_randrange__   = a + (b + __res_randrange__) % d
		__count_randrange__ += 1
	else:
		__res_randrange__  = a
		__count_randrange__ = 1
		__a__ = a
		__b__ = b
		__d__ = d
	return __res_randrange__ 
