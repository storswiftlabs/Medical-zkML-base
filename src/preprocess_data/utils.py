class Utils:

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
