#boksac a
#boksac b
#nerijeseno n
#ako ni jedan nije dobio dva glasa onda je pobjednik onaj za koga glasa glavni sudac
#ako glavni sudac kaze da je nerijeseno onda je nerijeseno!

z1 = input()
z2 = input()
z3 = input()
g = int(input())

votes = [z1, z2, z3]
count_A = votes.count("A")
count_B = votes.count("B")

if count_A >= 2:
    print("A")
elif count_B >= 2:
    print("B")
else:
    main_vote = votes[g - 1]
    print(main_vote)