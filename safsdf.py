import pandas as pd

five_word_lists = pd.read_csv("all_words.csv")

five_word_lists.columns=['words']

five_word_lists['words'] =  five_word_lists.words.str.lower()



def word_frequencies(filename="src/alice.txt"):
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.lower()
            line = line.split()
            stripped = [x.strip('''!"#$%&'()*,-./:;?@[]_''') for x in line]
          

            for word in stripped:
                try:
                    d[word] += 1
                except KeyError:
                    d[word] = 1
               
    return d




## checkgutenberg words to get word popularity 

    # 挑选一个文本： 简-奥斯丁的《爱玛》
    emma = gutenberg.words("austen-emma.txt")

    # 查看书的长度
    print len(emma)

    # 导入文本
    emma_text = nltk.Text(emma)
    emma_text.concordance("surprize")