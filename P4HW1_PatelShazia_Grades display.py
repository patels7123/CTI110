# Shazia Patel
# 7/11/2024
# P4LAB2
# Ask for number of scores user want to enter

score_num = int(input("How many scores do you want to enter? "))
        
print()
#create empty list

scores = []
# enters scores into the list
# for num in range(0, score_num):
for num in range(1, score_num + 1):
    # collect scores
    score = float(input("Enter score #" + str(num) + ": "))
    # score = float(input("Enter score #" + str(num + 1) + ": "))
    # validate entry
    while score < 0 or score > 100:
        print("\nINVALID score entered!!!")
        print("Score must be between 0 and 100!")
        score = float(input("Enter score #" + str(num) + ": "))
    scores.append(score)

# print(scores)


#find lowest score
 
lowest = min(scores)
scores_modified = scores

#drop lowest score from new list

scores_modified.remove(lowest)

# calculate average

avg = sum(scores_modified)/ len(scores_modified)

# determine letter grade for average

if avg >= 90:

    grade = "A"
elif avg >= 80:

    grade = "B"

elif avg >= 70:

    grade = "C"
elif avg >= 60:

    grade = "D"
else:

    grade = "F"

# display results

print("\n--------------Results-----------")
print("Lowest Score  : {}".format(lowest))
print("Modified List : {}".format(scores_modified))
print("Scores Average: {:.2f}".format(avg))
print("Grade         : {}".format(grade))
print("----------------------------------")







