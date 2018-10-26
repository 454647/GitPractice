import random,string


def print_something(N):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))


print_something(6)
