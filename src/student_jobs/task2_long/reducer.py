# This work created by student in group TP-61mp Kanavets Victoria, variant #6
from src.core.job.reducer import Reducer

class LongWordsReducer(Reducer):
    def reduce(self, key, values, emit):
        emit(key, sum(values))
