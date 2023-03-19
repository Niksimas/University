def longest_str3(x,y,z):
    spisok = [x, y, z]
    maximym = max(spisok, key=len)
    return maximym


def max_len3(x,y,z):
    spisok = [x, y, z]
    maximym = max(spisok, key=len)
    return len(maximym)




s = ['123456', 'Apple', 'Dog', '33232', 'asdasdaasdasd', 't']
for i in range(len(s)):
    for j in range(i+1, len(s)):
        for k in range(j+1, len(s)):
            print(s[i], s[j], s[k], '->', longest_str3(s[i], s[j], s[k]), max_len3(s[i], s[j], s[k]))