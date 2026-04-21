import random
print(random.random())
print(random.randint(50,100))

products = ["TV","Donkey Kong Bananza", "20000 Robux", "Too Bad","PS5","Try Again","Horizon Zero Dawn"]
print(random.choice(products))
random.seed(4)
print(random.random())