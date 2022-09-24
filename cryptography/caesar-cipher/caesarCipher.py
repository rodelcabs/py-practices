class CaesarCipher:
    def __init__ (self, shift, useUpperCase=False):
        self.shift = shift
        self.useUpperCase = useUpperCase
        self.maxLength = 26

        # generate a list of alphabet
        self.alpha = list(range(self.maxLength))
        self.alphabet = [chr(char + 97) for char in self.alpha]
    
    def encrypt(self, text):
        output = ""
        # char x = (x + n) % 26
        # where n = shift and x = character
        for x in text:
            if(x == " "):
                output += x
                continue

            charIndex = (self.alphabet.index(x.lower()) + self.shift) % self.maxLength
            char = self.alphabet[charIndex]

            output += char.upper() if self.useUpperCase else char
        
        return output

    def decrypt(self, cipher):
        decrypted = ""

        # char x = (x - n) % 26
        for x in cipher:
            if(x == " "):
                decrypted += x
                continue
            
            charIndex = (self.alphabet.index(x.lower()) - self.shift) % self.maxLength
            char = self.alphabet[charIndex]
            
            decrypted += char.upper() if self.useUpperCase else char

        return decrypted


caesarCipher = CaesarCipher(4, True)
encrypted = caesarCipher.encrypt("The quick brown fox jumps over the lazy dog")
decrypted = caesarCipher.decrypt("geiwev gmtliv")
print("text: 'The quick brown fox jumps over the lazy dog'")
print("cipher: " + encrypted)

