def alphabet_position(input_string):
    input_string = input_string.lower()
    output = []
    for character in input_string:
        number = ord(character) - 96
        if(number>0):
            output.append(str(number))
    output = " ".join(output)
    return output.strip()

sentence = "The sunset sets at twelve o'clock"

alphabet_position(sentence)
