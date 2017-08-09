# this sets your path correctly so the imports work
import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))

from api import QuorumAPI
import json

# this library will let us turn dictionaries into csv files
import csv

# first, we subclass the QuorumAPI to support wordclouds.
# to do this, we'll use the same approach as the count function
# in order to make the final API request have &word_cloud=true
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
        
        ### TODO #2
        # 1. Check out python's 'with...as' syntax
        # 2. Check out writer(), writerow() methods
        with open(file_name, 'w') as f:
            w = csv.writer(f, delimiter=',')
            w.writerow(('state', 'num'))
            for i in item_list:
                w.writerow((STATES[i['state'].upper()], i['value']))

    def get_word_mentions_per_state(self, search_term):
        """
        get the number of documents that the given word is mentioned in each state.
        Write this to the data.csv file that will then be used
        """

        ### TODO #1
        # 1. Check out api.py
        quorum_api = self.quorum_api.set_endpoint("document") \
                                    .map(True) \
                                    .filter(advanced_search=search_term)
        results = quorum_api.GET()
        self.save_state_csv(results, 'data.csv')


# After you are done with implementing the methods above, initialize a map visualizer!
### TODO #3
cv = MapVisualizer()

# Then, pass in the search term that you are interested in to the method, run it, 
# and go back to localhost:8000. Is the map what you expected it to be?
### TODO #4
cv.get_word_mentions_per_state(search_term = "women AND STEM")
