# this sets your path correctly so the imports work
import sys
import os
sys.path.insert(1, os.path.dirname(os.getcwd()))

from api import QuorumAPI
import json
# this library will let us turn dictionaries into csv files
import csv
import ast


# first, we subclass the QuorumAPI to support trendlines.
# to do this, we'll use the same approach as the count function
# in order to make the final API request have &trends=true
class TrendlineAPI(QuorumAPI):

    def trends(self, return_trendline=False):
        if return_trendline in [True, False]:
            self.filters["trends"] = return_trendline
        else:
            raise Exception("Must be a Boolean value!")

        return self

class TrendlineVisualizer(object):

    # Since both the api_key and username stay the same so initialize API object once
    quorum_api = TrendlineAPI(username="gwc", api_key="691e43c415d88cd16286edb1f78abb2e348688da")

    # Let's write a helper function that takes in a list of (date, count)
    # key-value pair objects and produces a csv file of the following format:
    # label,date,count
    # my label,20170101,19
    # my label,20170201,5
    # ...etc.
    # We can use the csv class that we imported above.
    # You can see the documentation for csv here -> https://docs.python.org/3/library/csv.html
    def save_state_csv(self, trend_label, item_list, file_name, append_date_to_end_of_file):        
        # When we open the file, we have to tell python whether to clear
        # the data already in the file or to add it to the end of the file
        # You can use the options 'w' to write, 'a' to append, and 'r' to read
        if append_date_to_end_of_file:
            file_option = ???
        else:
            file_option = ???

        # open the file with our file option
        # We want to use python's 'with...as' syntax because
        # it is a safe way to open and write files.
        # Look at this documentation for help -> https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
        with open(...) as f:
            w = csv.writer(f, delimiter=',')
            w.writerow(('label', 'date', 'count'))
            ...
                
    def get_bills_mentioning_topic(self, search_term, trend_label, make_multiple_queries=False):
        """
        get the number of bills that mention the given word overtime.
        Write this to the data.csv file that will then be used
        """
        quorum_api = self.quorum_api.set_endpoint(???) \
                               .trends(True) \
                               .filter(advanced_search=search_term)
        # get the results from the api with the GET() function from quorum-gwc/api.py
        results = ...
        # after you get the results, you can use the `results = ast.literal_eval(results)` function
        # to make sure the list of items is in a readable format
        results = ...
        # now use your save_state_csv function to save your data into 'data.csv'
        self.save_state_csv(...)


trends = TrendlineVisualizer()
trends.get_bills_mentioning_topic(search_term = "men AND STEM", trend_label = "Men and STEM")
trends.get_bills_mentioning_topic(search_term = "women AND STEM", trend_label = "Women and STEM", make_multiple_queries=True)
