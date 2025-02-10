class TextCleaner:
    def __init__(self, symbols):
        self.word_index_dictionary = {sym: i for i, sym in enumerate(symbols)}
    def __call__(self, text):
        indexes = []
        for char in text:
            try:
                indexes.append(self.word_index_dictionary[char])
            except KeyError:
                indexes.append(self.word_index_dictionary['U']) # unknown token
#                 print(char)
        return indexes