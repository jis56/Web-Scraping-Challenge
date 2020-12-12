## Web-Scraping-Challenge

A web application was built that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following steps were completed:

# Step 1: Scraping
Jupyter Notebook, BeautifulSoup, Pandas, and Splinter were used for scraping and analysis in mission_to_mars.ipynb. The following was scraped:
  - The latest news title and paragraph text from NASA Mars News (https://mars.nasa.gov/news/)
  - A featured space image jpg from JPL (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
  - Mars facts table that was converted into HTML table string (https://space-facts.com/mars/)
  - Titles and full resolution images from each of Mars' four hemispheres, which was appended into a dictionary (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
  
# Step 2: MongoDB and Flask App

MongoDB and Flask templating were used to create an HTML page that displays all the information scraped from the URLs above. The Jupyter Notebook above was converted into scrape_mars.py Python script, an index.html file was created to display all the data in appropriate HTML elements, and ap.py "/" and /"scrape" routes were created.
