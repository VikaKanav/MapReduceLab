# This work created by student in group TP-61mp Kanavets Victoria, variant #6
import string
from src.core.job.mapper import Mapper

class VowelConsonantMapper(Mapper):
    def map(self, record, emit):
        translator = str.maketrans('', '', string.punctuation)
        clean_record = str(record).translate(translator)
        vowels_set = set("aeiouyаеєиіїоуюя")
        
        for token in clean_record.split():
            word = token.lower()
            length = len(word)
            if length == 0:
                continue
            
            vowels = sum(1 for char in word if char in vowels_set)
            consonants = sum(1 for char in word if char.isalpha() and char not in vowels_set)
            
            if vowels + consonants > 0:
                emit(length, (vowels, consonants))
