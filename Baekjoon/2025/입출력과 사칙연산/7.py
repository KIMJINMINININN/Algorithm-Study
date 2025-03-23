text = input("")
if  (all(('A' <= char <= 'Z' or 'a' <= char <= 'z') for char in text)
        and text.islower()
        and len(text) < 51):
    print(text + '??!')
else:
    print("알파셋이 대문자가 있던지 글자의 50자가 넘었습니다.")