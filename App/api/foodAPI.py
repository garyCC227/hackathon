import request, json, urllib3

HEADER = {
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "56d77e19b7mshca1482175a5bf43p15b63djsn0ca1fbbea757"
}

class Food:
    def __init__(self, apiKey = None):
        self.apiKey_ = apiKey
        self.http_ = urllib3.PoolManager()

    
    """Generate Meal
        :param: timeFrame=(str: day, week) targetCalories=(int: >1500) diet=(str: "vegetarian", "vegan", "paleo", "carnism"
        :type return: json{meal:image, serving etc, nutrient}  
    """
    def generate_meal(self, timeFrame='day', targetCalories=2000, diet=None, exclude=""):
        r = json.loads(self.http_.request(
            'GET',
            "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate",
            fields={'timeFrame': timeFrame,
                    'targetCalories': targetCalories,
                    'diet': diet,
                    'exclude': exclude,
                    },
            headers=HEADER,
        ).data.decode('utf-8'))
        return r
    
    """Generate Meal
        :param: type=(str: breakfast, soup, main course) 
        :type return: json{meal:image, serving etc, nutrient}  
    """
    def get_video(self, query=None, type=None, cuisine="Italian", excludeingredients="mustard", \
                  includeingredients="chicken", maxLength=5, number=2):
        if query == None:
            return "need search keyword"
        r = json.loads(self.http_.request(
            'GET',
            "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/videos/search",
            fields={'query': query,
                    'type': type,
                    'cuisine': cuisine,
                    'excludeingredients': excludeingredients,
                    'includeingredients': includeingredients,
                    'maxLength': maxLength,
                    'number': number,
                    },
            headers=HEADER,
        ).data.decode('utf-8'))
        return r
    
    """ abstarct method of getting information by id 
    """
    def get_url(self, url):
        r = json.loads(self.http_.request(
            'GET',
            "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/" + url,
            headers=HEADER
        ).data.decode('utf-8'))
        if 'status' in r:
            return "invalid ID"
        else:
            return r
        
    """Get recipe description 
        :recipeID: recipeID: int
        :type return: dict{videos: }  
    """
    def summarize_recipe(self, recipeID):
        return self.get_url("{}/summary".format(recipeID))
        
    """parse recipe nutrition
        :recipeID: recipeID: int
        :type return: dict{basic nutrition: str, good: list, bad:list }  
    """
    def parse_recipe_nutrition(self, recipeID):
        return self.get_url("{}/nutritionWidget.json".format(recipeID))
    
    """get similar recipe list
        :recipeID: recipeID: int
        :type return: list{recipe: dict}  
    """
    def get_similar_recipe(self, recipeID):
        return self.get_url("{}/similar".format(recipeID))
    
    """get recipe infor
        :recipeID: recipeID: int
        :type return: list{vegan, glutenFree: bool, price: float, src: url}  
    """
    def get_recipe_info(self, recipeID):
        return self.get_url("{}/information".format(recipeID))

    """ price breakdown
        :recipeID: recipeID: int
        :type return: list{ingredients: list of idct, totalCOst: float, totalCostperSer: float}  
    """
    def get_price(self, recipeID):
        return self.get_url("{}/priceBreakdownWidget.json".format(recipeID))

    """ butrition
        :recipeID: recipeID: int
        :type return: list{general nutrition: str, good: list, bad: list}  
    """
    def get_nutrition(self, recipeID):
        return self.get_url("{}/nutritionWidget.json".format(recipeID))
        
    # get recepe instruction() with get recepe vedeio()


if __name__ == '__main__':
    Api = "56d77e19b7mshca1482175a5bf43p15b63djsn0ca1fbbea757"
    f = Food(Api)
    # result = f.generate_meal()
    zzz = f.get_nutrition(1003464)
    video = f.get_video()

'''
"vegetarian":false
"vegan":false
"glutenFree":true
"dairyFree":true
"veryHealthy":false
"cheap":false
"veryPopular":false
"sustainable":false
'''

