#Question 1
def sliding_window_maximum(num_list, k):
    if not num_list or k <= 0:
        return []

    result = []
    deque = []

    for i in range(len(num_list)):

        if deque and deque[0] < i - k + 1:
            deque.pop(0)

        while deque and num_list[deque[-1]] < num_list[i]:
            deque.pop()

        deque.append(i)

        if i >= k - 1:
            result.append(num_list[deque[0]])

    return result

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(sliding_window_maximum(num_list, k))

#Question 2
def count_chars(string):

    char_count = {}

    for char in string:

        if char in char_count:
            char_count[char] += 1

        else:
            char_count[char] = 1

    return char_count


string1 = 'Happiness'
print(count_chars(string1))

string2 = 'smiles'
print(count_chars(string2))
