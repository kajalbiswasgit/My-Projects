while True:
    favorite_foods = input("Please enter your favourite food(s), separated by commas: ")
    
    # Split input by commas and strip spaces
    food_list = [food.strip() for food in favorite_foods.split(",")]

    # Check if all entries are valid alphabetic words
    if all(food.replace(" ", "").isalpha() for food in food_list):
        print("✅ Your favourite food(s) are:", ", ".join(food_list))
        break
    else:
        print("❌ Please enter words only (no numbers or special characters).")
