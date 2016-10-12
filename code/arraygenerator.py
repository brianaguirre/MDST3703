__author__ = 'BrianAguirre'


f = open("data.txt", 'r')
text = f.read()
for i in range(0,51):
    print(str(text.splitlines()[i].split()) + ",")