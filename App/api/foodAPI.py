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
        :return: json{meal:image, serving etc, nutrient}  
    """
    def get_video_id(self, query=None, number=1):
        if query == None:
            return "need search keyword"
        
        r = json.loads(self.http_.request(
            'GET',
            "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/videos/search",
            fields={'query': query,
                    'number': number,
                    },
            headers=HEADER,
        ).data.decode('utf-8'))
        print(r["videos"][0]["youTubeId"])
        return r["videos"][0]["youTubeId"]

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
        :type return: dict{: }  
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
    """ generate information for recipe card includes img and descrition
        :recipeID: recipeID: int
        :type return: list{general nutrition: str, good: list, bad: list}  
    """
    def generate_recipe_card(self):
        result = self.generate_meal()["meals"]
        # add descriptoin and change image 
        for recipe in result:
            id = recipe["id"]
            recipe["description"] = self.summarize_recipe(id)["summary"]
            recipe["image"] = "https://spoonacular.com/recipeImages/{}-312x150.jpg".format(id)
            
        return result

    def visualize_ingredient(self, recipeID):
        r = self.http_.request(
            'GET',
            "https://api.spoonacular.com/recipes/{}/ingredientWidget".format(recipeID),
            fields={'defaultCss': "true",
                    },
            headers={
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "56d77e19b7mshca1482175a5bf43p15b63djsn0ca1fbbea757",
                "Accept": "text/html"
            }
        ).data.decode('utf-8')

        return r
    
    def visualize_equipment(self, recipeID):
        r = self.http_.request(
            'GET',
            "https://api.spoonacular.com/recipes/{}/equipmentWidget".format(recipeID),
            fields={'defaultCss': "true",
                    },
            headers={
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "56d77e19b7mshca1482175a5bf43p15b63djsn0ca1fbbea757",
                "Accept": "text/html"
            }
        ).data.decode('utf-8')

        return r
    
    def visualize_nutrition(self, recipeID):
        r = self.http_.request(
            'GET',
            "https://api.spoonacular.com/recipes/{}/nutritionWidget".format(recipeID),
            fields={'defaultCss': "true",
                    },
            headers={
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "56d77e19b7mshca1482175a5bf43p15b63djsn0ca1fbbea757",
                "Accept": "text/html"
            }
        ).data.decode('utf-8')

        return r
    
if __name__ == '__main__':
    Api = "56d77e19b7mshca1482175a5bf43p15b63djsn0ca1fbbea757"
    f = Food(Api)
    # result = f.get_video_id("Breakfast Porridge")
    # add descriptoin and change image 
    #result = f.generate_recipe_card()
    zzz = f.get_recipe_info(636588)
    # print(zzz)
    #video = f.get_video()


    '''
    "vegetarian":false
    "vegan":false
    "glutenFree":true
    "dairyFree":true
    "veryHealthy":false
    '''

