"""
Sonora Tilton
IS 303- A03

Survey Result Sorter- processes survey responses and produces a summary report

Inputs:
- survey name- one time
- name of resondant
- rating out of 10 (int) (validation?)

processes:
- validate input for rating
- average rating- accumulated rating first to get average
- min/max rating
- count by category (0-3 = bad, 4-7 = mid, 8-10 = good)

output:
- f string with survey name, average rating, highest and lowest ratings,
and the count by category to present to the user

"""

survey_name = input("What is the name of your survey? ")

responses = []
add_result = "yes"
while add_result == "yes":
    respondant_name = input("What is the name of the respondant? ").title()
    rating = int(input("What did they rate it out of 10? "))
    if rating < 1 or rating > 10:
        print("Please enter a whole number from 1-10.")
        break
    responses.append({"name": respondant_name, "score": rating})
    add_result = input("Would you like to add another response? yes/no ").lower()

#accumulated rating
total_score = 0
for response in responses:
    total_score += response["score"]
#average rating
average_score = total_score / len(responses)

#max rating
top_score = responses[0]
for response in responses:
    if response["score"] > top_score["score"]:
        top_score = response

#min rating
lowest_score = responses[0]
for response in responses:
    if response ["score"] < lowest_score["score"]:
        lowest_score = response

#count by category if/elif/else inside for loop
bad_score = 0
mid_score = 0
good_score = 0
for response in responses:
    if response["score"] < 4:
        bad_score += 1
    elif response["score"] < 8:
        mid_score += 1
    else:
        good_score += 1

print(f"The {survey_name} survey has an average rating of {average_score}. The max rating is {top_score["score"]}\n and the lowest rating is {lowest_score["score"]}. There were {good_score} good ratings, {bad_score} bad ratings, and {mid_score} ratings in between.")
