emoticon_dic = { ':-)': 0, ':-(': 0, }
s = input()
for key in emoticon_dic.keys():
    emoticon_dic[key] = s.count(key)

if sum(emoticon_dic.values()) == 0:
    print('none')
elif emoticon_dic.get(':-)') == emoticon_dic.get(':-('):
    print('unsure')
elif emoticon_dic.get(':-)') > emoticon_dic.get(':-('):
    print('happy')
else:
    print('sad')