import os
import time

def ver_win(velha,player):
  
    # p--  -p-  --p
    # p--  -p-  --p
    # p--  -p-  --p
    caso_1 =  velha[0][0] == player and velha[1][0] == player and velha[2][0] == player
    caso_2 =  velha[0][1] == player and velha[1][1] == player and velha[2][1] == player
    caso_3 =  velha[0][2] == player and velha[1][2] == player and velha[2][2] == player

    # ppp  ---  ---
    # ---  ppp  ---
    # ---  ---  ppp
    caso_4 =  velha[0][0] == player and velha[0][1] == player and velha[0][2] == player
    caso_5 =  velha[1][0] == player and velha[1][1] == player and velha[1][2] == player
    caso_6 =  velha[2][0] == player and velha[2][1] == player and velha[2][2] == player
    
    # p--  --p
    # -p-  -p-
    # --p  p--
    caso_7 =  velha[0][0] == player and velha[1][1] == player and velha[2][2] == player
    caso_8 =  velha[0][2] == player and velha[1][1] == player and velha[2][0] == player

    if caso_1: return True 
    if caso_2: return True 
    if caso_3: return True
    if caso_4: return True 
    if caso_5: return True
    if caso_6: return True
    if caso_7: return True 
    if caso_8: return True    

def x_y():

   x = int(input('cordenada x \n---> '))
   y = int(input('cordenada y \n---> '))
   print(f'cordenada x = {x} cordenada y = {y}') 
   return x,y    

def clear():  os.system('cls'), time.sleep(0.4)
   
qual_player = 'x'
velha_ =  [['-','-','-'],
           ['-','-','-'],
           ['-','-','-']]


for i in range(9):
 clear()
 jogo_da_velha = f'''
 JOGO DA VELHA

     (y)↦
   (x)     0    1     2 
    ↧  0 {velha_[0]    } 
       1 {velha_[1]    } 
       2 {velha_[2]    }
      
 o player jogando é {qual_player} \n\n '''

 
 print(jogo_da_velha)

 loop_XY = True 

 while loop_XY == True:
    time.sleep(0.5)
    x, y = x_y()

    if velha_[x][y] == '-':
     velha_[x][y] = qual_player
     loop_XY = False
    else: 
      print('espaço invalido')
      loop_XY = True

 if ver_win(velha_, qual_player):
   clear()
   print(f'''
 JOGO DA VELHA

     (y)↦
   (x)     0    1     2 
    ↧  0 {velha_[0]    } 
       1 {velha_[1]    } 
       2 {velha_[2]    }
      
 o player gahador é o {qual_player}\n\n''')
   
   break

 if   qual_player == 'x': qual_player = 'o' 
 elif qual_player == 'o': qual_player = 'x' 


if i == 8 and ver_win(velha_, qual_player) != True: 
   clear()
   print(f'''
 JOGO DA VELHA

     (y)↦
   (x)     0    1     2 
    ↧  0 {velha_[0]    } 
       1 {velha_[1]    } 
       2 {velha_[2]    }
      
 DEU VElHA \n\n''')
   
fim = input('fim')
   
