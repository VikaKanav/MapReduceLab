# This work created by student in group TP-61mp Kanavets Victoria, variant #6
from src.core.job.reducer import Reducer

class VowelConsonantReducer(Reducer):
    def reduce(self, key, values, emit):
        total_vowels = sum(v[0] for v in values)
        total_consonants = sum(v[1] for v in values)
        total_letters = total_vowels + total_consonants
        
        if total_letters > 0:
            vowel_pct = (total_vowels / total_letters) * 100
            consonant_pct = (total_consonants / total_letters) * 100
            emit(f"{key} символів", f"{vowel_pct:.0f}% голосних, {consonant_pct:.0f}% приголосних")
