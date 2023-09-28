numbers = input ("Ведите оценки студента разделяя пробелом").split()
a_fives = numbers.count("5")
print(a_fives/len(numbers)*100)
