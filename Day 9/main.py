from file_loading import load_file_readlines_int
from XMAS import xmas_analyser
from XMAS import xmas_code_breaker

def code_cracker():
    code_file = "input.txt"
    code_stream = load_file_readlines_int(code_file)

    list_length = 25

    for list_pointer in range(list_length, len(code_stream)):
        search_number = code_stream[list_pointer]
        search_list = code_stream[list_pointer - list_length: list_pointer]

        if not xmas_analyser(search_list, search_number):
            xmas_invalid = search_number
            code = xmas_code_breaker(code_stream, xmas_invalid)
            print(code)


if __name__ == '__main__':
    code_cracker()
