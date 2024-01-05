# WHERE2FLY2
#### Context:
I build this project in December 2022 as a final step of CS50 course from Harvard X. It was a 11-weeks online course introducing to computer science and programming. The focus was not on html and css which explains the basic design of the web application.
#### Video Demo:  https://youtu.be/jr1GXIpdPq4
#### Description:
The project is a web application for people planning their holidays. The goal is to help undecided travelers to find their next destination. It is always a challenge to decide where we want to go for the next holiday and the bigger the family, the longer the discussions.
The website helps users in two ways:
1. A page where users choose 4 criteria describing how they imagine their next vacations. Once they submit the form, the app searches in the database and returns (hopefully) a list of countries that match the user's criteria. Let's see that as suggestions. If the search is unsuccessful, use is informed.
2. There are other tools that might help users to finalize their decision if they already have a few destinations in mind, for example after doing the search. That includes a page where the user chooses a country from the ones in the database. Then it returns a list of useful information about the selected country such as population, languages spoken, local currency, time zone, cost of living, places to see, map ... There is another page that works in a similar way and displays information about the weather in the selected country. It consists of 3 tables showing monthly data on air temperature, number of daily hours of sunshine and sea surface temperature. Last tool shows the cost of living in the countries to give an idea of how expensive it will be on site.

### Languages used:
Html, CSS, Jinja, JavaScript, SQL, Python, Flask

### Files:
- travel.db is a database containing 7 tables covering 45 countries.
- all csv files used to build the database are stored in the /csv folder.
- app.py contains the routes that the Web app needs to work as well as db.execute queries: queries to search and suggest destinations to the user, queries to get information about weather and country details, query listing Cost of Living index per country and routes to homepage, sources and pages displaying errors messages (in case of wrong input or unsuccessful search).
- html files are stored in the /templates folder. They are built using layouts with Jinja (layout.html). Bootstrap and W3 Schools provided very useful tools. Some of the pages are "static" (error.html, index.html, search_no_results.html, sources.html), the others are dynamic using a form to request user's input (countries.html, search.html, weather.html) or using app.py to provide data from travel.db requested by user (countries_result.html, search_results.html, weather_results.html).
- Files used for the design of the site are stored in the /static/img folder: flags, icons, pictures, maps. The sources are listed in sources.html.
- styles.css is the CSS file used for the website.

### Steps to build the project:
Here are the steps I took to build the web app:
1. Create the database in Google sheets and build in SQL.
2. Create a rough structure for the website so that I can check if the code is working
3. Write the codes in app.py
4. Finalize the design of the website
5. Review, corrections

Database was created in Google sheet file either by directly downloading dataset from the internet and arranging data (sources are listed in sources.html) or by manually entering information. I then exported the files in csv format. I uploaded the tables in the project folder and imported them into travel.db by typing in the terminal the commands ".mode csv" then for example ".import temperatures.csv temperatures" in sqlite3. The table structures were beforehand created in phpLiteAdmin. I also used this interface to manage the database when I needed to amend the table. This is the part where I "debated" the most with myself. I had to merge tables, redesign them in order to optimize the query. I ended up with less tables than I had initially planned.
I also hesitated to build the menu. At first I used a nav bar on the top then I went for a dropdown menu because it took up more space on the screen which was better from a user's experience perspective. I applied a similar logic also when choosing the background of the website. I wanted a picture of a plane but I soon realized that it was distracting for the user, so I replaced it with a colored background.