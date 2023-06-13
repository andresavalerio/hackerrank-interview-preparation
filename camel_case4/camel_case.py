def combine(words: str, start_capital = False):
    separated_words = words.split(" ")
    if start_capital:
        capital_words = separated_words
        combined_word = ''
    else:
        capital_words = separated_words[1:]
        combined_word = separated_words[0]

    for word in capital_words:
        combined_word += word.capitalize()

    return combined_word



def camel_case(s: str):
    operation, str_type, words = s.split(";")

    if operation == 'S':
        if str_type == 'M':
            pass
        elif str_type == 'C':
            #class
            pass
        else:
            #variable
            pass
    else:
        # Combine operation
        if str_type == 'M':
            return combine(words)+"()"
        elif str_type == 'C':
            return combine(words, start_capital=True)
        else:
            return combine(words)
