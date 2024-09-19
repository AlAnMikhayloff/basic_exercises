# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1:])
# ???


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))
# ???


# Вывести количество гласных букв в слове
word = 'Архангельск'

count = 0

for sign in word:
    if sign in "аеёиоуыэюяАЕЁИОУЫЭЮЯ":
        count += 1
        
print("Количество гласных букв:", count)
# ???


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))
# ???


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
i = 0
for word in sentence.split(' '):
    i+=1
    print(sentence.split(' ')[i-1][0])
  
# ???


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'

i = 0
sum_letter = 0

for word in sentence.split(' '):
    i+=1
    sum_letter = sum_letter + len(sentence.split(' ')[i-1])

print(sum_letter/len(sentence.split(' ')))    
# ???