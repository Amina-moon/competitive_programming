def swap_case(s):
    lst=[]
    for i in range(len(s)):
        if s[i]==s[i].lower():
            lst.append(s[i].upper())
        elif s[i]==s[i].upper():
            lst.append(s[i].lower())
        joined=''.join(lst)
    return joined

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
