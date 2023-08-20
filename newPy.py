
import pandas as pd
import requests

from multiprocessing import Pool

import os
import tqdm


def checkIfWordExist( word ): 

    try: 
        response = requests.get( base_url + word )
        data = response.json() 
        
        if type( data ) == list:
            return True 
        else:
            return False 
    
    except:
        return "failedQuery"

if __name__ == "__main__":

    
    print( checkIfWordExist("hello") )
    
    five_word_lists =  pd.read_csv("all_words.csv")
    five_word_lists.columns=['words']

    
    base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    fiveWordList = five_word_lists['words'].tolist()


    pool = Pool(os.cpu_count())

    results = []
    for result in tqdm.tqdm( pool.imap_unordered(  checkIfWordExist, fiveWordList ), total = len( fiveWordList ) ):
        results.append( result )

    print( results )

