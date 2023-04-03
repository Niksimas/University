def longest_str(x, y):
    spisok = [x, y]
    maximym = max(spisok, key=len)
    return maximym


def max_len(x, y):
    spisok = [x, y]
    maximym = max(spisok, key=len)
    return len(maximym)

s = ['123456', 'Apple', 'Dog', '33232', 'asdasdaasdasd', 't']
for i in range(len(s)):
    for j in range(i+1, len(s)):
        print(s[i], s[j], '->', longest_str(s[i], s[j]), max_len(s[i], s[j]))
