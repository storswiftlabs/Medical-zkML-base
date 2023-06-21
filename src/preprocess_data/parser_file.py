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
                new_line_list.append('4')
        return '\t'.join(new_line_list) + '\n'

    @staticmethod
    def parser_heart_disease(line: str) -> str:
        """
         Parses Heart Disease.
         Replaces spaces with tabs and question mark with 0.

         @param line - Line from the text file.

         @return Line with spaces replaced
        """

        if Utils.has_question_mark(line):
            return ""
        return line.replace(",", "\t").replace("?", "0.0")

    @staticmethod
    def parser_parkinsons(line: str) -> str:
        if line.endswith('PPE\n') and line != "":
            return ""
        line_list = line.replace('\n', '').split(',')[1:]
        status = line_list[-7]
        new_line = line_list[0:-7] + line_list[-8:]
        new_line.append(status + '\n')
        return '\t'.join(new_line)

    @staticmethod
    def parser_heart_failure_clinical(line: str):
        if line.startswith('age'):
            return ""
        line_list = line.replace('\n', '').split(',')
        return '\t'.join(line_list) + '\n'

    @staticmethod
    def parser_chronic_kidney_disease(line: str):
        if Utils.has_question_mark(line):
            return ""
        if not line.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9')):
            return ""
        line = line.replace('abnormal', '0').\
            replace('normal', '1').\
            replace('\n', '').\
            replace(' ', '').\
            replace('\t', '')
        line = line.replace('notpresent', 'False')
        line = line.replace('present', 'True')
        line = line.replace('notckd', 'False')
        line = line.replace('yes', 'True')
        line = line.replace('no', 'False')
        line = line.replace('poor', 'False')
        line = line.replace('good', 'True')
        line_list = line.replace('ckd', 'True').split(',')
        if len(line_list) != 25:
            return ""
        # print(line_list)
        pc = line_list[6]
        line_list = line_list[:6] + line_list[7:]
        line_list.append(pc)
        return '\t'.join(line_list) + '\n'

    def parser_lymphography(line: str) -> str:
        line = line.replace(',', '\t')
        new_line = line[2:len(line)].replace('\n', '') + '\t' + str(int(line[0]) - 1) + '\n' # noqa E501
        return new_line


if __name__ == "__main__":
    with open('data/Chronic_Kidney_Disease/chronic_kidney_disease.arff',
              mode='r',
              encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(ParserFile.parser_chronic_kidney_disease(line))
            ParserFile.parser_chronic_kidney_disease(line)
