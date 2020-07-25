
def Vowels(word):
    vowels_list = ['a','e','i','o','u']
    count = 0

    word = word.lower()
    word_list = list(word)
    
    for i in vowels_list:
            count += word_list.count(i)  # count = count + 1
    return count


print("Enter a word :")
word = str(input())

print ('There are {} vowles in the \"{}\"'.format(str(Vowels(word)),word))
