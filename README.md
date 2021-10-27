<h1> Intermediate Plus Projects from the 100 Days of Code Python Pro Bootcamp </h1>
<h2> Day 32: Birthday Wisher Project </h2>
This project automates a "Happy Birthday" email to friends and family on their birthdays. Completed the project using what I've learned about email SMTP, datetime, pandas, working with csv files and reading text files. 

<h2> Day 33: ISS Overhead Notifier Project </h2>
Learning about APIs to build an ISS (International Space Station) tracker that emails me when the ISS is above my current location and it is night time.

<h2> Day 34: GUI Quiz App </h2>
This project involved building a class based Tkinter UI and reviewing OOP concepts to make a GUI quiz app. Questions for the Quizzler app were taken from the Open Trivia Database using the API. 

<h2> Day 35: Rain Alert App </h2>
Learned about API keys, authentication, environment variables and sending SMS using Python. Built an rain alert app that messages you in the morning, telling you to bring an umbrella if it's going to rain.

<h2> Day 36: Stock Trading News Alert Project </h2>
A Python program to help you trade stocks. It uses an API to get stock price data and calculates the percent increase/decrease in the value of the stock. If there's over 5% increase/decrease, the program will message us information about the fluctuation and send the first three recent news articles about the company (using an news API). I completed the hard level version of this project.

<h2> Day 37: Habit Tracker Project </h2>
Learned about advanced authentication and making POST/PUT/DELETE requests using the requests module. I used Pixela to build a habit tracker which displays the varying degrees of intensity to which I commmitted to the habit that day (i.e. coding for 30 mins).

<h2> Day 38: Exercise Tracking Application </h2>
Built a workout tracking application using google sheets and natural language processing (via Nutritionix API). This project helped review what I learned about APIs and making POST requests, authorization headers, and environment variables.

<h2> Day 39: Capstone Part 1: Flight Deal Finder & Day 40: Capstone Part 2: Flight Club</h2>

Part 1: This program finds flight deals for us to save $$ on our next trip. Google sheets tracks the locations we want to visit and the price cutoff (historical low price). We feed this location and price data into an flight search API which searches through all the locations, looking for the cheapest flight in the next 6 months. When it finds a flight deal, it sends the flight date and price via Twilio SMS module to our phone. Then, we can book it right away.

Part 2: This project turned into a product that let users sign up to use our service. We send users an email notifying them of the best flight deals.

<h2> Day 41-43: Web Foundation HTML/CSS </h2>
Building a personal CV website using HTML and CSS. 

<h2> Day 44: Web Foundation [Skipped Project] </h2>
I watched the lectures on intermediate CSS for Day 45 but opted out of the project since I'm already practicing my HTML/CSS skills through <a href="https://www.frontendmentor.io/profile/rachanahegde">Frontend Mentor</a>.

<h2> Day 45: Web Scraping with Beautiful Soup </h2>
This project involved using beautiful soup for web scraping in order to compile a list of the 100 greatest movies to watch. 

<h2> Day 46: Create a Spotify Playlist using the Musical Time Machine </h2>
I used Python code to create a Spotify playlist of the top 100 songs that were playing on a particular date. To accomplish this, I used Beautiful Soup to scrape the Billboard Hot 100 songs from a certain date and the Spotify API to create a new playlist made up of those songs.

<h2> Day 47: Amazon Price Tracker Project </h2>
The program alerts me with an email when the Amazon product price drops below my target price. I used BeautifulSoup to scrape the product price from the Amazon web page then compared this price to the target amount and set up the email alert with smtplib.

<h2> Day 48: Cookie Clicker Project (Automated Game Playing Bot) </h2>
I used Selenium to build a bot that automatically clicks on the cookie in the Cookie Clicker game and purchases upgrades at timed intervals. The goal is max out the cookies per second after playing the game for 5 minutes. I learned a lot from this project regarding error handling and how to use try and except to ensure that the program continues to run (and click cookies!). I also became more familiar with the time module which I used to limit the duration of the while loop to 5 minutes and time the intervals at which the bot purchases upgrades. Reading the Selenium documentation helped me use explicit waits and expected conditions to address potential errors when attempting to access or click elements. (I managed to get 107.8 cookies/second with my algorithm - higher than Angela's score but not one that I could get consistently - and I decided to stop tweaking after spending 10 hours on the project!) 

<h2> Day 49: Automated Job Application Bot with Selenium </h2>
This project involved using selenium webdriver to open LinkedIn, log in, and apply for all jobs that meet my criteria (including Easy Apply). While this is an interesting strategy for automating the job application process on LinkedIn, coding the app bot proved to be far more complicated than I anticipated. Selenium threw up exceptions and errors at nearly every step of the process. I implemented WebdriverWait and expected conditions as well as try and except statements to catch the most common errors, NoSuchElementException and ElementClickInterceptedException. I also used the sleep function throughout the program to give the page time to load or ensure LinkedIn didn't think I was a bot. I also tried the variation of the project that involves saving the job and following the company instead of submitting an application (the code is at the bottom of the main.py file).

<h2> Day 50: Auto Tinder Bot </h2>
I attempted to use selenium to build an auto-swiping tinder bot. Unfortunately, this project was unsuccessful since LinkedIn continued to demand verification via phone and email and/or some kind of CAPTCHA puzzle. This made it impossible to automate the login process and I couldn't find a workable solution to these security measures. (I uploaded the code I wrote up to this point.)

<h2> Day 51: Internet Speed Twitter Complaint Bot </h2>
This project uses Selenium to automatically check your internet speed before tweeting at your service provider to ask why it's lower than their guaranteed download and upload speed. This project also enabled me to review my OOP skills by creating an InternetSpeedTwitterBot class with two methods, get_internet_speed and tweet_at_provider. 

<h2> Day 52: Instagram Follower Bot </h2>
I built a follower bot that will help build my Instagram brand by following users who follow accounts that post similar content as me. Ideally, this will get the attention of those users who could potential follow me back. This bot does, however, get restricted by Instagram after following a certain number of users (even with the sleep function slowing down the button clicking to imitate a human).

<h2> Day 53: Web Scraping Capstone - Data Entry Job Automation </h2>
I researched house prices that fit a certain criteria for a client on the Zillow website and then transferred that data into a Google form. I used the form to create a spreedsheet in Google sheets. Essentially, I automated an data entry job using everything I learned about web scraping so far with Selenium. 

The project actually required me to use BeautifulSoup to scrape the Zillow website but I was unable to do so since the entire page's listings wouldn't load. Instead, I used Selenium and various keys to scroll through all the listings. This enabled me to access the prices, addresses, and links for each listing. Unfortunately, the results of the web scraping were inconsistent - sometimes, I was able to collect the data for all 40 listings and at other times, the first nine loaded before the program crashed with NoSuchElementException errors. In the courses's comments, other students mentioned encountering similar issues and that the website's front end code had changed since Angela developed this course. Zillow also discourages bots by requiring CAPTCHA after the program accesses it multiple times so after I successfully scraped the data I needed, I hardcoded the results as lists. I, then, looped through those lists in order to automatically fill out the Google form.

<h2> Day 54: Introduction to Web Development with Flask </h2>
This set of lectures covered backend web development, the command line, Python decorator functions and using Flask for web development. 

<h2> Day 55: HTML & URL Parsing in Flask and the Higher Lower Game</h2>
Today's lectures covered rendering and parsing HTML in Flask and advanced decorators in order to build a 'Guess the Number' website. The user types the number into the URL after the forward slash and they find out if their guess is too high, too low, or correct! 
