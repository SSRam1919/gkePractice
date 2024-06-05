import morse_code # type: ignore
import random2 # type: ignore

name = input()

def generate_text(name):
    
    enc_str = morse_code.encrypt(name)

    #printing encrypted morse code of given string
    #print(enc_str)
    enc_str_wo_space = ""

    for i in enc_str:
        if(i!=" "):
            enc_str_wo_space+=i
    #priting encrypted morse code with out space
    #print(enc_str_wo_space)

    converted_morse_code = ""

    n = 0
    res = []
    while n < len(enc_str_wo_space):
        rand_num = random2.randint(2,4)
        res.append(enc_str_wo_space[n:rand_num+n])
        res.append(" ")
        n += rand_num

    converted_morse_code = ''.join(res)
    output_without_numerals = morse_code.decrypt(converted_morse_code)
    #print("converted morse code : ",converted_morse_code)
    #print("result list res      : ",res)
    #print("---------------------------------------------------")
    #print("converted morse code decrypted to alphabets from final output")
    #print("---------------------------------------------------")
    #print(output_without_numerals)
    #print(morse_code.decrypt(enc_str))
    #print("---------------------------------------------------")
    #print("converted morse code decrypted to alphabets from result list")
    #print("---------------------------------------------------")
    #for i in res:
    #    if (i!=" "):
    #        print(morse_code.decrypt(i))

    nu = []
    for i in range(0,5):
        num = random2.randint(2,5)
        num = str(num)
        nu.append(num)

    numeral_output = ''.join(nu)

    final_output = output_without_numerals+numeral_output
    return final_output

