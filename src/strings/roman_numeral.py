class RomanNumeral:

    def roman_to_int(self: str) -> int:
        roman_to_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for i in range(len(self) - 1, -1, -1):
            current_value = roman_to_int_map[self[i]]
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            prev_value = current_value

        return result

    def int_to_roman(self: int) -> str:
        roman_to_int_map = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
                            ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
                            ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

        result = ''

        for r, n in roman_to_int_map:
            while self >= n:
                result += r
                self -= n

        return result
