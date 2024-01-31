#this is jungle game!
Animal_list=["elephant","lion","monkey"]#this list is in the power order

print("in this game you should choose a animal whit your own opinion")
print("the anima names are: elephant,lion,monkey")

p_1=input("p_1,pleas choose your animal: ")
p_2=input("p_2,pleas choose your animal: ")

p_1_score=0
p_2_score=0

again="nothing"

while again != "no":
    while p_1 not in Animal_list:
        p_1=input("p_1,pleas enter you Animal again: ")
    while p_2 not in Animal_list:
        p_2=input("p_2,pleas enter you Animal again: ")
    while p_1 == p_2:
        print("nobody win this round!")
    if p_1 == "elephant" and p_2 == "lion":
        p_1_score+=1
        print("p_1 is the winner of this round!")
        print(f"p_1={p_1_score}-p_2={p_2_score}")
    elif p_1 == "elephant" and p_2 == "monkey":
        p_1_score+=1
        print("p_1 is the winner of this round!")
        print(f"p_1={p_1_score}-p_2={p_2_score}")
    elif p_1 == "lion" and p_2 == "elephant":
        p_2_score+=1
        print("p_2 is the winner of this round!")
        print(f"p_1={p_1_score}-p_2={p_2_score}")
    elif p_1 == "monkey" and p_2 == "elephant":
        p_2_score+=1
        print("p_2 is the winner of this round!")
        print(f"p_1={p_1_score}-p_2={p_2_score}")
    elif p_1 == "lion" and p_2 == "monkey":
        p_1_score+=1
        print("p_1 is the winner of this round!")
        print(f"p_1={p_1_score}-p_2={p_2_score}")
    elif p_1 == "monkey" and p_2 == "lion":
        p_2_score+=1
        print("p_2 is the winner of this round!")
        print(f"p_1={p_1_score}-p_2={p_2_score}")
    again=input("do you want to play again? ")
