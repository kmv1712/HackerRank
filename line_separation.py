string = "AABCAAADA"
n = 1

#Ключевая строка беорет строку и разделяет ее на подстроки например если n 3 то будет [AAB, CAA, ADA]
wrap_list = [string[i:i+n] for i in range(0, len(string), n)]
for item in wrap_list:
    y = []
    for x in item:
        if x not in y:
            y.append(x)
    print(''.join(y))
