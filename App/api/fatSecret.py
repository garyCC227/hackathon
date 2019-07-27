# from fatsecret import Fatsecret
from rauth.service import OAuth1Service
import datetime
from rauth.service import OAuth1Service
from tmp import Fatsecret

# Be sure to add your own keys
consumer_key = '0b43941f5bc54a29bffd21c493b18b54'
consumer_secret = 'abbfea79f7894a2a9b901cefebe984de'

class Fatsecret:
    def __init__(self, consumer_key, consumer_secret, session_token=None):
        """ Create unauthorized session or open existing authorized session
        :param consumer_key: App API Key. Register at http://platform.fatsecret.com/api/
        :type consumer_key: str
        :param consumer_secret: Secret app API key
        :type consumer_secret: str
        :param session_token: Access Token / Access Secret pair from existing authorized session
        :type session_token: tuple
        """

        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

        # Needed for new access. Generated by running get_authorize_url()
        self.request_token = None
        self.request_token_secret = None

        # Required for accessing user info. Generated by running authenticate()
        self.access_token = None
        self.access_token_secret = None

        self.oauth = OAuth1Service(
            name='fatsecret',
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            request_token_url='http://www.fatsecret.com/oauth/request_token',
            access_token_url='http://www.fatsecret.com/oauth/access_token',
            authorize_url='http://www.fatsecret.com/oauth/authorize',
            base_url='http://platform.fatsecret.com/rest/server.api')

        # Open prior session or default to unauthorized session
        if session_token:
            self.access_token = session_token[0]
            self.access_token_secret = session_token[1]
            self.session = self.oauth.get_session(token=session_token)
        else:
            # Default to unauthorized session
            self.session = self.oauth.get_session()


if __name__ == '__main__':

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