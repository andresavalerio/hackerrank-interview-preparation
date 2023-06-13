def combine(initial_word: str, iterable_words: list):
    for word in iterable_words:
        initial_word += word.capitalize()

    return initial_word


def camel_case(s: str):
    operation, str_type, words = s.split(";")

    if operation == 'S':
        # Split operation
        if str_type == 'M':
            #method
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
            separated_words = words.split(" ")
            capital_words = separated_words[1:]
            initial_word = separated_words[0]

            return combine(initial_word, capital_words)+"()"

        elif str_type == 'C':
            separated_words = words.split(" ")

            combined_word = combine("", separated_words)

            return combined_word
        else:
            separated_words = words.split(" ")
            capital_words = separated_words[1:]
            initial_word = separated_words[0]

            return combine(initial_word, capital_words)
