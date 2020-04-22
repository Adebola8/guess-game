import random

def easy_level():
    print( ' You are in the easy level \n'
         ' You have a maximum of 6 guesses \n'
        ' You have to choose a number between 1 and 10 \n'
         )

    secret_number=random.randint(1, 10)
    Guess_count=0
    Guess_limit=6
    
    while Guess_count<Guess_limit:
        while True:
            try:
                User_guess= int(input(" Your guess: "))
                Guess_count +=1
                limit= 6 - Guess_count
                print(f'( You have {limit } guesses left)')
            except ValueError:
                print(" oops not an integer! Enter a value  ")
                continue
            break
            
           
        if User_guess <1 or User_guess> 10:
             print(' You have to enter a value between 1 and 10 \n'
             	       ' That was wrong \n'
             	       )
             	       
           
            
        elif User_guess == secret_number:
            print(' You got it right \n'
                    ' Game Over \n'
                 )
            break
            
        elif User_guess != secret_number:
            print('That was wrong \n')
                    
            
    else:
        print("Your guess chance is exhausted, Game Over") 
        


def medium_level():
    print(' You are in the medium level \n'
    	      ' You have a maximum of 4 guesses \n'
    	      ' You have to choose a number between 1 and 20 \n'
    	      )
    secret_number=random.randint(1, 20)
    Guess_count=0
    Guess_limit=4
    while Guess_count<Guess_limit:
        while True:
            try:
                User_guess= int(input(" Your guess: "))
                Guess_count +=1
                limit= 4 - Guess_count
                print(f'(" You have {limit } guesses left")')
            except ValueError:
                print(" oops not an integer! Enter a value  ")
                continue
            break
          
        if User_guess <1 or User_guess>20:
            print(' That was wrong \n'
            	      ' You have to enter a value between 1 and 20 \n'
            	   ) 
            
           
        elif User_guess == secret_number:
            	    print(' You got it  right>\n'
            	            ' Game Over \n'
            	           )
            	    break
            	    
        elif User_guess != secret_number:
                  print('That was wrong \n')
                  
        
    else:
        print("Your have reached your guess limit, Game Over")
           

def hard_level():  
    print(' You are in the hard level \n'
    	' You have a maximum of 3 guesses \n'
    	' You have to choose a number between 1 and 50 \n'
    	      )
    secret_number=random.randint(1, 50)
   
    number= range(1,51)
    x= (number)
    Guess_count=0
    Guess_limit=3
    while Guess_count<Guess_limit:
        while True:
            try:
                User_guess= int(input(" Your guess: "))
                Guess_count +=1
                limit= 3 - Guess_count
                print(f'(" You have {limit } guesses left")')
            except ValueError:
                print(" oops not an integer! Enter a value  ")
                continue
            break
             
             
                
         
        if User_guess <1 or User_guess>50:
            print(' That was wrong \n'
            	      ' You have to enter a value between 1 and 50 \n'
            	   ) 
          
        elif User_guess == secret_number:
            print( ' You got it right \n'
                      ' Game Over \n'
                   )
            break
               
        elif User_guess != secret_number:
            print('That was wrong \n')  
        
    else:
        print("Your chance of guesses is exhausted, Game Over")
        
        
        
            
           
  

def game_level():
    print(' Hello, welcome to the guess game')
    User= input('Choose a game level to proceed; easy, medium or  hard:')
 
    while True:
        if User.upper() =="EASY":
                easy_level()
                break

        elif User.upper() =="MEDIUM":
                medium_level()
                break

        elif User.upper() =="HARD":
                hard_level()
                break
                
        else:
            game_level()
            break
            
            
                

game_level()