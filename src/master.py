import os
import pandas as pd
from decision_tree.data_analysis import Model
from preprocess_data.parser_file import ParserFile

FILE_PATH = os.path.abspath(
    '../medical-zkML/data/Heart_Disease/processed.cleveland.data')

if __name__ == "__main__":
    pf = ParserFile(FILE_PATH)
    lines = pf.read_file()
    for index, line in enumerate(lines):
        # line = Utils.parseInt(line)
        lines[index] = pf.parser_heart_disease(line)
    pf.write_to_tsv(lines)

    titanic = pd.read_table(pf.get_save_path(), sep='\t', header=None)
    model = Model(titanic)
    model.get_prediction(len=13)
