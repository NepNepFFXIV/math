roman_to_int = { 
    'M': 1000, 
    'D': 500, 
    'C': 100, 
    'L': 50, 
    'X': 10, 
    'V': 5, 
    'I': 1
} 

int_to_roman = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

num_base = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


def to_roman(integer):
    result = ""
    for base_value in num_base:
        q, r = divmod(integer, base_value)
        if q > 0:
            result += int_to_roman[base_value] * q
            integer = r
    return result


def from_roman(string):        
    p = 0
    result = 0
    for i in range(len(string)-1, -1, -1): 
        temp = roman_to_int[string[i]]
        if temp >= p:
            result += temp
        else: 
            result -= temp
        p = temp
    return result

if __name__ == "__main__":
    print(to_roman(3549))
    print(from_roman('MCMIV'))