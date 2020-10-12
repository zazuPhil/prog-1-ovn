svar = input('Hur tar du dig hem ')

if svar == 'gå':
    print('Du få motion, sent')
elif svar == 'cykla':
    print('Du få motion, I tid')
elif svar == 'buss':
    print('få inte motion, kom tidigare')
    buss = input('25 kr för bussbiljett? [ja/nej]')

    if buss == 'ja':
        print('förlorade 25 kr')
    elif buss == 'nej':
        print('spara 25 kr')
    else:
        print('gå hem')
else:
    print('få motion, trött')