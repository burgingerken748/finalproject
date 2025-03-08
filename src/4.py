import random
numbers = ["1","2","3","4","5","6","7","8","9"]
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
words = [ "apple", "banana", "orange", "pear", "kiwi", "pineapple", "strawberry", "raspberry", "blueberry", "blackberry", "cranberry", "bilberry", "damson", "cherry", "plum", "peach", "nectarine", "pomegranate", "apricot", "cherimoya", "fig", "quince", "prune", "rabbit", "nut", "kernel"]
words.extend(letters)
words.extend(numbers)
print(random.choice(words))