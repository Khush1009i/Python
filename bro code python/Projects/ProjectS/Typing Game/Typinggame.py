from time import time # to record time

# now to calculate accuracy of input prompt
def tperror(prompt):
    global inwords

    words = prompt.split()
    errors =0

    for i in range(len(inwords)):
        if i in (0,(len(inwords)-1)):
            
            if inwords[i] == words[i]:
                continue
            
            else:
                errors += 1
        
        else:
            if inwords[i] == words[i]:
                if(inwords[i+1] == words[i + 1]) & (inwords[i+1]== words[i-1]):
                  continue
                else:
                  errors += 1
    return errors
# to calculate speed typing per min:
def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords/ time

    return speed

# the total elapsed time
def elapsedtime(stime, etime):
    time = etime - stime # etime is end time & stime start time
    return time

if __name__ == '__main__':
    prompt = "Python is an intrepreted , high level, general-purpose programming language. Creted by Guido van Rossum & first released in 15"
    print("Type this :- ",prompt,'')
    #checking to i/p
    input("press Entr when you re ready to check your speed ")

    #recording time input for speed cehck
    stime = time()
    inprompt =input()
    etime = time()

    # collect all info returned by the function 
    time = round(elapsedtime(stime, etime),2) # roundd-off time
    speed = speed(inprompt, stime, etime)
    errors = tperror(prompt)

    # printing all data to see result:
    print("################################")
    print("Toatl time elapsed:", time, "sec")
    print("Your average:",speed,"words per min")
    print("with the total of", errors,"errors") 
    print("################################")