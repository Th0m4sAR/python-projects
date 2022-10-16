morse_dict = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":".-.", "l":".-..", "m":"--", "n":"-.", "o":"---",
"p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", " ":" "}



def toMorse():
    sentence = input("Write down: ")
    morse = []
    chars = sentence.lower()
    for char in chars:
        morse.append(morse_dict[char])
        morse_setence = " ".join(morse)
    print(morse_setence)
    toContinue()
    

def toContinue():
    answer = input("Keep going: y or n   ")
    if answer == "y":
        toMorse()
    elif answer == "n":
        print("Goodbye")
    else:
        print("Please provide a valid answer")
        toContinue()

toMorse()