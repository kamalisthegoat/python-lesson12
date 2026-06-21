n = int(input("eenter a number: "))

odd = [i for i in range(n) if i % 2 != 0]
even = [i for i in range(n) if i % 2 == 0]

print("odd numbers area:", odd)
print("even numbers are:", even)

fruity = ["apple", "banana", "mango", "orange", "grapes"]
fruitybrother = [fruit.capitalize() for fruit in fruity]

print("capitalized of the fruits is:", fruitybrother)