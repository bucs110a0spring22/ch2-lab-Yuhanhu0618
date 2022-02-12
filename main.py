import random

#Part A
weeks = 16
classes = 5
tuition = 6000
class_per_week = 2
cost_per_week = ((tuition / classes) / weeks)
cost_per_class = cost_per_week/class_per_week
print("Cost per week:", cost_per_week)
print("每节课花销:", cost_per_class)
print(class_per_week, type(class_per_week))
print(cost_per_class, type(cost_per_class))
print()

#Part B
food_choice_of_today = ["Korean fried chicken wings", "Mapo tofu", "Pasta", "Burger", "Tonkotsu ramen"]
dinner_today = random.choice(food_choice_of_today)
print(dinner_today)