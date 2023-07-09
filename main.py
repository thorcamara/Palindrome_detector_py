frase = str(input('Type your frase: ')).strip().upper()
words = frase.split()
join = ''.join(words)
#reverse = '' # Method 1
reverse = join[::-1] # Method 2
'''for letter in range(len(join) -1, -1, -1):
    reverse += join[letter]''' # Method 1
if reverse == join:
    print('The reverse of \033[1;32m{}\033[m is \033[1;32m{}\033[m'.format(join, reverse))
    print('We have a \033[1;33mPalindrome\033[m!')
else:
    print('The reverse of \033[1;32m{}\033[m is \033[1;31m{}\033[m'.format(join, reverse))
    print('The typed sentence is not a \033[1;33mPalindrome\033[m')
