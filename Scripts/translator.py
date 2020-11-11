from googletrans import Translator, LANGUAGES


class Translation:
    """
    Translate a text files !

    Param
    -----
        LANGCODE
    """

    def __init__(self, lang_code: str):
        self.Translator = Translator()
        self.lang_code = lang_code

    def Translate(self, text: str) -> str:

        return self.Translator.translate(text, dest=self.lang_code).text

    def from_file(self, input_path: str, output_path: str) -> None:
        """
        Translate Text File of one language into another language

        Param
        -----
            :input_path -> path of source file
            :ouput_path -> file name or path of output_file
        """

        with open(input_path, "r") as file_obj:
            lines = file_obj.read()

        with open(output_path, "w") as file_obj:
            file_obj.write(str(self.Translate(lines)))

    def __repr__(self) -> str:

        return f"{self.__class__}({self.lang_code})"


if __name__ == "__main__":
    print(LANGUAGES)  # To Get all Avialable Languages
    t = Translation("ta")
    print(t.Translate("Hello World !"))
    # print(t.from_file("sample.txt", "sample_out.txt"))
