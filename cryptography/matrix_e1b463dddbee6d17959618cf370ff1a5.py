def bytes2matrix(text):
    # Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    # Converts a 4x4 matrix into a 16-byte array.  """
    plain_text_message = []
    
    for i in range(4):
        for j in range(4):
            plain_text_message.append(chr(matrix[i][j]))

    return plain_text_message


matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(bytes2matrix("hhhhfasdfasdfasdfasdf"))
