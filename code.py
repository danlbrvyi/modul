def spam(number):
    return 'bulochka' * (number)


def my_sum(list_of_numbers):
    answer = 0
    for num in list_of_numbers:
        answer += num
    return answer


def shortener(string):
    words = string.split()
    for word in range(len(words)):
        if len(words[word]) > 6:
            words[word] = words[word][:6] + '*'
    return ' '.join(words)



def compare_ends(words):
    count = 0
    for letters in words:
        if len(letters) >= 2:
            if letters[0] == letters[-1]:
                count += 1
    return count

