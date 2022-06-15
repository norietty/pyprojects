"""
This Script will implement the route cypher 
"""
from load_dictionary import load

# Get the cypher text 
cypher_text = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

#Get the mitrix deminsion and key to decyrept the message 
num_of_cols = int(input('Enter the number of column please:'))
num_of_rows = int(input('Enter the number of rows:'))
input_key = input('Enter your key:')
input_keys = []
i = 0
while i < len(input_key):
    if input_key[i] == '-':
        input_keys.append(-int(input_key[i+1]))
        i += 2
    else:
        input_keys.append(int(input_key[i]))
        i += 1


cypher_list = cypher_text.split(' ')

#Construct the trnslation matrix 
trans_matrix = [None] * num_of_cols

for n in input_keys:
    if n > 0:
        trans_matrix[abs(n)-1] = cypher_list[0:num_of_rows][::-1]
        cypher_list = cypher_list[num_of_rows:]
    else:
        trans_matrix[abs(n)-1] = cypher_list[0:num_of_rows]
        cypher_list = cypher_list[num_of_rows:]

#Reconstruct the string from the translation matrix.

message = ''

for i in range(num_of_rows):
    for col in trans_matrix:
        word = col.pop()
        message += word + ' '

print(message)


