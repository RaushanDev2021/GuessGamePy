with open('/Users/raushanruslankyzy/Downloads/DRUGTEST30_20250325-1610.txt', 'r') as file:
    words = file.read()
#if you want to use the code above make sure to put correct directory and file name

words = words.split()
word_count = len(words)
print("Number of words:", word_count)