f = open('game').read()
f=f.split('\n')
a=[]
for i in f:
    a.append(i.split('$'))
for i in a:
    if '55' in i[2]:
        print('У персонажа '+i[1]+'в игре '+i[0]+'нашлась ошибка с кодом ' +i[2]+'.' +' Дата фиксации: ',i[-1])
        i[2]='Done'
        i[-1] = '0000-00-00'
file = open('game_new.csv', "w")
for i in a:
    if i[-1]=='0000-00-00':
        file.write(('\t'.join(i))+'\n')
