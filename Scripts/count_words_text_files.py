class CountWord:
    """
    Class count the word in the
    Text file
    """

    def __init__(self, file_path: str):
        self.data_set = {}
        with open(file_path, "r") as file_obj:
            words = file_obj.read().split()
            for i in words:
                self.data_set[i] = words.count(i)

    def count_all(self) -> dict:

        return self.data_set

    def count_this(self, query) -> int:

        return self.data_set[query]


if __name__ == "__main__":
    file = input("Enter the file path: ")
    cw = CountWord(file)
    print(cw.count_all())
