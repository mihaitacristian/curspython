######### Guessing Game

# secret = "Andra"
# guess = ""
# guess_count = 0
# guess_limit = 6
# out_of_guesses = False

# while secret != guess  and not out_of_guesses:
#     if guess_count<guess_limit: 
#         guess= input("Enter the secret ..: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True


# if out_of_guesses:
#     print ("You lose!!")
# else:
#     print ("You win!")    


secret_number = 10
concurent = int(input("Ghiceste numarul corect ...: "))
secret_conter = 0
secret_limit = 10
out_of_luck = False

while concurent != secret_number and not out_of_luck:
    if secret_conter<secret_limit:
        concurent = int(input("Ghiceste numarul corect ...: "))
        secret_conter += 1
    else:
        out_of_luck=True

if out_of_luck:
    print("Keept trying....!")
else:
    print("you found the secret")    
