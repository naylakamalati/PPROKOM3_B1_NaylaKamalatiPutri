z=[1, 3, 2, 4, 'Alice', 'Bob']
z.sort(key=str)
print(z)
print("Hello there!\nHow are you?\n\'m doing fine.")
multi_line = """Hello there!
I'm fine."""
print(multi_line)
spam = 'Hello World'
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Sinamon']))
print('ABC'.join(['My', 'name', 'is', 'Sinamon']))
print ('My name is Simon'.split())
print('MyABCnameABCis ABCSimon'.split('ABC'))