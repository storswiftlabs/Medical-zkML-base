import os
import pandas as pd
from decision_tree.data_analysis import Model
from preprocess_data.parser_file import ParserFile
from src.decision_tree.dt_to_leo_code import dt_to_leo_code

FILE_PATH = os.path.abspath(
    # '../medical-zkML/data/Heart_Disease/processed.cleveland.data'
    '../data/Iymphography/lymphography.data'
)

if __name__ == "__main__":
    pf = ParserFile(FILE_PATH)
    lines = pf.read_file()
    for index, line in enumerate(lines):
        # line = Utils.parseInt(line)
        lines[index] = pf.parser_lymphography(line)
    pf.write_to_tsv(lines)

    titanic = pd.read_table(pf.get_save_path(), sep='\t', header=None)
    model = Model(titanic)
    dec_tree = model.get_prediction(len=18)
    leo = dt_to_leo_code(dec_tree, "dt.aleo")
    print(leo)
    print(pf.get_save_leo_path(), 22)

    f = open(pf.get_save_leo_path(), "w")
    f.write(leo)