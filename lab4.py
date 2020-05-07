from utilities import *

def parse_story(file_name): #1
    '''
    Returns an ordered list of all the words contains in file_name, 
    with BAD_CHARS removed, and VALID_PUNCTUATION condsidered as 
    individual tokens. Also removes all whitespaces.

    (string) --> list[string]

    '''
    myFile = open(file_name, 'r')
    content = myFile.read()
    myFile.close() 

    for character in VALID_PUNCTUATION:
        replacement = ' ' + character + ' '
        content = content.replace(character, replacement)
    
    content = content.lower()
    for character in BAD_CHARS:
        replacement = ' '
        content = content.replace(character, replacement)

    words = []
    for word in content.split():
        words.append(word)

    return words
   
def get_prob_from_count(counter): #2
    '''
    Returns the probability of each element in counter, 
    using the total of all the elements in counter.

    (list[int]) -> list[float]

    >>> get_prob_from_count([10, 20, 40, 30])
    [0.1, 0.2, 0.4, 0.3]
    >>> get_prob_from_count([40, 20, 110, 40])
    [0.19047619047619047, 0.09523809523809523, 0.5238095238095238, 0.19047619047619047]
    '''
    
    total = 0
    for n in counter:
        total += n
    for i in range(len(counter)):
        counter[i] = counter[i] / total
    
    return counter

def build_ngram_counts(words, n): #3
    '''
    Returns a dictionary of n-tokens made from input words. 
    The key will be a dictionary of n number of strings, 
    and the value will be two list: a list of strings, 
    and the corresponding counts of each string.

    (list[string], int) --> Dict{tup: List[List[string],List[int]]}
    '''
    ngram = {}
    for i in range(len(words) - n):
        sequence = ()
        for distance in range(n):
            temp = (words[i + distance],)
            sequence = sequence + temp
        ngram[sequence] = [[]]
    
    for i in range(len(words) - n):
        sequence = ()
        for distance in range(n):
            temp = (words[i + distance],)
            sequence = sequence + temp
        nextWord = [words[i + n]]
        ngram[sequence][0].append(nextWord[0])

    for sequence in ngram:
        ngram[sequence].append([])
    
    for sequence in ngram:
        words = ngram[sequence][0]
        #print(words)
        for word in words:
            ngram[sequence][1].append(ngram[sequence][0].count(word))
            while(words.count(word) > 1):
                index = 0
                for index in range(-1, -(len(words)) ,-1):
                    if(words[index] == word):
                        break
                ngram[sequence][0].pop(index)
    
    return ngram
            
def prune_ngram_counts(counts, prune_len): #4
    '''
    Returns the dictionry held in counts with 
    only prune_len values. The values that are kept are
    ones of the highest frequency.
    If the last values are the same, it keeps them all.
    

    (Dict{tup: List[List[string],List[int]]}, int) --> Dict{tup: List[List[string],List[int]]}

    >>> prune_ngram_counts({('i', 'love'): [['js', 'py3', 'c', 'no'], [20, 20, 10, 2]],('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]],('toronto', 'is'): [['six', 'drake'], [2, 3]]}, 3)
    {('i', 'love'): [['js', 'py3', 'c', 'no'], [20, 20, 10]], ('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]], ('toronto', 'is'): [['six', 'drake'], [2, 3]]}
    >>> prune_ngram_counts({('this', 'is'): [['just', 'not', 'ever', 'idk'], [46, 2, 4, 8]],('just', 'a'): [['test', 'drill', 'whatevr', 'whatlol'], [53, 123, 34, 5]],('toronto', 'is'): [['cold', 'ohwell'], [2, 3]]}, 2)
    {('this', 'is'): [['just', 'idk'], [46, 8]], ('just', 'a'): [['test', 'drill'], [53, 123]], ('toronto', 'is'): [['cold', 'ohwell'], [2, 3]]}
    '''
    
    for sequence in counts:
        temp_list = []
        for i in counts[sequence][1]:
            temp_list.append(i)
        
        temp_list.sort()
        temp_list.reverse()

        temp = prune_len
        if(len(temp_list) > prune_len):
            while(len(temp_list) > temp and \
                  temp_list[temp - 1] == temp_list[temp]):
                  temp += 1
        temp_list = temp_list[:temp]
        index = 0
        while(index in range(len(counts[sequence][1]))):
            if (not(counts[sequence][1][index] in temp_list)):
                counts[sequence][1].remove(counts[sequence][1][index])
                counts[sequence][0].remove(counts[sequence][0][index])
                index -= 1
            index += 1
            
    return counts

def probify_ngram_counts(counts): #5
    '''
    Transforms the count the second list in the values counts
    into probabilities.

    (Dict{tup: List[List[string],List[int]]}, int) --> Dict{tup: List[List[string],List[int]]}, int
    '''

    for sequence in counts:
        counts[sequence][1] = get_prob_from_count(counts[sequence][1])
    return counts
                
def build_ngram_model(words, n): #6
    '''
    Builds an n-gram model with token size n, 
    using the words provided.

    (list[string], int) --> Dict{tup: List[List[string],List[int]]}
    '''
    words = build_ngram_counts(words,n)
    words = prune_ngram_counts(words, 15)
    words = probify_ngram_counts(words)
    
    for sequence in words:
        for turn in range(len(words[sequence][1]) ** 2):
            for i in range(len(words[sequence][1]) - 1):
                if(words[sequence][1][i] < words[sequence][1][i + 1]):
                    words[sequence][1][i], words[sequence][1][i + 1] = words[sequence][1][i + 1], words[sequence][1][i]
                    words[sequence][0][i], words[sequence][0][i + 1] = words[sequence][0][i + 1], words[sequence][0][i]

    return words

def gen_bot_list(ngram_model, seed, num_tokens=0): #7 #FIX THIS USING THE PROVIDED FUNCTION!!!! 
    '''
    Returns a randomly generated list of strings 
    of num_tokens length, starting with the provided seed, 
    made using the provided ngram_model

    (Dict{tup: List[List[string],List[int]]}, tup(string), int) --> list[string]
    
    '''

    sentence = list(seed)
    sentence = sentence[:num_tokens]
    if(seed in ngram_model.keys()):
        left = len(ngram_model[seed])
        if len(sentence) >= num_tokens:
            sentence = sentence[:num_tokens]   
        else:
            nex = list(seed)
            left2 = num_tokens - len(seed)
            next_seed = seed
            while(next_seed in ngram_model.keys() and check_open_ngram(next_seed ,ngram_model) and len(sentence) < num_tokens):
                new_word = gen_next_token(next_seed, ngram_model)
                next_seed = (next_seed[1:len(seed)]) + (new_word,)
                sentence.append(new_word)
     
    return sentence

def gen_bot_text(token_list, bad_author): #8
    '''
    For bad_author = True, returns all the strings
    provided in token_list as a string with a space 
    between every element from token_list.
    For bad_author = False, reutrns a string of text
    following the following rules:
        1. No spaces before tokens that are in  VALID_PUNCTUATION
        2. All sentences start with a capital letter.
        3. All words from ALWAYS_CAPATALIZE are capatilized. 
    
    (list[string]) --> string

    '''
    sentence = token_list[0]
    if(bad_author):
        for index in range(1,len(token_list) - 1):
            sentence += ' '
            sentence += token_list[index]
        sentence += ' '
        sentence += token_list[-1]
    
    else:
        for word in range(len(token_list)):
            if (token_list[word].capitalize() in ALWAYS_CAPITALIZE):
                token_list[word] = token_list[word].capitalize()
            else:
                token_list[word] = token_list[word].lower()
        sentence = sentence.capitalize()
        for index in range(1,len(token_list) - 1):
            if(token_list[index] in VALID_PUNCTUATION and not (token_list[index] in END_OF_SENTENCE_PUNCTUATION)):
                sentence += token_list[index]
            elif(token_list[index] in END_OF_SENTENCE_PUNCTUATION):
                sentence += token_list[index].capitalize()
                token_list[index+1] = token_list[index+1].capitalize()
            else:
                if(not('\n' in token_list[index - 1])):
                    sentence += ' '
                    sentence += token_list[index]
                else:
                    sentence += token_list[index]

        if((not (token_list[-1] in END_OF_SENTENCE_PUNCTUATION)) and not ('\n' in token_list[-2])):
            sentence += ' '
        sentence += token_list[-1]
        #print(sentence)
    for word in range(len(sentence)):
        if(sentence[word] == 'Chapter'):
            sentence[word] == "CHAPTER"
    
    return sentence

def write_story(file_name, text, title, student_name, author, year): #9
    '''
    Creates a text file with the name file_name. It starts
    with a title page that follows the format:
        title: year, UNLEASHED
        student_name, inspired by author
        Copyright year published (year), publisher: EngSci press
    It fits a max of 90 characters per line, and creates a new line at
    the last word before the line reaches over 90 characters.
    It fits 30 lines per page, with a page number at the bottom,
    skipping the title page. The page number has new line above it.
    Every 12 pages is a new chapter, writtern as CHAPTER #\n\n.
    Starting with CHAPTER 1.

    (string, string, string, string, string, int) --> None
    '''
    
    myFile = open(file_name, 'w')
    for i in range(10):
        myFile.write('\n')
    myFile.write(title +': ' + str(year) + ', UNLEASHED\n')
    myFile.write(student_name +', inspired by ' + author+'\n')
    myFile.write('Copyright year published ('+ str(year) +'), publisher: EngSci press\n')
    for i in range(17):
        myFile.write('\n')
    myFile.write('CHAPTER 1\n\n')
    character_counter = 0
    line_counter = 4
    page_counter = 0
    index = -1
    while(index < len(text) - 1):
        index += 1
        character_counter += 1
        #print(text[index], end ='')
        if(character_counter == 90):
            if(text[index] in VALID_PUNCTUATION): #If the 90th character is in VALID_PUNC, add newline in the next index
                text = text[:index + 1] + '\n' + text[index + 2:]
                #print('\n')
                index += 1
            elif(text[index + 1] == ' '): #If the next index is a space, add newLine where the space is
                #print(text[index-4:index + 1])
                text = text[:index + 1] + '\n' + text[index + 2:]
                index += 1
                #print('\n')
            else:
                while((not (text[index] in VALID_PUNCTUATION)) and (not(text[index + 1] == ' '))):
                    index -=1
                if(text[index] in VALID_PUNCTUATION):
                    text = text[:index + 1] + '\n' + text[index + 2:]
                    #print('\n')
                    index += 1
                elif(text[index + 1] == ' '):
                    text = text[:index + 1] + '\n' + text[index + 2:]
                    #print('\n')
                    index += 1
            character_counter = 0
            line_counter += 1
            #print(line_counter)
            if(line_counter % 30 == 0):
                #print('Page = ',line_counter / 30)
                #.\n\nfegr
                add = str(line_counter // 30) + '\n'
                text = text[:index + 1]  + '\n' + add + text[index + 1:]
                add = len(add)
                index = index + 1 + add
                line_counter += 2
                character_counter = 0
                if((line_counter // 30 % 12) == 0):
                    add = str(line_counter // 30 // 12 + 1)
                    text = text[:index + 1]  + 'CHAPTER ' + add + '\n\n' + text[index + 1:]
                    add = len(add)
                    line_counter += 2
                    index = index + add + 10

                character_counter = 0
    #print(line_counter)
    for i in range(31 - line_counter % 30 ):
        text = text[:]  + '\n'
    text = text[:]  + str(line_counter // 30 + 1)  

    #text = text.split()
    #for word in text:
    myFile.write(text)
    myFile.close()


if (__name__ == "__main__"):
    x = 5

    #1
    test = parse_story('test_text_parsing.txt') 
    right = ['the', 'code', 'should', 'handle', 'correctly', 'the', 'following', ':', 'white', 'space', '.', 'sequences', 'of', 'punctuation', 'marks', '?', '!', '!', 'periods', 'with', 'or', 'without', 'spaces', ':', 'a', '.', '.', 'a', '.', 'a', "don't", 'worry', 'about', 'numbers', 'like', '1', '.', '5', 'remove', 'capitalization']
    if(test == right):
        print("1. parse_story is right")

    #2
    test = (get_prob_from_count([10, 20, 40, 30])) 
    right = [0.1, 0.2, 0.4, 0.3]
    if(test == right):
        print("2. get_prob_from_count is right")
    
    #3
    test = (build_ngram_counts(['the', 'child', 'will', 'go', 'out', 'to', 'play', ',', 'and', 'the', 'child', 'can', 'not', 'be', 'sad', 'anymore', '.'], 2))
    right = {('the', 'child'): [['will', 'can'], [1, 1]], ('child', 'will'): [['go'], [1]], ('will', 'go'): [['out'], [1]], ('go', 'out'): [['to'], [1]], ('out', 'to'): [['play'], [1]], ('to', 'play'): [[','], [1]], ('play', ','): [['and'], [1]], (',', 'and'): [['the'], [1]], ('and', 'the'): [['child'], [1]], ('child', 'can'): [['not'], [1]], ('can', 'not'): [['be'], [1]], ('not', 'be'): [['sad'], [1]], ('be', 'sad'): [['anymore'], [1]], ('sad', 'anymore'): [['.'], [1]]}
    if(test == right):
        print("3. build_ngram_counts is right")

    #4
    test = prune_ngram_counts({('i', 'love'): [['js', 'py3', 'c', 'no'], [20, 20, 10, 2]],('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]],('toronto', 'is'): [['six', 'drake'], [2, 3]]}, 3)
    right = {('i', 'love'): [['js', 'py3', 'c'], [20, 20, 10]],('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]],('toronto', 'is'): [['six', 'drake'],[2, 3]]}
    if(test == right):
        print("4. prune_ngram_counts is right")

    #5
    test = probify_ngram_counts({('i', 'love'): [['js', 'py3', 'c'], [20, 20, 10]],('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]],('toronto', 'is'): [['six', 'drake'], [2, 3]]})
    right = {('i', 'love'): [['js', 'py3', 'c'], [0.4, 0.4, 0.2]], ('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [0.32, 0.28, 0.2, 0.2]], ('toronto', 'is'): [['six', 'drake'], [0.4, 0.6]]}
    if(test == right):
        print("5. probify_ngram_counts is right")
    
    #6
    test = (build_ngram_model(['the', 'child', 'will', 'the', 'child', 'can', 'the', 'child', 'will', 'the', 'child', 'may','go', 'home', '.'], 2))
    right = {('the', 'child'): [['will', 'can', 'may'], [0.5, 0.25, 0.25]], ('child', 'will'): [['the'], [1.0]], ('will', 'the'): [['child'], [1.0]], ('child', 'can'): [['the'], [1.0]], ('can', 'the'): [['child'], [1.0]], ('child', 'may'): [['go'], [1.0]], ('may', 'go'): [['home'], [1.0]], ('go', 'home'): [['.'], [1.0]]}
    if(test == right):
        print("6. build_ngram_model is right")
        
    #7
    test = gen_bot_list({('the', 'child'): [['will', 'can','may'], [0.5, 0.25, 0.25]],('child', 'will'): [['the'], [1.0]], ('will', 'the'): [['child'], [1.0]],('child', 'can'): [['the'], [1.0]],('can', 'the'): [['child'], [1.0]],('child', 'may'): [['go'], [1.0]],('may', 'go'): [['home'], [1.0]],('go', 'home'): [['.'], [1.0]]}, ('the', 'child'),2)
    right = ['the', 'child']
    if(test == right):
        print("7. gen_bot_list is right")

    #8
    test = gen_bot_text(['this', 'is', 'a', 'string', 'of', 'text', '.', 'which', 'needs', 'to', 'be', 'created', '.'], False)
    right = 'This is a string of text. Which needs to be created.'
    if(test == right):
        print("8. gen_bot_text is right")
    
    


#Test:
#random.seed(1)
#ngram_model = {('the', 'child'): [['will', 'can','may'], [0.5, 0.25, 0.25]],('child', 'will'): [['the'], [1.0]], ('will', 'the'): [['child'], [1.0]],('child', 'can'): [['the'], [1.0]],('can', 'the'): [['child'], [1.0]],('child', 'may'): [['go'], [1.0]],('may', 'go'): [['home'], [1.0]],('go', 'home'): [['.'], [1.0]]}

#print(gen_bot_list({('the', 'child'): [['will', 'can','may'], [0.5, 0.25, 0.25]],('child', 'will'): [['the'], [1.0]], ('will', 'the'): [['child'], [1.0]],('child', 'can'): [['the'], [1.0]],('can', 'the'): [['child'], [1.0]],('child', 'may'): [['go'], [1.0]],('may', 'go'): [['home'], [1.0]],('go', 'home'): [['.'], [1.0]]}, ('the', 'child'),5))

#print(prune_ngram_counts({('this', 'is'): [['just', 'not', 'ever', 'idk'], [46, 2, 4, 8]],('just', 'a'): [['test', 'drill', 'whatevr', 'whatlol'], [53, 123, 34, 5]],('toronto', 'is'): [['cold', 'ohwell'], [2, 3]]}, 2))




