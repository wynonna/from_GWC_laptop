# this sets your path correctly so the imports work
import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))

from api import QuorumAPI
import json

# this library will let us turn dictionaries into csv files
import csv

STATES = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

class MapAPI(QuorumAPI):

    def map(self, return_map=False):
        if return_map in [True, False]:
            self.filters["map"] = return_map
        else:
            raise Exception("Must be a Boolean value!")

        return self


class MapVisualizer(object):

    # Since both the api_key and username stay the same so initialize API object once
    quorum_api = MapAPI(username="gwc", api_key="691e43c415d88cd16286edb1f78abb2e348688da")

    # Let's write a helper function that takes in a dictionary of (state, number)
    # key-value pairs and produces a csv file of the following format:
    # state,num
    # Alabama,9
    # Alaska, 5
    # ...etc.
    # We can use the csv class that we imported above.
    def save_state_csv(self, item_list, file_name):
        # we want to use python's 'with...as' syntax because
        # it is a safe way to open and write files.
        with open(file_name, 'w') as f: # w instead of wb in python 3
            w = csv.writer(f, delimiter=',')
            w.writerow(('state', 'num'))
            for i in item_list:
                w.writerow((STATES[i['state'].upper()], i['value']))

    def get_female_legislators_per_state(self, search_term):
        """
        get the number of female legislators per state.
        Write this to the data.csv file that will then be used
        """

    # An enum is a data type consisting of a set of named values called elements or numbers. A color enum may include
    # blue, green, and red. 
    # class Gender(PublicEnum):
    #     male = enum.Item(
    #         1,
    #         'Male',
    #         slug="male",
    #         pronoun="he",
    #         pronoun_object="him",
    #         pronoun_possessive="his",
    #         honorific="Mr."
    #     )
    #     female = enum.Item(
    #         2,
    #         'Female',
    #         slug="female",
    #         pronoun="she",
    #         pronoun_object="her",
    #         pronoun_possessive="her",
    #         honorific="Ms."

        # How can we get the number of female legislators per state?
        quorum_api_females = self.quorum_api.set_endpoint("TODO") \
                               .map(True) \
                               .count(True) \
                               .filter(
                                    # TODO
                                    most_recent_person_type=1  # legislators
                                )

        # retrives the total females and assigns to dictionary                       
        total_females = quorum_api_females.GET()

        # Clears the API results before the next API call
        quorum_api_females.clear()

        # How can we get the total number of legislators per state? 
        # TODO

        # Retrive the total number of legislators per state and assign to dictionary

        # Clear the API results before next API call


        # Now let's find the proportion of women over total legislators per state!




        self.save_state_csv(TODO, 'data.csv')

# After you are done with implementing the code, initialize a map!
cv = MapVisualizer()

# And enter the search term that you are interested in, and go back to localhost:8000,
# is the map what you expected it to be?
cv.get_female_legislators_per_state()
