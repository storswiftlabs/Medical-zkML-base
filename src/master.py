import pandas as pd
from decision_tree.data_analysis import Model
from preprocess_data.parser_file import ParserFile

FILE_PATH = [{
    'file': 'data/Heart_Disease/processed.cleveland.data',
    'func': ParserFile.parser_heart_disease,
    'intercept': 13,
    'encoding': 'utf-8'
}, {
    'file': 'data/Acute_Inflammations/diagnosis.data',
    'func': ParserFile.parser_acute_inflammations,
    'intercept': 5,
    'encoding': 'utf-16'
}, {
    'file': 'data/Parkinsons/parkinsons.data',
    'func': ParserFile.parser_parkinsons,
    'intercept': 23,
    'encoding': 'utf-8'
}]
# {'file': 'data/Acute_Inflammations/diagnosis.data', 'func': 3}
if __name__ == "__main__":
    for file in FILE_PATH:
        print("=" * 30 + file['file'].split('/')[-1] + "=" * 30)
        pf = ParserFile(file['file'])
        lines = pf.read_file(file['encoding'])
        for index, line in enumerate(lines):
            lines[index] = file['func'](line)
        pf.write_to_tsv(lines)

        titanic = pd.read_table(pf.get_save_path(), sep='\t', header=None)

        model = Model(titanic)
        model.get_prediction(len=file['intercept'])
        print('\n')
