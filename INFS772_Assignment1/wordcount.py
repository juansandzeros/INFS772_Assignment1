__author__ = 'Juan Harrington' # please type your name
import nltk
import util
import os
import sys

# you need to first implement the tokenize method. What this function does is that it takes a string s as its input
# and outputs a list of tokens - in this assignment, we assume that each token is a word (you don't need to further process the tokens).
# To implement this function, you need to use the NLTK package, which is the python package for natural language
# processing. You need to first download NLTK from https://pypi.python.org/pypi/nltk and then install it.
# Please google to find out how to use the NLTK package to do tokenization.
# when you run nltk for the first time, you will probably see some error message.
# To fix the problem, you need use python console to run the following two lines of code first
# import nltk
# nltk.download('punkt')
def tokenize(s):
    tokens = [] # initialize the output list
    # your code here.
    tokens = nltk.word_tokenize(s)
    return tokens # return a list of tokens

# after tokenization, you need to lowercase all tokens/words. This method has no return value. Since the input tokens is
#  a list, which is mutable,  you direct change the input list "tokens".
def lower_case(tokens):
    # you code here
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

# after tokenization and lower_case(), you can now do wordcount for a file. This function takes filename with path as
# its argument. There is a test case in the main method
def wordcount_file(fname_with_path):
    s = ""
    # your code for read the content of files - in our class we talked about how to read file line by line. Here you can
    # just call f.read() to read file content as a string.
    f = open(fname_with_path,"r")
    s = f.read()
    words = tokenize(s) # call the tokenize method you just implemented
    lower_case(words) # call the lower_case method you just implemented
    dc =  util.count_list(words) # here you need to call the count_list function you implemented in util.py for task 4
    return dc

# now you are ready to count the words in a directory. There is a test case in the main method.
def wordcount_directory(directory):
    dict = {} # initialize the output dictionary
    # your code here
    # 1. you need to first look at how to find all files in a directory: hint: look at the OS module slide
    # 2. read files in the directory one by one
    # 3. After you read a file, call the "wordcount_file" method to do wordcount for the file. You are going to get
    #    a dictionary for each file
    # 4. you need to combine the wordcount results for all files in the directory.
    #    the idea is that after reading the first file, you will get a dictionary that shows wordcounts for the file,
    #    You need to add results stored in the dictionary to "dict", the output dictionary. Then you read the second file, and you again get a dictionary.
    #    You need to add the results stored in the dictionary again to "dict", and so on.
    #    How to add the contents in a dictionary to another dictionary? you need to take out a key-value pair from the former and check to see if
    #    the latter already has the key, if yes, you need to modify the value associated with the key,
    #    if no, you just add the key-value pair to the latter.
    #
    for filename in os.listdir(directory):
        words = wordcount_file(os.path.join(directory,filename))
        for k,v in words.iteritems():
            if k in dict:
                dict[k] = dict[k] + v
            else:
                dict[k] = v
    return dict

def main():
    """print "------------test case for wordcount_file()----------------"
    print wordcount_file("C:/Users/jharrington/Documents/_DSU-MSA/INFS772/Assignment1/wordcount_data/news1.txt") # you need to change the file path
    # output:{'managed': 1, 'being': 1, '4.9': 1, 'results': 1, 'jpmorgan': 3, 'thomson': 1, 'shares': 1, 'its': 1, 'bank\x92s': 2, '21': 1, ',': 13, '1.19': 1, 'to': 3, 'reuters': 1, '4': 1, 'quarterly': 1, '2014': 1, '2013': 1, 'was': 2, 'big': 2, 'anticipated': 1, '23.55': 1, 'during': 1, 'bank': 2, 'sluggish': 1, 'drop': 1, 'wednesday': 1, 'settle': 1, '22.5': 1, 'quarter': 2, 'unexpected': 1, 'financial': 1, 'trading': 1, 'are': 1, 'year': 1, 'said': 1, 'for': 2, 'profit': 4, 'legal': 2, 'increase': 1, '3': 1, 'investigation': 1, '7': 1, 'new': 1, 'net': 1, 'ever': 1, 'million': 1, 'reported': 2, 'by': 6, '$': 11, 'on': 3, '900': 1, 'of': 5, 'annual': 1, 'foreign': 1, '23.6': 1, 'analysts': 2, 'slightly': 1, 'or': 3, 'revenue': 2, 'into': 1, 'period': 1, 'down': 1, 'crisis': 1, 'from': 2, 'basis': 2, '21.8': 1, '.': 9, 'expected': 1, 'pretax': 1, 'surveyed': 1, 'a': 9, 'company': 2, 'hurt': 1, 'wake': 1, 'manipulation': 1, 'highest': 1, 'these': 1, 'markets': 1, 'below': 1, 'were': 1, 'midmorning': 1, 'at': 1, 'and': 1, '1.1': 1, 'share': 3, 'an': 2, 'currency': 1, 'as': 2, 'dropped': 1, 'in': 5, 'chase': 1, '5.6': 1, 'percent': 4, 'absorbed': 1, 'earnings': 1, 'fourth': 2, '1.30': 1, '1.31': 1, 'earlier': 1, 'prepared': 1, 'most': 1, 'fell': 2, 'recent': 1, 'billion': 7, 'so-called': 1, 'short': 1, 'whole': 1, 'costs': 1, 'expenses': 1, 'banks': 1, 'the': 17, 'latest': 1}
    # if in your output, the words are ordered differently, you don't need to word. You can just look at some examples,
    you can look up many times 'jpmorgan' appears, or how many time ',' appears.
    """

    """print "------------test case for wordcount_directory()----------------"
    directory = 'C:/Users/jharrington/Documents/_DSU-MSA/INFS772/Assignment1/wordcount_data/' # you need to change this
    print wordcount_directory(directory)
    # output {'all': 2, 'managed': 1, 'skip': 1, '0.12': 1, 'results': 3, 'supplement': 1, 'go': 2, 'adjustment': 1, '1.19': 3, 'to': 26, 'under': 2, 'quarterly': 1, 'presentation': 5, 'risk': 1, 'far': 1, 'continues': 1, 'nor': 1, '--': 1, 'wednesday': 2, 'large': 1, 'solid': 1, 'settle': 1, 'added': 1, 'disclaimer': 1, 'cfo': 1, 'unexpected': 1, 'core': 2, 'street': 1, 'manipulating': 1, 'contributed': 1, 'shares': 1, 'consistently': 1, 'capital': 3, 'new': 1, 'firms': 1, 'boost': 1, 'notable': 1, 'here': 3, 'reported': 5, 'november': 1, 'strong': 1, 'change': 2, '900': 1, 'items': 2, 'changed': 1, 'prior': 1, 'amount': 1, 'analysts': 3, 'runoff': 1, 'settled': 1, 'golden': 1, 'marianne': 1, 'foreign-exchange': 1, 'total': 2, 'crisis': 1, 'cost': 2, 'from': 7, 'remains': 1, 'positive': 2, 'call': 2, '6': 1, 'markets': 2, 'historically': 1, 'more': 2, 'flat': 2, '``': 2, 'standardized': 1, 'tax': 1, 'company': 4, 'hurt': 1, '98': 1, 'me': 1, 'this': 4, 'can': 2, 'dropped': 1, 'control': 1, 'share': 5, 'currency': 1, 'incremental': 2, 'numbers': 1, 'requirements': 1, '5.5': 1, '5.6': 2, '5.9': 1, '1': 2, 'how': 2, 'methodology': 1, 'earnings': 4, 'fourth': 5, 'chase': 4, 'stock': 1, 'fx': 1, 'earlier': 1, 'reflect': 1, 'a': 21, 'short': 1, 'lines': 1, 'so': 2, 'banks': 1, 'order': 1, 'finalized': 1, 'over': 1, 'move': 1, 'thomson': 1, 'through': 2, 'still': 1, 'its': 2, 'before': 1, '24': 1, 'bank\x92s': 2, '10.5': 1, '21': 1, '22': 1, ',': 52, 'better': 1, 'reuters': 1, '2015': 1, '2014': 1, '2013': 2, 'good': 1, 'return': 3, 'ceo': 1, 'anticipated': 1, 'they': 1, 'front': 1, 'now': 1, 'bank': 7, 'fully': 2, 'drop': 1, 'slide': 1, '22.5': 1, 'quarter': 9, 'everyone': 1, 'financial': 1, 'nii': 1, 'trading': 1, 'expect': 1, 'year': 6, 'our': 6, 'buffers': 1, 'out': 1, 'profit': 5, 'risk-weighted': 1, 'increase': 2, 'investigation': 1, '7': 2, 'got': 1, 'sluggish': 1, 'tangible': 3, 'after': 1, 'turning': 1, 'cet1': 1, 'million': 2, 'regulators': 2, 'estimate': 1, 'expecting': 1, 'revenue': 9, 'given': 2, 'similarly': 1, 'approximately': 3, 'contra': 2, 'returns': 1, '2': 2, '650': 1, 'final': 1, 'gives': 1, 'that': 5, 'jamie': 1, 'part': 1, 'manipulation': 1, '11': 1, '10': 1, '13': 1, '15': 1, '14': 1, 'was': 11, 'i': 3, 'future': 1, 'were': 5, 'midmorning': 1, 'and': 24, 'cleaner': 1, '1.1': 3, 'investors': 1, 'remained': 1, 'eps': 5, 'have': 1, 'predominantly': 1, 'also': 2, 'concerns': 1, 'absorbed': 1, 'financials': 1, 'which': 5, '1.30': 1, '1.31': 2, '1.33': 1, 'sure': 1, 'most': 1, 'assault': 1, 'net': 9, 'so-called': 1, 'reflecting': 1, 'responded': 1, 'saying': 1, 'particularly': 1, 'show': 2, 'jpmorgan': 6, 'businesses': 3, 'portfolio': 1, 'impact': 5, 'giant': 1, 'ratio': 4, '(': 1, 'guidance': 1, 'year-on-year': 1, 'going': 3, 'surveyed': 1, 'equity': 4, '8': 1, 'firm-wide': 1, 'his': 1, 'preferred': 5, 'nearly': 2, 'reporters': 1, 'during': 3, ';': 1, 'lobs': 1, 'regarding': 1, 'ever': 1, 'morning': 1, 'banking': 1, 'common': 3, 'including': 1, 'reference': 1, 'see': 2, 'accused': 1, 'are': 3, 'best': 1, 'points': 2, 'said': 2, 'federal': 1, 'please': 1, '3': 2, 'various': 1, 'phased': 2, 'available': 1, '10.1': 1, 'we': 9, 'terms': 1, 'dividends': 4, 'agencies': 1, 'however': 1, 'come': 1, 'thank': 1, 'improved': 1, 'annual': 1, 'foreign': 1, 'expense': 5, 'whole': 1, 'asked': 1, 'adjusted': 1, 'wall': 1, 'loan': 1, 'period': 1, 'resentment': 1, 'allocated': 1, 'throughout': 2, 'along': 1, 'conference': 1, 'basis': 3, 'due': 1, 'been': 1, '.': 50, 'rivals': 1, 'much': 1, 'interest': 1, 'expected': 1, 'proposal': 1, 'improve': 1, 'hardly': 1, 'firm': 5, 'corresponding': 1, 'scrutiny': 1, 'wake': 1, 'child': 1, 'last': 1, 'despite': 1, 'those': 2, '58.4': 1, 'these': 3, 'straight': 1, 'full-year': 1, 'slr': 2, 'will': 3, 'while': 1, 'tlac': 1, 'at': 6, 'is': 4, 'site': 1, 'expenses': 2, 'weighed': 1, 'in': 26, 'around': 1, 'credit': 1, ')': 1, 'make': 1, '4.9': 3, 'elevated': 1, 'struggling': 1, 'higher': 1, 'used': 1, 'counterparty': 1, 'reporting': 1, 'forecasts': 1, 'driven': 1, 'moving': 1, 'issuance': 1, 'recent': 3, 'largely': 1, 'charges': 1, 'well': 3, 'increases': 1, 'dimon': 2, 'costs': 2, 'the': 69, 'corporate': 1, 'latest': 1, 'less': 1, 'being': 1, 'when': 1, 'not': 1, 'profitable': 1, 'web': 1, '$': 31, 'forward-looking': 1, 'lake': 1, 'add': 1, '4': 2, 'has': 3, 'take': 1, 'increased': 2, 'government': 1, 'rules': 1, 'big': 2, 'couple': 1, '23.55': 1, 'performance': 1, 'world': 1, 'disappointed': 1, 'advanced': 1, 'excluding': 2, '50': 1, "'ve": 5, 'continue': 1, 'translated': 1, 'page': 9, 'some': 2, 'back': 1, 'trends': 1, 'growth': 1, 'comparability': 1, 'for': 12, 'bottom': 1, 'affects': 1, 'legal': 7, 'refer': 1, 'be': 5, 'business': 1, 'each': 2, 'continuing': 1, 'ratios': 1, 'offset': 1, 'peer': 1, 'by': 13, 'on': 21, 'about': 2, 'of': 34, 'industry': 1, '23.6': 2, 'important': 1, 'slightly': 1, 'or': 6, 'outlook': 1, 'statements': 1, 'into': 2, 'down': 4, 'operator': 1, 'refined': 1, 'your': 1, '5.29': 1, 'lob': 2, 'there': 1, '21.8': 1, 'kidding': 1, 'overhead': 1, ':': 1, 'pretax': 1, 'billion': 20, 'adjusting': 1, 'but': 1, 'line': 3, 'highest': 1, 'with': 5, 'he': 1, 'cib': 1, 'record': 3, 'below': 4, "'re": 2, 'an': 5, "''": 2, 'as': 10, 'periods': 1, 'distributions': 2, '%': 11, 'no': 1, 'percent': 4, 'other': 1, '5': 1, 'details': 1, 'income': 5, 'you': 5, "'s": 4, 'prepared': 1, 'regulations': 1, 'fell': 3, 'additionally': 1, 'included': 2, "'m": 2, 'ago': 1, 'fsb': 1, 'assets': 1, 'calls': 1, 'invest': 1, 'presenting': 1, 'starting': 1, 'profits': 2}
    """
    directory = 'C:/Users/jharrington/Documents/_DSU-MSA/INFS772/Assignment1/wordcount_data/' # you need to change this
    print wordcount_directory(directory)

if __name__ == '__main__':
    main()