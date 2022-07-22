import jieba

text = "皇家幼猫粮里头VD和钙磷的加持 而且还是高易消化蛋白哦 幼猫消化更轻松吸收更好哟~ 虽然幼猫都是少食多餐的 但是抵不住它们馋嘴呀 " \
       "时不时的加餐我就会选同品牌的幼猫湿粮 产自奥地利的幼猫专属"

#
jieba.add_word("猫", 102200, 'n')
jieba.add_word("幼猫")
jieba.add_word("猫粮")
lst = jieba.cut(text, cut_all=True, HMM=False)
temp = []
for word in lst:
    temp.append(word)
print(temp)

lst = jieba.cut_for_search(text, HMM=True)
temp = []
for word in lst:
    temp.append(word)

print(temp)
