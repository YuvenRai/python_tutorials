pet_daily_food_consumption=int(input("How many cups of pet food does your pet eat in one day? "))
pet_food_available=int(input("How many cups of pet food do you have right now? "))
pet_food_needed_for_week = pet_daily_food_consumption * 7

if pet_food_available >= pet_food_needed_for_week:
    print("\n🎉 Yay! You have enough food for the week!")
else:
    additional_food_needed = pet_food_needed_for_week - pet_food_available
    print(f"\n😟 You need {additional_food_needed} more cups of food to last the week.")




















'''
🐍 Problem Name: Pet Feeding Time



🎯 Goal:

Write a Python program that helps figure out if you have enough pet food for the week.


📖 Story:

You are taking care of your pet (dog, cat, or any animal you choose). Your pet eats a certain amount of food each day. You have a bag of pet food at home. The program will help you figure out:


If you have enough food to last 7 days.

If not, how much more you need to buy.


📋 Requirements:


Ask the player:


“How much food (in cups) does your pet eat in one day?”

“How much food (in cups) do you have right now?”

Calculate:


Food needed for a week = daily amount × 7

Compare it to what you have.

If you have enough food, display:

Yay! You have enough food for the week.



If you do not have enough food, display:

You need X more cups of food.

(Replace X with the actual amount.)
'''