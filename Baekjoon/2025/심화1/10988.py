text = input()

value = 1

for idx, val in enumerate(text):
    if val != text[len(text) -1 -idx]:
        value = 0

print(value)