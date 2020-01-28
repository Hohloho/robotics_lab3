import numpy as np
def alphabet_position(input_string):
    input_string = input_string.lower()
    output = []
    for character in input_string:
        number = ord(character) - 96
        output.append(number)
    output = np.array(output)
    output = output[output >= 0]
    return print(output)

sentence = "The sunset sets at twelve o'clock"

alphabet_position(sentence)
