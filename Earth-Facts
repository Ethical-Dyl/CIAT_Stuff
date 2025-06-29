# Step 1. Program 1. Write a Python program that includes at least one outer loop and one inner loop.

import requests # I am importing the requests module for my API call on line 18

seen_facts = 0 # I am creating a var that has a value of 0, this is a counter used for our first while loop.

# Below is the while loop(s), the first loop asks the user if they would like to see some facts about earth.
# If they say no the program ends and a goodbye message prompts. 
# If they say yes then the second loop will be iterated, generating the first facts and then adding +1 to the seen_facts counter.
# In the second loop they will be asked if they would like to see more facts, if yes they see more and loop again, if no the program exits. 

while seen_facts < 1: # First Loop
    try:
        see_space = input('Would you like to see some Earth facts? [yes, no] ')
        if see_space.lower() == "yes": #The .lower() ensures the user can enter Yes, yes, No, no. 
            while True: # Second Loop
                try: 
                    response = requests.get('https://api.bootprint.space/all/earth') # This is a free api, no auth or apikeys needed
                    data = response.json() # Here I get the response and place it in the data variable for parsing
                    fact = data['fact'] # Here I take the 'fact' entry from the json response from the variable above 'data'
                    print(fact) 
                    seen_facts += 1 # Increase coutner so the user won't get prompted again once in the first loop if they say no in this second loop
                    see_more = input('Would you like to see more Earth facts? ')
                    if see_more.lower() == "yes":
                            continue
                    if see_more.lower() == "no":
                            print('Hope you learned something new!')
                            exit(0)
                    else:
                         raise ValueError # If this is raised (called on) the ValueError exeption is called. 
                    

                except KeyboardInterrupt: # The user hit CTRL + C.
                    print('User Exit')
                except ValueError: # The user entered in a response other than yes or no.
                    print('please answer yes or no')
        

        if see_space.lower() == "no":
             print('No worries, goodbye!')
             exit(0)
        else:
             raise ValueError # Same as other


    except KeyboardInterrupt: # Same as other
          print('User Exit')
    except ValueError: # Same as other
          print('please answer yes or no')
