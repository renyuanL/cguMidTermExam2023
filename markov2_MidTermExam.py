# 期中考題目
# 2023-03-31
# 本檔案為 Python 程式碼檔案。
# 連同所需之文字檔 
# "emma_zh.csv", "emma.txt", "_jy_神雕俠侶.txt", 
# 可於此處下載：
# HTTP://

import sys
import random

class Markov:
    '''
    '''
    def __init__(self, 
                 filename,  
                 lang,
                 order= 2):
        '''
        '''
        
        self.suffix_map= {}
        self.prefix=     ()
        
        self.filename= filename
        self.lang=     lang
        self.order=    order

        self.text= ''
        
    def process_file(self):
        '''
        '''
        with open(self.filename, encoding='utf-8') as fp:
            for line in fp:
                wordL= (line.rstrip().split() 
                        if self.lang=='en' else 
                        list(line))
                for word in wordL:
                    self.process_word(word)

    def process_word(self, word):
        '''
        '''

        if len(self.prefix) < self.order:
            self.prefix += (word,)
            return

        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            
            self.suffix_map[self.prefix] = [word]

        self.prefix= self.shift(self.prefix, word)        

    def shift(self, t, word):
        '''
        '''
        return t[1:] + (word,)

    def random_text(self, n=10):
        '''
        '''

        start= random.choice(list(self.suffix_map.keys()))

        for i in range(n):
            suffixes = self.suffix_map.get(start, None)
            if suffixes == None:
                self.random_text(n-i)
                return 
            
            word= random.choice(suffixes)

            #print(word, end=' ')

            self.text += word +' '

            start= self.shift(start, word)


def main(script= None, 
         filename=  'emma.txt', 
         lang=      'en'):
    '''
    '''
    
    order= random.randint(2, 5)
    n=     random.randint(10, 30)

    markov= Markov(
        filename= filename,
        order= order, 
        lang= lang
        ) 
    markov.process_file()
    markov.random_text(n)

    theText= markov.text

    print(f'{order= }, {n= }, {len(theText)= }, {theText= }')

if __name__ == '__main__':
    main(*sys.argv)

# Path: markov2_MidTermExam.py

# 1. 請執行本程式碼，並抄出其執行結果。

# 2. 請說明本程式碼之目的或其所解決的問題。

# 3. 請為本程式加上中文註解。

# 4. 請嘗試修改本程式碼，使其能夠處理英文文本檔案。
#    例如："emma.txt"，請抄出其執行結果。

# 5. 請嘗試修改本程式碼，使其能夠處理中文文本檔案。
#    例如："emma_zh.csv" 或 "_jy_神雕俠侶.txt"，
# 請抄出其執行結果。

# 6. 請嘗試任何方式修改本程式碼，
#    改善本程式，並說明你所改善的地方。

# 7. 將你的結果，程式碼部分上傳至 E-learning 系統。
#    同時將任何可抄寫至紙本之部分繳交給助教或老師。
