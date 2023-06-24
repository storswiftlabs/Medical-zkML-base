import os
import pandas as pd
from decision_tree.data_analysis import Model
import decision_tree.dt_to_leo_code as leo
from decision_tree.dt_to_leo_code import quantize_leo
from preprocess_data.parser_file import ParserFile

FILE_PATH = [
    {
        'file': 'data/Heart_Disease/processed.cleveland.data',
        'func': ParserFile.parser_heart_disease,
        'intercept': 13,
        'encoding': 'utf-8'
    },
    {
        'file': 'data/Acute_Inflammations/diagnosis.data',
        'func': ParserFile.parser_acute_inflammations,
        'intercept': 5,
        'encoding': 'utf-16'
    },
    {
        'file': 'data/Parkinsons/parkinsons.data',
        'func': ParserFile.parser_parkinsons,
        'intercept': 22,
        'encoding': 'utf-8'
    },
    {
        'file':
        'data/Heart_Failure_Clinical_Records/heart_failure_clinical_records_dataset.csv',  # noqa: E501
        'func': ParserFile.parser_heart_failure_clinical,
        'intercept': 12,
        'encoding': 'utf-8'
    },
    {
        'file': 'data/Chronic_Kidney_Disease/chronic_kidney_disease.arff',
        'func': ParserFile.parser_chronic_kidney_disease,
        'intercept': 24,
        'encoding': 'utf-8'
    },
    {
        'file': 'data/Iymphography/lymphography.data',
        'func': ParserFile.parser_lymphography,
        'intercept': 18,
        'encoding': 'utf-8'
    },
    {
        'file': 'data/Liver_Disorders/bupa.data',
        'func': ParserFile.parser_bupa,
        'intercept': 6,
        'encoding': 'utf-8'
    },
    {
        'file': 'data/Breast_Cancer/breast-cancer.data',
        'func': ParserFile.parser_breast_cancer,
        'intercept': 9,
        'encoding': 'utf-8'
    },
    {
        'file': 'data/Primary_Tumor/primary-tumor.data',
        'func': ParserFile.parser_primary_tumor,
        'intercept': 17,
        'encoding': 'utf-8'
    }
]

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
        exponent, is_negative = quantize_leo(titanic.iloc[0])
        model = Model(titanic)
        dec_tree = model.get_prediction(_len=file['intercept'])
        leo_code = leo.dt_to_leo_code(dec_tree, 'dt.aleo', exponent, is_negative)
        leo_path = os.path.dirname(file['file']) + r'/' + \
            os.path.dirname(file['file']).split('/')[-1] + '.leo'
        with open(leo_path, mode='w+', encoding='utf8') as f:
            f.writelines(leo_code)
        print()
