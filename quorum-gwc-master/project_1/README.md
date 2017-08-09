# Choropleth Project
In this project you are going to generate a map with each state colored by the number of times a given word or phrase has been mentioned in Congress.

##Overall Process
1. Use our state API and person API to figure out which Members represent which states.
2. Use our document API to find the number of documents from Members representing a given state that mention a particular word or phrase.
3. Combine your results into a CSV.
4. Visualize that CSV through a choropleth visualization you'll run on your local server on your computer.

## How to Run Your Localserver
1. Run `python -m SimpleHTTPServer`
2. Go to `localhost:8000` in your local browser
3. Rejoice!