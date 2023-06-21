import os


class AbcParser(object):

    def __init__(self, filename: str):
        """

         @param filename - The name of the file being read in the
        """
        self._filename = filename

    def read_file(self, encoding='utf-8') -> list[str]:
        """
         Read the file and return a list of lines.


         @return list [ str ] The lines of the file as a list of strings.
         Each string is a line
        """
        with open(self._filename, mode='r', encoding=encoding) as f:
            return f.readlines()

    def get_save_path(self) -> str:
        """
         Get the path to save the data.
         It is based on the filename that was passed to the constructor.


         @return The path to save the data to ( string )or None
         if not found ( None will be returned
        """
        return os.path.join(os.path.dirname(self._filename), "new_data.tsv")

    def write_to_tsv(self, lines: list[str]) -> str:
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
        return line.replace(",", "\t").replace("?", "0.0")


if __name__ == "__main__":
    with open('data/Acute_Inflammations/diagnosis.data',
              mode='r',
              encoding='utf-16') as f:
        ParserFile.parser_acute_inflammations(f.readline())
