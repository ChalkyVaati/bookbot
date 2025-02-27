
def get_num_words(booktext):
  
    bookArr = booktext.split()
    get_num = len(bookArr)
    print(f'Found {get_num} total words')


def get_letters(booktext):
    dict = {}

    AllLetters = 'abcdefghijklmnopqrstuvwxyz'
    filteredtext = booktext.lower()
    for Letter in AllLetters:
        LetterCount = filteredtext.count(Letter)
        dict[Letter] = LetterCount
    for key, values in dict.items():
        print(f'{key}: {values}')
   

