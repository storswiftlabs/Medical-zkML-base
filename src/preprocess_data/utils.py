import re


class Utils:

    @staticmethod
    def has_question_mark(line: str) -> bool:
        pattern = re.compile(r'\?', re.IGNORECASE)
        findRes = re.findall(pattern, line)
        return len(findRes) > 0

    @staticmethod
    def parseInt(line: str) -> str:
        splitLine = line.split(',')
        for i, v in enumerate(splitLine):
            try:
                nl = v.split('.')
                if int(nl[1]) != 0:
                    break
                v = str(int(float(v)))
            except (ValueError, IndexError):
                break
            finally:
                splitLine[i] = v
        return ','.join(splitLine)

    @staticmethod
    def feature_two_combine_into_one(feature1, feature2):
        """
         Feature_two_combine_into_one
         Feature two combine into one
         Parameters:
             feature1, feature2
         Returns:
             mix
         Mixed type:
             src type:dst type
             0 0:0
             1 0:1
             0 1:2
             1 1:3
        """
        # print("cc debug feature_two_combine_into_one", feature1, feature2, type(feature1))
        if feature1 == 'False':
            if feature2 == 'False':
                return '0'
            else:
                return '2'
        else:
            if feature2 == 'False':
                return '1'
            else:
                return '3'
