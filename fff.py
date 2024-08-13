def dis(r):

  print (f"{r[1]}|{r[2]}|{r[3]}")

  print ("-----")

  print (f"{r[4]}|{r[5]}|{r[6]}")

  print ("-----")

  print (f"{r[7]}|{r[8]}|{r[9]}")



def imp(y):

  x=int(y)

  impt=input(f"Player{x} x or o  un can chonese anything but it will afect the graphics")

  return impt



def check():

  impt=input("u ready p? y or n")

  return (impt!="y")

def play(semn,r):

  impt=input("chose a space")

  if impt.isdigit():

    impt=int(impt)

    if r[impt]!=" ":

      print("is taken chose somthing else ")

      return(play(semn,r))

    else:

        r[impt]=semn

        return(r)

  else:

    print("a number from 1 to 9 ")

    return(play(semn,r))

def win(r):

   if (r[1]==r[2]==r[3]!=" "):

     return(True,r[1])

   elif(r[4]==r[5]==r[6]!=" "):

     return(True,r[4])

   elif(r[7]==r[8]==r[9]!=" "):

     return(True,r[7])

   elif(r[1]==r[4]==r[7]!=" "):

     return(True,r[1])

   elif(r[2]==r[5]==r[8]!=" "):

    return(True,r[2])

   elif(r[3]==r[6]==r[9]!=" "):

    return(True,r[3])

   elif(r[1]==r[5]==r[9]!=" "):

    return(True,r[1])

   elif(r[3]==r[5]==r[7]!=" "):

    return(True,r[3])

   else:

    return(False)

w=False

d=[" "," "," "," "," "," "," "," "," "," "]

semn1=imp(1)

semn2=imp(2)

player=1

counter=9

while counter>0:

  if player==1:

    semn=semn1

    player=2

  else:

    semn=semn2

    player=1

  counter-=1

  dis(d)

  d=play(semn,d)

  w=win(d)

  if w:

    dis(d)

    print(f"{semn} won")

    break