MORSE_CODE ={
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}

# mors_code= "...---..."
# a = 0
# l_letters = [] # karsilastigi her yeni kelimeyi icine yazdirmak istiyorum.
# while a< len(mors_code):
#     letters = ""   # her kelimeyi words icne yazdirmak istiyorum
#     while mors_code[a]!= " ": # bosluk gormedigi sürece eklemeye devam edecek
#         letters += mors_code[a]
#         a += 1
#         if len(mors_code)== a: # son kelime biterken bosluk olmayacagindan bir cikis sartina ihtiyac var.
#             break
#     l_letters.append(letters) # her yeni kelime listeye eklenir.
#     a += 1
# # print(l_letters) # buraya kadar sprit metodunun yaptigi isi yapmis olduk.
# b = 0
# l_words= []
# while b< len(l_letters):
#     words= ""
#     while l_letters[b] != "":
#         words += Mors_dict[l_letters[b]]
#         b += 1
#         if len(l_letters)==b:
#             break
#     b += 1
#     if words!="":
#         l_words.append(words)
# words_t= ""
# for i in range(len(l_words)):
#     if i!=len(l_words)-1:
#         words_t += l_words[i] + " "
#     else:
#         words_t += l_words[i]
# print(words_t)

def decodeMorse(morse_sequence):
    words = []
    for morse_word in morse_sequence.split('   '):
        for morse_char in morse_word.split(' '):
            word = ''.join(MORSE_CODE.get(morse_char, ''))
        if word:
            words.append(word)
    return ' '.join(words)
print(decodeMorse("...---..."))