from src.preprocess_data.parser_file import ParserFile

FILE_PATH = [
    {
        'file': 'data/Heart_Disease/processed.cleveland.data',
        'func': ParserFile.parser_heart_disease,
        'intercept': 13,
        'encoding': 'utf-8',
        'purpose': 'classification'
    },
    {
        'file': 'data/Acute_Inflammations/diagnosis.data',
        'func': ParserFile.parser_acute_inflammations,
        'intercept': 5,
        'encoding': 'utf-16',
        'purpose': 'classification'
    },
    {
        'file': 'data/Parkinsons/parkinsons.data',
        'func': ParserFile.parser_parkinsons,
        'intercept': 22,
        'encoding': 'utf-8',
        'purpose': 'classification'
    },
    {
        'file':
            'data/Heart_Failure_Clinical_Records/heart_failure_clinical_records_dataset.csv',  # noqa: E501
        'func': ParserFile.parser_heart_failure_clinical,
        'intercept': 12,
        'encoding': 'utf-8',
        'purpose': 'classification'
    },
    {
        'file': 'data/Chronic_Kidney_Disease/chronic_kidney_disease.arff',
        'func': ParserFile.parser_chronic_kidney_disease,
        'intercept': 24,
        'encoding': 'utf-8',
        'purpose': 'classification'
    },
    {
        'file': 'data/Iymphography/lymphography.data',
        'func': ParserFile.parser_lymphography,
        'intercept': 18,
        'encoding': 'utf-8',
        'purpose': 'classification'
    },
    {
        'file': 'data/Liver_Disorders/bupa.data',
        'func': ParserFile.parser_bupa,
        'intercept': 6,
        'encoding': 'utf-8',
        'purpose': 'classification'
    },
    {
        'file': 'data/Breast_Cancer/breast-cancer.data',
        'func': ParserFile.parser_breast_cancer,
        'intercept': 9,
        'encoding': 'utf-8',
        'purpose': 'classification'
    },
    {
        'file': 'data/Primary_Tumor/primary-tumor.data',
        'func': ParserFile.parser_primary_tumor,
        'intercept': 17,
        'encoding': 'utf-8',
        'purpose': 'classification'
    }
]

if __name__ == "__main__":
    """
    Data preprocess
    """
    MODEL_NAME = 'dt'
    for file in FILE_PATH:
        print("=" * 30 + file['file'].split('/')[-1] + "=" * 30)
        pf = ParserFile(file['file'])
        lines = pf.read_file(file['encoding'])
        for index, line in enumerate(lines):
            lines[index] = file['func'](line)
        pf.write_to_tsv(lines)
