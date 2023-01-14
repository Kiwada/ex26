frase = str(input('digite uma frase:')).upper().strip()
# quantas vezes aparece a letra A
#Em que Posição ela aparece a primeira vez
#Em que posição ela aparece a última vez
print('A letra a Aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) 