candy_count = int(input("How many candies do you have?: "))
friend_count = int(input("How many kids are there? (Don't forget yourself!): "))
print("\n")

candies_per_person = candy_count / friend_count
leftover_candies = candy_count % friend_count


if leftover_candies == 0:
    print(f"Yay! Everyone got the same amount of candy! Each person gets {int(candies_per_person)} candies.")
else:
    print(f"Each person gets {int(candies_per_person)} candies.")
    print(f"There will be {leftover_candies} candies left over.")
    print("Hmm… there are some extra candies! Who gets them?")



'''
Problem Name: Candy Sharing Helper

🎯 Goal:

Write a Python program that helps figure out how to share candies equally with friends.


📖 Story:

You have a bag of candies. You and your friends want to share them fairly, so everyone gets the same number. The program will help you figure out:


How many candies each person gets.

How many candies will be left over.


📋 Requirements:


Ask the player:


“How many candies do you have?”

“How many friends are there?” (Don’t forget yourself!)

Calculate:


Candies per person = total candies ÷ number of people (integer division).

Leftover candies = candies that don’t fit equally (remainder).

Show results:

Each person gets X candies.
There will be Y candies left over.
If there are no leftovers, display:

Yay! Everyone got the same amount of candy!
If there are leftovers, display:

Hmm… there are some extra candies! Who gets them?

'''