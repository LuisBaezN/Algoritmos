from morse import MORSE_CODE

def decode_morse(morse_code):
    morse_code = morse_code.strip() + ' '
    letter = []
    res = []
    cont = 0
    
    for e in morse_code:
        if e == ' ':
            if len(letter) == 0:
                cont += 1
            if cont == 2:
                letter.append(' ')
                cont = 0
            if len(letter) > 0:
                if letter[0] == ' ':
                    res.append(''.join(letter))
                else:
                    res.append(MORSE_CODE[''.join(letter)])
            letter = []
        else:
            cont = 0
            letter.append(e)
    return ''.join(res)


if __name__ == '__main__':
    cad = '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '
    print(decode_morse(cad))