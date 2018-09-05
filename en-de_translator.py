from translate import Translator # translator library
import re # separating sentences in text file
import random # picking random sentences from text file
import os # clearing terminal
import sys # exiting while loop


# german translation
def german(sentence):
    de_translator = Translator(to_lang='de')
    german = de_translator.translate(str(sentence))
    return german


# Also have french as an option!
def french(sentence):
    fr_translator = Translator(to_lang='fr')
    french = fr_translator.translate(str(sentence))
    print('\nFrench: \n', french, sep='')


# getting english sentence from text file
def get_en_sentences():
    with open('en_sentences.txt') as f:
        text = f.read()

    en_sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
    en_sentences = [x.replace('\n', ' ') for x in en_sentences]
    return en_sentences


def main():
    os.system('clear')
    print('Instructions:',
        '=============',
        'Enter your German translation of the English sentence given and compare it to the computer\'s answer!',
        'Hit enter when you want to move on, or \'q\' when you want to quit.\n\n\n', sep='\n')

    en_sentences = get_en_sentences()

    # loop until 'q'
    while True:
        # pick english sentence
        en_sentence = random.choice(en_sentences)

        # show english
        print('English:\n', en_sentence, sep='')

        # make attempt to translate english into german
        my_answer = input('\nAttempt:\n')
        if my_answer == 'q':
            print('\nGoodbye! :)')
            sys.exit()

        # show correct translation
        correct_answer = german(en_sentence)
        print('\nGerman: \n', correct_answer, sep='')

        # wait for enter or 'q' to be hit before continuing
        my_answer = input('\n')
        if my_answer == 'q':
            print('\nGoodbye! :)')
            sys.exit()

        # write english, translation attempt, and correct translation to file
        with open('de_answers.txt', 'a') as f:
            f.write('=======================================================\n'
                + '\nEnglish: '+ en_sentence
                + '\n\nAttempt: '+ my_answer
                + '\n\nGerman: '+ correct_answer + '\n\n')

        os.system('clear')


if __name__ == '__main__':
    main()
