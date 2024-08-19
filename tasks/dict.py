# dictinary = dict.fromkeys('abcd', 122)
# print(dictinary)

# {'a': 122, 'b': 122, 'c': 122, 'd': 122}

# dictinary['a'] = 'm'
# print(dictinary)

# # {'a': 'm', 'b': 122, 'c': 122, 'd': 122}

# 1
import re

exemple_text = """Little girl, little girl Why are you crying? Inside your restless soul your heart is dying Little one, little one Your soul is purging Of love and razor blades Your blood is surging Runaway From the river to the street And find yourself with your face in the gutter Your a stray for the salvation army There is no place like home When you got no place to go Little girl, little girl Your life is calling The charlatans and saints of your abandon Little one little one The sky is falling The lifeboat of deception is now sailing In the wake all the way No rhyme or reason Your bloodshot eyes Will show your heart of treason Little girl little girl You dirty liar You're just a junkie Preaching to the choir Runaway To your lost tranquility And find yourself with your face in the gutter Your a stray for the dregs of humanity There is no place like home When you got no place to go The traces of blood Always follow you home Like the Mascara tears From your getaway Your walking with blisters And running with shears So unholy. Sister of grace. Runaway From the river to the street And find yourself with your face in the gutter You're a stray for the salvation army There is no place like home When you got no place to go"""

words = re.split(r'[\?\.\!, \n]', exemple_text.lower())

exemple_dict = {}

for word in words:
    # if word not in exemple_dict:
    #     exemple_dict[word] = 1
    # else:
    #     exemple_dict[word] += exemple_dict[word] + 1

    exemple_dict[word] = exemple_dict.get(word, 0) + 1

new_dict = {}

for key, value in exemple_dict.items():
    new_dict[value] = new_dict.get(value, []) + [key, ]

for key in sorted(new_dict, reverse=True):
    print(f" {key} : {new_dict[key]}")


'''
 18 : ['the']
 16 : ['your']
 10 : ['little']
 9 : ['is']
 7 : ['of', 'to', 'no']
 6 : ['girl', '', 'you', 'and', 'place']
 5 : ['with']
 4 : ['one', 'in', 'a', 'like', 'home']
 3 : ['runaway', 'from', 'find', 'yourself', 'face', 'gutter', 'stray', 'for', 'there', 'when', 'got', 'go']
 2 : ['soul', 'heart', 'blood', 'river', 'street', 'salvation', 'army', "you're"]
 1 : ['why', 'are', 'crying', 'inside', 'restless', 'dying', 'purging', 'love', 'razor', 'blades', 'surging', 'life', 'calling', 'charlatans', 'saints', 'abandon', 'sky', 'falling', 'lifeboat', 'deception', 'now', 'sailing', 'wake', 'all', 'way', 'rhyme', 'or', 'reason', 'bloodshot', 'eyes', 'will', 'show', 'treason', 'dirty', 'liar', 'just', 'junkie', 'preaching', 'choir', 'lost', 'tranquility', 'dregs', 'humanity', 'traces', 'always', 'follow', 'mascara', 'tears', 'getaway', 'walking', 'blisters', 'running', 'shears', 'so', 'unholy', 'sister', 'grace']

'''

''''
Створіть словник зі списками добрих справ на сьогодні і на завтра. Надрукуйте із словника добрі справи, які плануєш зробити сьогодні і взавтра.

Вхідні дані:

Немає
Вихідні дані:

today:
Make a compliment to a friend
Call your grandparents
Embrace parents
tomorrow:
Feed the birds in the park
Give unnecessary things to those who need them
Smile

'''
good_works = {
    'today': ['Make a compliment to a friend', 'Call your grandparents', 'Embrace parents'], 'tomorrow': ['Feed the birds in the park', 'Give unnecessary things to those who need them', 'Smile']}

# ['Make a compliment to a friend', 'Call your grandparents', 'Embrace parents']
print(good_works.get('today'))

# ['Feed the birds in the park', 'Give unnecessary things to those who need them', 'Smile']
print(good_works.get('tomorrow'))
