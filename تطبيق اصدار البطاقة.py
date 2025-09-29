EG=input('Are you Egyptian?(yes.no)\n').lower()
if EG=='yes':
    print('Good that is first step ')
    age=input('are you 18 years old\n ').lower()
    if age>='yes':
        print ('The card has been issued. ')
    else:
        print('You are still young ')
else:
    print('This is for Egyptians only ')