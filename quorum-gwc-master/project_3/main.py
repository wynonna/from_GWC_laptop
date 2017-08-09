# this sets your path correctly so the imports work
import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))

from api import QuorumAPI
import json
# this library will let us turn dictionaries into csv files
import csv

# A dict of states with its abbreviations and its full name
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

# first, we subclass the QuorumAPI to support wordclouds.
# to do this, we'll use the same approach as the count function
# in order to make the final API request have &word_cloud=true
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
    # state, num
    # Alabama,9
    # Alaska, 5
    # ...
    # California, 18
    # ...etc.
    def save_state_csv(self, item_list, file_name):
        """
        ### TODO ###
        Use the CSV class as imported above to write the key-value pairs into a
        csv file! Don't forget to first include the headers, i.e. state and num!
        Hint: we want to use python's 'with...as' syntax because it is a safe
        way to open and write files.
        """


    def get_word_mentions_per_state(self, search_term):
        """
        ### TODO ###
        Get the total number of sponsors and cosponsors on bills in which the
        given word is mentioned in the bill.
        Hint: Take a look at the api.py file!
        """

        # First, let's set up the endpoint and filters!


        # Then, get the results from making a request!


        # Save the csv file as data.csv



cv = MapVisualizer()

cv.get_word_mentions_per_state(search_term = "healthcare")
