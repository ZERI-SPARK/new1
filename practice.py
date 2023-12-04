# string = "A man is a ; , a is nam A"
# palindrome 
# lowsercase and unwanted symbols and whitespaces unko remove krna hai
# output = "amanisaaisnama"
# not palindrome then output false
# time complexity - O(n)

def illegalChar(string : str) -> str:
    invalid = r'<>{}[];:,.-_)(&^%$#@!"\' '

    for char in invalid:
        string = string.replace(char, '')

    return string

string = "A man is a ; , a si nam A"
string = illegalChar(string.lower())

if string == string[::-1]:
    print(string)
else:
    print(False)



