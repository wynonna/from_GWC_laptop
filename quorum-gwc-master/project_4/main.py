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

#######################
#     MAKE A CSV      #
#######################

    # Let's write a helper function that takes in a list of (date, count)
    # key-value pair objects and produces a csv file of the following format:
    # label,date,count
    # my label,20170101,19
    # my label,20170201,5
    # ...etc.
    # We can use the csv class that we imported above.
    def save_state_csv(self, trend_label, item_list, file_name, append_date_to_end_of_file):
        # When we open the file, we have to tell python whether to clear
        # the data already in the file or to add to the end of file.

        # TODO: Specify file writing options so that it creates a new file.

        # TODO: Add option to append to existing file, if the user specifies it via the function arguments.

        # TODO: Open the file! We want to use python's 'with...as' syntax because
        # it is a safe way to open and write files.
        # Be sure that the first row of a new file are the category names.
        # Make sure you print every data point into the CSV.

#######################################
#       GET DATA HELPER FUNCTION      #
#######################################

    def get_topic_mentions_count(self, search_term, trend_label, make_multiple_queries=False, *args, **kwargs):
        """
        get the number of bills that mention the given word overtime.
        Write this to the data.csv file that will then be used
        """

        #TODO: use the QuorumAPI to down to the data you're looking for.
        #Be sure to set it so that it will show trends.

        #TODO: get the data set!

        #This converts the results into a dictionary.
        results = ast.literal_eval(results)

        #TODO: Convert the results into a CSV using save_state_csv.



trends = TrendlineVisualizer()

# Create a CSV given the search term!

# What about two trendlines? How about three?