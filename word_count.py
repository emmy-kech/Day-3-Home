def words(words_str):
  
    word_list = words_str.split() 
    set_wordlist = list(set(word_list)) 
    wordcount_dict = {} 
    for word in set_wordlist:
        if word.isdigit()==True: 
            wordcount_dict[int(word)] = word_list.count(word)
        elif word in word_list: 
            wordcount_dict[word] = word_list.count(word)
    return wordcount_dict 