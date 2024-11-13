from random import randint
from statistics import mean
# num_1
list_random: list[int] = [randint(1, 100) for _ in range(50)]
print("bigger than 50:", list(filter(lambda number: number > 50, list_random)))
print("divisible by 7:", list(filter(lambda number: number % 7 == 0, list_random)))
print("two digit numbers:", list(filter(lambda number: 9 <number < 100, list_random)))
print("two digit numbers are same:", list(filter(lambda number: 9 <number < 100 and number % 10 == number // 10, list_random)))
print("sum equal to 9:", list(filter(lambda number: number % 10 + number // 10 == 9, list_random)))
avg = statistics.mean(list_random)
print("bigger than average:", list(filter(lambda number: number > avg, list_random)))
print(list(filter(lambda number: number > max(list_random) / 2, list_random)))
#

# num_2
games: list[str] = ["Fortnite", "V Auto Theft Grand ", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
print("games with length bigger than 8 letters:", list(filter(lambda word: len(word) > 8, games)))
print("Games that start with the letter F:", list(filter(lambda word: word.upper().startswith('F'), games)))
print("A game with two words:", list(filter(lambda word: len(word.split()) == 2, games))
print("A game with the V word:", list(filter(lambda word: 'V' in word.upper(), games)))
#

# num_3
l_random: list[int] = [randint(-50, 50) for _ in range(20)]
print(l_random)
print(" number power 3:", list(map(lambda number: number ** 3, l_random)))
print("The first digit of the number:", list(map(lambda number: number if -1 < number < 10 else number % 10, l_random)))
print("Fahrenheit:", list(map(lambda number: number * 9 / 5 + 32, l_random)))
print("Positive or Negative:", list(map(lambda num: "positive" if num > 0 else "negative", l_random)))
#

#  num_4
fruits: list[str] = ["Strawberry", "Pineapple", "Grapes", "Watermelon", "Mango ", "Orange ", "Banana ", "Apple "]
print("Reverse order of the fruit:", list(map(lambda fruit: fruit[::-1], fruits)))
print("first letter in every fruit:", list(map(lambda fruit: fruit[0], fruits)))
print("Capital letters:", list(map(lambda fruit: fruit.upper(), fruits)))
print("The middle letter in fruit:", list(map(lambda fruit: fruit[len(fruit) // 2], fruits)))
print("A fruit ending in the letter S:", list(map(lambda word: word + '!' if word.lower().endswith('s') else word, fruits)))
#

# num_5
# Saves the variable without being able to change it, is outside of all programs and functions
# Without it the parameter does only reading
# Because in the function it changes the value of "X" and a global value cannot change
#

