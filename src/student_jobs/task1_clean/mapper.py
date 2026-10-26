# This work created by student in group TP-61mp Kanavets Victoria, variant #6
import string
from src.core.job.mapper import Mapper

class CleanWordCountMapper(Mapper):
    def map(self, record, emit):
        translator = str.maketrans('', '', string.punctuation)
        clean_record = str(record).translate(translator)
        for token in clean_record.split():
            emit(token.lower(), 1)