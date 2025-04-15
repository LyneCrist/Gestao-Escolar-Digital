import re


class CommonsUtil:

    ALPHA_PATTERN = "[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\\-_\\s]+$"

    ALPHA_NUMERIC_PATTERN = "[A-Za-z0-9.-_]+$"

    ALPHA_NUMERIC_CHARACTER_PATTERN = "[A-Za-z0-9_À-ÿ.-_\\s]+$"

    NUMERIC_PATTERN = "[0-9]+$"

    PHONE_NUMERIC_PATTERN = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"

    def __init__(self):
        pass

    def remove_characters(self, text: str) -> str:
        return re.sub("[^0-9]", "", text)

    def find_numbers(self, text: str):
        return re.findall(r"[0-9]+", text)

    def is_alpha_pattern(self, text: str):
        return re.match(self.ALPHA_PATTERN, text)

    def is_numeric_pattern(self, text: str):
        return re.match(self.NUMERIC_PATTERN, text)

    def is_alpha_numeric_character_pattern(self, text: str):
        return re.match(self.ALPHA_NUMERIC_CHARACTER_PATTERN, text)

    def is_phone_pattern(self, text: str):
        return re.match(self.PHONE_NUMERIC_PATTERN, text)
