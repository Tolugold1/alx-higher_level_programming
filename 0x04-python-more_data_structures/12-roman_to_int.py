def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in dic:
        for j in roman_string:
            if j in i:
                if len(roman_string) == 1:
                    result += dic[i]
                elif len(roman_string) > 1:
                    result += dic[i]
    return result
