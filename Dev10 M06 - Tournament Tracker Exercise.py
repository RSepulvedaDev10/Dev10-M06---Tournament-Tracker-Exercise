import csv

def signUp(participants):

    print(f"Participant Sign Up")
    print(f"====================\n")
    
    while True:
        participantname = input("Please enter the name of the participant: ").lower()
        
        participantposition = int(input("Please enter the slot you wish to place the participant: "))
        
        try:
            
            if participants[participantposition] == None and participantposition < (total + 1) and participantposition != 0:
                participants[int(participantposition)] = participantname
                print(f"Participant successfully added.")
                break
            elif participants[participantposition] != None:
                print(f"{participantposition} is already taken. Please choose another slot.")
            else:
                print(f"This is not a valid slot. Try again.")
        except:
            print(f"This is not a valid slot. Try again.")

    
    print(f"{participantname} has been signed up to the starting slot #{participantposition}")
    return participants
        
    
def cancelSignUp(participants):
    
    print(f"Participant Cancellation")
    print(f"====================\n")
    
    while True:
        participantname = input("Please enter the name of the participant: ").lower()
    
        participantposition = int(input("Please enter the slot you wish to remove the participant from: "))
        
        try:
            
            if participants[participantposition] == participantname:
                participants[participantposition] = None
                print(f"Participant successfully removed")
                break
            elif participants[participantposition] != participantname:
                print(f"{participantname} is not in this slot.")
            else:
                print(f"This is not a valid entry. Try again.")
        except:
            print(f"This is not a valid entry. Try again.")
    
    return participants
        
        
    
def viewParticipants(participants):
    
    print(f"View Participants")
    print(f"====================\n")
    
    while True:
        print(f"There are currently {str(len(participants))} slots in the tournament.")
        participantposition = int(input("Please enter the number of a slot in range you wish to view: "))
        
        if participantposition < (len(participants)) + 1 and participantposition > 0:
            print(f"Pulling up Participants")
    
            for i in range (participantposition - 5, participantposition + 6):
                    if i > 0:
                        print(f"#{i}: {participants[i]}")
            break
        else:
            print(f"This is not a valid entry. Try again.")
            
        
    
def saveTournament (participants):
    
    print(f"Save Tournament")
    print(f"====================\n")
    
    while True:
        saveprompt = input("Would you like to save your changes to CSV (Y/N)? ").lower()
        
        if saveprompt == "y":
            with open('Tournament Tracker Roster.csv') as file:
                for i in range(1, len(participants)+1):
                    try:
                        file.write('{},{}\n').format(i, participants[i])
                    except:
                        continue
                print(f"Tournament has been successfully saved")
                file.close()
                break
        elif saveprompt == "n":
            print(f"Returning to menu.")
            break
        else:
            print(f"This is not a valid entry. Please enter 'Y' or 'N' in the prompt.")
                                           

def exitTourment ():

    print(f"Exit Tournament")
    print(f"====================\n")
    print(f"All unsaved changes will be lost")
    
    while True:
        
        exitprompt = str(input("Type 'y' to confirm exit or press any other key to cancel: ")).strip().lower()
        
        if exitprompt == "y":
            print(f"Understood. Have a great day")
            quit()
        else:
            print(f"Returning to menu")
            break
                
                

print(f"Welcome to Tournaments R Us")
print(f"============================")


total = int(input("Enter the number of participants: "))

participants = [None] * (total + 1)


    
print(f"There are {str(total)} participant slots now avaialable for the tournament!")
    
while(True):
    
    menuselection = 0
    
    print(f"Main Menu")
    print(f"=========")
    print(f"1. Sign Up")
    print(f"2. Cancel Sign Up")
    print(f"3. View Participants")
    print(f"4. Save Changes")
    print(f"5. Exit Tournament")
    
    menuselection = input("Please input a number corresponding with the option you would like to choose: ")
    
    if menuselection == "1":
        participants = signUp(participants)
    elif menuselection == "2":
        participants = cancelSignUp(participants)
    elif menuselection == "3":
        viewParticipants(participants)
    elif menuselection == "4":
        saveTournament(participants)
    elif menuselection == "5":
        exitTourment ()
    else:
        print(f"This is not a valid entry. Try again")