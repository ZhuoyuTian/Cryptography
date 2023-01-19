dict_a = {chr(i): (i-97) for i in range(97, 123)}
print(dict_a)
new_dict = {v : k for k, v in dict_a.items()}
print(new_dict)
#1. 字母变数字
def char_to_num(sentance):
    ob_sentance = list(sentance)
    ob_num = []
    for i in range(len(ob_sentance)):
        ob_num.append(dict_a[ob_sentance[i]])
    return ob_num
sentance = "moilvgofxtmzflz"
print(char_to_num(sentance))
ob_num = char_to_num(sentance)
#2. 暴力破解
def guess(ob_num):
    for k in range(26):
        p_num = []
        p_char = []
        for i in ob_num:
            plain_num = (i-k) % 26
            p_num.append(plain_num)
        print(k)
        print(p_num)
        for i in range(len(p_num)):
            p_char.append(new_dict[p_num[i]])

        plain_char =  "".join(p_char)
        print(plain_char)
guess(ob_num)
