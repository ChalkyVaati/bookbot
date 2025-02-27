from stats import get_num_words, get_letters
import sys



def get_book_text(path):
    with open(path) as f:
        return f.read()   

def print_book_report(text, Currentbook):    
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {Currentbook}')
        print('----------- Word Count ----------')
        get_num_words(text)
        print('--------- Character Count -------')
        get_letters(text)
        print('============= END ===============')


def main():
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

        Currentbook = sys.argv[1]
        text = get_book_text(Currentbook)

        print_book_report(text, Currentbook)

main()