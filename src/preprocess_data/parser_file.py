import os

from preprocess_data.utils import Utils


class AbcParser(object):

    def __init__(self, filename: str):
        """

         @param filename - The name of the file being read in the
        """
        self._filename = filename

    def read_file(self, encoding='utf-8'):
        """
         Read the file and return a list of lines.


         @return list [ str ] The lines of the file as a list of strings.
         Each string is a line
        """
        with open(self._filename, mode='r', encoding=encoding) as f:
            return f.readlines()

    def get_save_path(self):
        """
         Get the path to save the data.
         It is based on the filename that was passed to the constructor.


         @return The path to save the data to ( string )or None
         if not found ( None will be returned
        """
        return os.path.join(os.path.dirname(self._filename), "new_data.tsv")

    def write_to_tsv(self, lines):
        """
         Write lines to tab separated file.
         This is useful for debugging and to avoid having to re
         - write the file every time it is called

         @param lines - List of lines to write

         @return String of file written
        """
        with open(self.get_save_path(), 'w+', encoding="utf-8") as f:
            f.writelines(lines)


class ParserFile(AbcParser):

    def __init__(self, filename: str):
        """
         Initialize parser from file.
         This is the method that must be overridden by subclasses.
         The filename is used to determine the type of parser to use

         @param filename - The name of the
        """
        super(ParserFile, self).__init__(filename)

    @staticmethod
    def parser_acute_inflammations(line: str) -> str:
        line_list = line.replace('no', 'False').replace('yes', 'True').replace(
            '\n', '').replace(',', '.').split('\t')
        new_line_list = line_list[0:-2]
        if line_list[-2] == 'False':
            if line_list[-1] == 'False':
                new_line_list.append('0')
            else:
                new_line_list.append('2')
        else:
            if line_list[-1] == 'False':
                new_line_list.append('1')
            else:
                new_line_list.append('3')
        return '\t'.join(new_line_list) + '\n'

    @staticmethod
    def parser_heart_disease(line: str) -> str:
        """
         Parses Heart Disease.
         Replace commas with tabs.

         @param line - A line in the file is parsed.

         @return Organized data rows
        """

        if Utils.has_question_mark(line):
            return ""
        return line.replace(",", "\t")

    @staticmethod
    def parser_parkinsons(line: str) -> str:
        if line.startswith('name'):
            return ""
        # Filter the first column of patient names
        line_list = line.replace('\n', '').split(',')[1:]
        # Get Parkinson's prediction results as the last column of the data
        # Status - 0 for healthy and 1 for PD.
        pv = line_list[-7]
        new_line = line_list[0:-7] + line_list[-6:]
        new_line.append(pv)
        return '\t'.join(new_line) + '\n'

    @staticmethod
    def parser_heart_failure_clinical(line: str):
        if line.startswith('age'):
            return ""
        return line.replace(',', '\t')

    @staticmethod
    def parser_primary_tumor(line: str) -> str:
        if Utils.has_question_mark(line):
            return ""
        line_list = line.replace('\n', '').split(',')
        # Get predicted value results
        # histologic-type: epidermoid - 0, adeno - 1, anaplastic - 2
        pv = line_list[5]
        line_list = line_list[:5] + line_list[6:]
        line_list.append(pv)
        return '\t'.join(line_list) + '\n'

    @staticmethod
    def parser_chronic_kidney_disease(line: str):
        """
        column names for predicted values
        ckd - chronic kidney disease
        notckd - not chronic kidney disease
        """
        if Utils.has_question_mark(line):
            return ""
        if not line.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9')):
            return ""
        line_list = line.replace('abnormal', '1').\
            replace('normal', '0').\
            replace('\n', '').\
            replace(' ', '').\
            replace('\t', '').\
            replace('notpresent', '0').\
            replace('present', '1').\
            replace('notckd', '0').\
            replace('yes', '0').\
            replace('no', '1').\
            replace('poor', '0').\
            replace('good', '1').\
            replace('ckd', '1').split(',')
        if len(line_list) != 25:
            return ""
        return '\t'.join(line_list) + '\n'

    def parser_lymphography(line: str) -> str:
        if Utils.has_question_mark(line):
            return ""
        line = line.replace(',', '\t')
        new_line = line[2:len(line)].replace(
            '\n', '') + '\t' + str(int(line[0]) - 1) + '\n'  # noqa E501
        return new_line

    @staticmethod
    def parser_breast_cancer(line: str) -> str:
        if Utils.has_question_mark(line):
            return ""
        arr = line.replace('\n', '').split(',')
        row0 = arr[0].replace('no-recurrence-events', '0'). \
            replace('recurrence-events', '1')
        row1 = arr[1].replace('80-89', '9'). \
            replace('80-89', '8'). \
            replace('70-79', '7'). \
            replace('60-69', '6'). \
            replace('50-59', '5'). \
            replace('40-49', '4'). \
            replace('30-39', '3'). \
            replace('20-29', '2'). \
            replace('10-19', '1'). \
            replace('0-9', '0')
        row2 = arr[2].replace('premeno', '2'). \
            replace('ge40', '1'). \
            replace('lt40', '0')
        row3 = arr[3].replace('55-59', '11'). \
            replace('50-54', '10'). \
            replace('45-49', '9'). \
            replace('40-49', '9'). \
            replace('40-44', '8'). \
            replace('35-39', '7'). \
            replace('30-34', '6'). \
            replace('25-29', '5'). \
            replace('20-24', '4'). \
            replace('15-19', '3'). \
            replace('10-14', '2'). \
            replace('5-9', '1'). \
            replace('0-4', '0')
        row4 = arr[4].replace('36-39', '12'). \
            replace('33-35', '11'). \
            replace('30-32', '10'). \
            replace('27-29', '9'). \
            replace('24-26', '8'). \
            replace('21-23', '7'). \
            replace('18-20', '6'). \
            replace('15-17', '5'). \
            replace('12-14', '4'). \
            replace('9-11', '3'). \
            replace('6-8', '2'). \
            replace('3-5', '1'). \
            replace('0-2', '0')
        row5 = arr[5].replace('no', '1'). \
            replace('yes', '0')
        row6 = arr[6].replace('3', '2'). \
            replace('2', '1'). \
            replace('1', '0')
        row7 = arr[7].replace('right', '1'). \
            replace('left', '0')
        row8 = arr[8].replace('central', '4'). \
            replace('right_low', '3'). \
            replace('right_up', '2'). \
            replace('left_low', '1'). \
            replace('left_up', '0')
        row9 = arr[9].replace('no', '1'). \
            replace('yes', '0')
        # print(arr)
        # print(row0, row1, row2, row3, row4, row5, row6, row7, row8, row9)
        new_line = row1 + '\t' + row2 + '\t' + row3 + '\t' + row4 + '\t' + \
            row5 + '\t' + row6 + '\t' + row7 + '\t' + row8 + '\t' + row9 + \
            '\t' + row0 + '\n'
        return new_line

    @staticmethod
    def parser_bupa(line: str) -> str:
        if Utils.has_question_mark(line):
            return ""
        line = line.replace(',', '\t')
        return line


if __name__ == "__main__":
    with open('../data/Breast_Cancer/breast-cancer.data',
              mode='r',
              encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(ParserFile.parser_chronic_kidney_disease(line))
            ParserFile.parser_chronic_kidney_disease(line)
