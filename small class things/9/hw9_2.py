from helper import remove_punc
import nltk
import math
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

#Clean and lemmatize the contents of a document
#Takes in a file name to read in and clean
#Return a list of words, without stopwords and punctuation, and with all words stemmed
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def readAndCleanDoc(doc) :
    #1. Open document, read text into *single* string
    f = open(doc, 'r')
    text = f.read().replace('\n',' ')
    f.close()
    #2. Tokenize string using nltk.tokenize.word_tokenize
    tokens = nltk.tokenize.word_tokenize(text)
    #3. Filter out punctuation from list of words (use remove_punc)
    tokens = remove_punc(tokens)
    #4. Make the words lower case
    lowercase = []
    for w in tokens:
        lowercase.append(w.lower())
    #5. Filter out stopwords
    stop = stopwords.words('english')
    words = []
    for x in lowercase:
        if x not in stop:
            words.append(x)
    #print("Before: "+ str(len(words)))
    #6. Stem words
    for index in range(len(words)):
        #y = nltk.stem.WordNetLemmatizer().lemmatize(y, 'v')
        #stem_words.append(nltk.stem.PorterStemmer().stem(y))
        words[index] = nltk.stem.PorterStemmer().stem(words[index])
    #print("After: "+ str(len(words)))
    return words
    
#Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames*
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one 
#column per word (there should be as many columns as unique words that appear
#across *all* documents. Also, Before constructing the doc-word matrix, 
#you should sort the wordlist output and construct the doc-word matrix based on the sorted list
#
#Also returns 2) a list of words that should correspond to the columns in docword
def buildDocWordMatrix(doclist) :
    #1. Create word lists for each cleaned doc (use readAndCleanDoc)
    wordlist = []
    clean = []
    for x in doclist:
        clean.append(readAndCleanDoc(x))
    for i in clean:
        for j in i:
            if j not in wordlist:
                wordlist.append(j)
    wordlist.sort()
    #print(wordlist)
    #2. Use these word lists to build the doc word matrix
    docword = np.zeros((len(clean),len(wordlist)))
    row = 0
    for x in clean: #for each doc
        for y in x: #go through the words in the doc
            docword[row][wordlist.index(y)] += 1
        row += 1

    return docword, wordlist
    
#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def buildTFMatrix(docword) :
    tf = []
    for y in docword:
        line = []
        summation = sum(y)
        for x in y:
            line.append(x / summation)
        tf.append(line)

    new_array = np.array(tf)
    tf = new_array
    return tf
    
#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of words in the doc word matrix)
#Don't forget the log factor!
def buildIDFMatrix(docword) :
    N = len(docword)
    totals = []
    col_tot = len(docword[0])
    row_tot = len(docword)
    #print(col_tot)
    #print(row_tot)
    for y in range(col_tot):
        hold = 0
        for x in range(row_tot):
            if docword[x][y] != 0:
                hold += 1
        totals.append(hold)

    idf = []
    for x in totals:
        idf.append(math.log10(N/x))
    #print(idf) #[-2.515211304327802, -2.3191060593097763]

    new_array = np.array([idf])
    idf = new_array
    return idf
    
#Builds a tf-idf matrix given a doc word matrix
def buildTFIDFMatrix(docword) :
    #TF * IDF
    tfidf = []
    tf = buildTFMatrix(docword)
    idf = buildIDFMatrix(docword)
    for x in tf:
        tfidf.append(x*idf[0])

    new_array = np.array(tfidf)
    tfidf = new_array
    return tfidf
    
#Find the three most distinctive words, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most common words in each document
def findDistinctiveWords(docword, wordlist, doclist) :
    distinctiveWords = {}
    #you might find numpy.argsort helpful for solving this problem:
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html
    tfidf = buildTFIDFMatrix(docword)
    index = 0
    for x in tfidf:
        holder = x
        top3_index = (-holder).argsort()[:3]
        #top3 = [holder[0], holder[1], holder[2]]
        #top3_index = [np.where(x == top3[0]), np.where(x == top3[1]), np.where(x == top3[2])]
        #print(top3_index)
        words = [wordlist[top3_index[0]], wordlist[top3_index[1]], wordlist[top3_index[2]]]
        distinctiveWords[doclist[index]] = np.array(words, dtype='<U12') #put top 3 word with the document in the dictionary
        index += 1

    return distinctiveWords


if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext
    
    ### Test Cases ###
    directory='lecs'
    path1 = join(directory, '1_vidText.txt')
    path2 = join(directory, '2_vidText.txt')
    
    # Uncomment and recomment ths part where you see fit for testing purposes
    #'''
    print("*** Testing readAndCleanDoc ***")
    print(readAndCleanDoc(path1)[0:5])
    print("*** Testing buildDocWordMatrix ***") 
    doclist =[path1, path2]
    docword, wordlist = buildDocWordMatrix(doclist)
    print(docword.shape)
    print(len(wordlist))
    print(docword[0][0:10])
    print(wordlist[0:10])
    print(docword[1][0:10])
    print("*** Testing buildTFMatrix ***") 
    tf = buildTFMatrix(docword)
    print(tf[0][0:10])
    print(tf[1][0:10])
    print(tf.sum(axis=1))
    print("*** Testing buildIDFMatrix ***") 
    idf = buildIDFMatrix(docword)
    print(idf[0][0:10])
    print("*** Testing buildTFIDFMatrix ***") 
    tfidf = buildTFIDFMatrix(docword)
    print(tfidf.shape)
    print(tfidf[0][0:10])
    print(tfidf[1][0:10])
    print("*** Testing findDistinctiveWords ***")
    print(findDistinctiveWords(docword, wordlist, doclist))
    #'''
