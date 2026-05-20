def count_words(sentence):
    words = sentence.split()
    return len(words)

def main():
    try:
        sentence = input("Enter a sentence: ")
        word_count = count_words(sentence)
        print("Total number of words in the sentence: {}".format(word_count))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()