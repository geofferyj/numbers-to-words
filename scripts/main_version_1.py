import re


# dictionary of number words
number_words = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninty',
    '00': 'hundred',

}
# Receives  input
while True:
    number = input('please enter a number: ').strip()  # .strip() removes trailing spaces
    if number.isdigit():  # checks if the string is composed of only numbers
        break
    print('please enter an integer between 0 and 1000')  # if it doesn't loop again

# remove starting zeros if any
number = number.lstrip('0')
    
# Split input into d|dd|ddd,ddd,...,ddd
rnumber = number[::-1]

lrnumber = [[rnumber[i:i+3]] for i in range(0, len(rnumber), 3)]  # splits the number  into 3 digits list

rlrnumber = lrnumber[::-1]

lnumber = []
for i in range(len(rlrnumber)):
    lnumber.append(rlrnumber[i][0][::-1])  # stores the final list

counter = 0
# String processing begins
for i in lnumber:
    
    if re.findall(r'^0?$', i):  # match one zero
        print(number_words.get(i))  # prints zero
        break  # exits loop
    
    elif re.findall(r'^0+$', i):  # match 1 or more zeros
        print('zeros')  # prints zeros
        break
    
    # matches the first 1 or 2 digits eg. 1 23 12
    if len(i) < 3:
        if len(i) == 1 and i[0] != '0':
            print(number_words.get(i[0]), end=' ')
            
        elif len(i) == 2 and i[0] == '1':
            print(number_words.get(i[0] + i[1]), end=' ')
            
        elif len(i) == 2 and i[0] != '1' and i[0] != '0':
            print(number_words.get(i[0] + '0'), end=' ')
            print(number_words.get(i[1]), end=' ')
    
    # match other digits    
    else:
        if i[0] != '0':
            print(number_words.get(i[0]), number_words.get('00'), end=' ')
            
        if (i[1] != '0') and (i[1] == '1'):
            print('and', number_words.get(i[1] + i[2]), end=' ')
        
        elif i[1] != '0':
            print('and', number_words.get(i[1] + '0'), end=' ')

        if i[1] == '1' and i[2] != '0':
            pass
        
        if (i[0] == '0' and i[1] == '0') and i[2] != '0':
            print('and', number_words.get(i[2]), end=' ')
        
        elif i[2] != '0' and i[2] != '1':
            print(number_words.get(i[2]), end=' ')

    # if len(lnumber) - counter == 0:
    #     continue
    
    if len(lnumber) - counter == 2:
        print('thousand', end='')
        
    elif len(lnumber) - counter == 3:
        print('million', end='')
        
    elif len(lnumber) - counter == 4:
        print('billion', end='')
        
    elif len(lnumber) - counter == 5:
        print('trillion', end='')
        
    elif len(lnumber) - counter == 6:
        print('quadrillion', end='')
        
    elif len(lnumber) - counter == 7:
        print('quintillion', end='')
        
    elif len(lnumber) - counter == 8:
        print('sextillion', end='')
        
    elif len(lnumber) - counter == 9:
        print('septiillion', end='')
        
    elif len(lnumber) - counter == 10:
        print('octillion', end='')
        
    elif len(lnumber) - counter == 11:
        print('nonillion', end='')
        
    elif len(lnumber) - counter == 12:
        print('decillion', end='')
        
    else:
        continue
    
    print(',', end=' ')
    counter += 1
