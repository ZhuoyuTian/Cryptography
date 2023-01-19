import itertools as it
# for e in it.permutations('ABCD', 4):
#     print(''.join(e), end=', ')
#密文分块（4）
#计算统一性距离，d = 4时，统一性距离很小，所以我们这里只取一个块就能找出规律
def change_to_block(sentance):
    ob_sentance = sentance[0:4]
    return ob_sentance
print(change_to_block('ISTIACSERTE'))

#排列组合
for e in it.permutations(change_to_block('ISTIACSERTE'), 4):
    print(''.join(e), end=', ')