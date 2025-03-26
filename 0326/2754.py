score=input()

if score[0]== "A":
    score_i=4
elif score[0] == "B":
    score_i=3
elif score[0] == "C":
    score_i = 2
elif score[0] == "D":
    score_i=1
else:
    score_i=0

if score[-1] == "+":
    score_i+=0.3
elif score[-1] == "-":
    score_i-=0.3

print("{:.1f}".format(score_i))