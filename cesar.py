class cesar :
    alphabet = list("abcdefghijklmnopqrstuvwxyz") #used to code and decode every letter in message

    def __init__(self,message):
        self.message = message.lower()
    
    def code(self,key):

        message_list, code_index, coded_message = list(self.message) , [] , ""
       
        for i in range(len(message_list)):

            if message_list[i] in cesar.alphabet: #verify if evrey letter in message is in alphabet

                if (cesar.alphabet.index(message_list[i])+key >= len(cesar.alphabet)):
                    code_index.append((cesar.alphabet.index(message_list[i])+key)-len(cesar.alphabet)) #adding index of coded letters to list

                else:
                    code_index.append(cesar.alphabet.index(message_list[i])+key)
            
        for i in range(len(code_index)):
            coded_message+= cesar.alphabet[code_index[i]] #concatenation

        return coded_message
    
    def decode(self,key):

        coded_message, decode_index, decoded_message = list(self.message) , [] , ""

        for i in range(len(coded_message)): 

            if coded_message[i] in cesar.alphabet: #verify if evrey letter in message is in alphabet

                if (cesar.alphabet.index(coded_message[i])-key < 0):                   
                    decode_index.append((cesar.alphabet.index(coded_message[i])-key)+len(cesar.alphabet)) #adding index of decoded letters to list
                
                else:
                    decode_index.append(cesar.alphabet.index(coded_message[i])-key)
            
        for i in range(len(decode_index)):
           
           decoded_message+= cesar.alphabet[decode_index[i]] #concatenation

        return decoded_message

#main

test1= cesar('hello')
print(test1.code(3))

test2 = cesar('khoor')
print(test2.decode(3))
            