from fatsecret import Fatsecret

# Be sure to add your own keys
consumer_key = '0b43941f5bc54a29bffd21c493b18b54'
consumer_secret = 'abbfea79f7894a2a9b901cefebe984de'


fs = Fatsecret(consumer_key, consumer_secret)

# Test Calls w/o authentication

print("\n\n ---- No Authentication Required ---- \n\n")

# list of foods
foods = fs.foods_search(b"Tacos")
print("Food Search Results: {}".format(len(foods)))
print(type(foods))
# print("{}\n".format(foods))

food = fs.food_get('1345')
# print("Food Item 1345")
# print("{}\n".format(food))

recipes = fs.recipes_search("Tomato Soup")
# print("Recipe Search Results:")
# print("{}\n".format(recipes))

recipe = fs.recipe_get('88339')
# print("Recipe 88339")
# print("{}\n".format(recipe))

# Test Calls with 3 Legged Oauth



print("\n\n ------ User OAuth Example ------ \n\n")

# print(fs.get_authorize_url())
# session_token = fs.authenticate(input("\nPIN: "))

# foods = fs.foods_get_most_eaten()
# print("Most Eaten Food Results: {}".format(len(foods)))

# recipes = fs.recipes_search("Enchiladas")
# print("Recipe Search Results: {}".format(len(recipes)))

# profile = fs.profile_get()
# print("Profile: {}".format(profile))
