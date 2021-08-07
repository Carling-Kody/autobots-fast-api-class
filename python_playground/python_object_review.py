
first_name = 'Kody'
last_name = 'Carling'
age = 39
employed = True
fav_numbers =[1,2,3,4,5]
word = "Python"
user = {
    "first_name": first_name,
    "last_name": last_name,
    "age": age,
    "employed": employed,
    "favorite_food": ["Pizza", "ice cream", "boom"],
    1: "hello"
}

print(f'{first_name} {last_name}')
print(age)
print(fav_numbers[2])
print(fav_numbers[:2])
print(fav_numbers[::2])
print(fav_numbers[:-1])
print(word[1])
print(user["first_name"])
print(user["favorite_food"][2])

# start : stop : step
# [start:stop:step]
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1 

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6  (slice position)
#    0   1   2   3   4   5    (index position)