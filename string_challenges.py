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
# ???


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???