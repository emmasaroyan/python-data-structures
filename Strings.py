#the program finds "0.8475" and prints it as a float number
#using find() and slicing

text = "X-DSPAM-Confidence:    0.8475"

number = text.find('0.8475')

print(float(text[number:len(text)]))
