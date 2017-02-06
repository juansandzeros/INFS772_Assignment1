__author__ = 'Juan Harrington' # change author name

# this method counts how many times each element appears in the list. It outputs a dictionary. Each key-value pair
# show a list element and its number of occurrences
def count_list(li):
    dict = {}
    # your code here - the test cases are available in the main method
    #dict = [[x,li.count(x)] for x in set(li)]
    for item in li:
        if not item in dict:
            dict[item] = 1
        else:
            dict[item] = dict[item] + 1
    return dict

def main():
    #print "------ test cases for the method count_list() -------"
    print count_list([1, 3, 2, 1, 3, 3])
    #output: {1: 2, 2: 1, 3: 3}
    print count_list(['a', 'b', ' ', ' ', 'b', 'b'])
    #output: {'a': 1, ' ': 2, 'b': 3}'''

# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()