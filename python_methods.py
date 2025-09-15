text = "   welcome to PYTHON programming 101!   "

text.strip();print(text)

text.capitalize();print(text)

text.upper();print(text)

text.lower();print(text)

text.title();print(text)

text.swapcase();print(text)

text.center(50, '-');print(text)

text.count('o');print(text)

text.replace("PYTHON", "Java");print(text)

text.split();print(text)

text.join("|");print(text)


print(text.startswith("welcome"))

print(text.endswith("101!"))

print(text.isalnum())

print(text.isalpha())

print(text.isdigit())

print(text.isspace())

print(text.islower())

print(text.isupper())

print("cat" == "cat")

print("cat" != "Cat")

print("cat" < "caterpillar")

print("dog" > "Dog")

print("10" == 10)
print("10" != 10)
print("10" > 10)

list = ["dog", "cat", "zebra", "ant"]

list.sort();print(list)

print(sorted(list))

print(type(str(1)))

print(type(int("1")))

print(type(float("1.0")))

try:
    print(type(int("hello")))   
except:
    print("Error: Cannot convert 'hello' to an integer.")