import json;
from difflib import get_close_matches;
data = json.load(open('data.json','r'))
try:
    print('Enter The Word You Want To Search:')
    word = str(input())
    word = word.lower()
    if word in data:
        for i in (data[word]):
            print(i)
    elif len(get_close_matches(word,data.keys())) > 0:
        close = (get_close_matches(word,data.keys())[0])
        print("Do You Mean " + close + "?/  Y/N")
        choice = input().upper()
        if choice == 'Y':
            for i in (data[close]):
                print(i)
        elif choice == 'N':
            print('Oops! We Do Not Have This Information Yet!')
        else:
            print('Invalid Choice')
    else:
        print('Oops! We Do Not Have This Information Yet!')
        
except:
    print('Please Double Check What You Enter!')



