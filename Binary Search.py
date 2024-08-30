import random as rd
import os
import time

#Func clear console
def clear(): os.system('cls'), time.sleep(0.6)

numLimit = int(input('\n Escolha a quntidade de numeros  \n\n ->'))
nums = []
numRodadas = 0

#Adicionar numeros na lista
for i in range(1,numLimit + 1):
    nums.append(i)

#Numero a se achar    
rdNum = rd.randint(1,max(nums))
maxNum, minNum = max(nums), min(nums)

while 1:
    numRodadas += 1
    clear()
    print(nums)
    
    advNumBot = int(input('\n \033[35mDiga qual numero o bot escolheu \n\n -> \033[0;0m'))

    if advNumBot >  maxNum:
      print('\033[31mNumero maior que a quantidade de numeros\033[0;0m')
      input() 
    else:
        if advNumBot != rdNum:
           
           if advNumBot > rdNum:
              for j in range(advNumBot - 1, maxNum):
                  nums[j] = '-'
           if advNumBot < rdNum:
              for j in range(0, advNumBot):
                  nums[j] = '-'
        else:
            print(f'\033[32mVoce acerotu o numero com {numRodadas} rodadas\033[0;0m')
            break