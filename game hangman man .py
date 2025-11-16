
import random

# Word list
words = ['apple', 'juice', 'cat']
pc = random.choice(words)
show = ['_'] * len(pc)

# Title
print('''                                           
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/   
''')

print('\n')
print(' '.join(show))

# Hangman stages
hangman = [
"""
 ____
|/   |
|    
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \\|
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \\|/
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \\|/
|    |
|   / \\
|
|_____
"""
]

# Game setup
hearts = 5
letters = ['']
print(f'Hearts: {hearts}❤')

# Main game loop
while '_' in show and hearts > 0:
    user = input('Enter a letter:\n').lower()
    
    if user in letters:
        print('You already guessed that letter!')
        print(f'Hearts: {hearts}❤')
        continue

    letters.append(user)
    
    if user in pc:
        for i in range(len(pc)):
            if pc[i] == user:
                show[i] = user
    else:
        print('❌ Wrong!')
        hearts -= 1
        if hearts > 0:
            print(hangman[5 - hearts])
    
    print(' '.join(show))
    print(f'Hearts: {hearts}❤')

# End of game
if '_' not in show:
    print('        *********🎉 You won!*******\n.                 The word was:', ' '.join(pc))
else:
    print('         ********💀 You lost!********\n                      The word was:', ' '.join(pc))
    print(hangman[-1])