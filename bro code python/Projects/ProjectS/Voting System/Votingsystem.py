nominee1 = input("Enter name of the 1st nominee: ")
nominee2 = input("Enter name of the 2nd nominee: ")
nominee3 = input("Enter name of the 3rd nominee: ")

# initially vote count for both must be 0;
nm1_votes = 0
nm2_votes = 0
nm3_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter  = len(voter_id)

while True:
    if voter_id == []: #check when voter list is completed
        print("Votin session is ended!!")
        if nm1_votes >nm2_votes or nm1_votes > nm3_votes:
            percent = (nm1_votes / no_of_voter)*100
            print(nominee1,"has won th election",percent,"%")
            break

        elif nm2_votes >nm3_votes or nm2_votes > nm1_votes:
            percent = (nm2_votes / no_of_voter)*100
            print(nominee2,"has won th election",percent,"%")
            break

        elif nm3_votes >nm1_votes or nm3_votes > nm2_votes:
            percent = (nm3_votes / no_of_voter)*100
            print(nominee3,"has won th election",percent,"%")
            break
        else:
            print("Ther is no winner , all have got the same numb of votes...!!")
            print("Now, the current Government will decide the winner")


    voter = int(input("Enter your Voter Id: "))
    if voter in voter_id:
        print("You are a voter")
        voter_id.remove(voter) # remove that specific id so it can try to vote again.
        print("-----------------------------------")
        print("To give vote to ",nominee1,"Press 1")
        print("To give vote to ",nominee2,"Press 2")
        print("To give vote to ",nominee3,"Press 3")
        print("-----------------------------------")
        vote = int(input("Enter your precious vote: "))

        if vote ==1:
            nm1_votes +=1
            print(nominee1,"Thanks for voting")
            print("We respect your vote... ")
            print("thnaks for chosing", nominee1)
        
        elif vote == 2:
             nm2_votes +=1
             print(nominee2,"Thanks for voting")
             print("We respect your vote... ")
             print("thanks for chosing", nominee2)
        
        elif vote == 3:
             nm3_votes +=1
             print(nominee3,"Thanks for voting")
             print("We respect your vote... ")
             print("thnaks for chosing", nominee3)
        
        elif vote > 3 :
            print("Check your passkey !!")
        
        else:
            print("You are not a Voter Or you have already voted...!!")
           