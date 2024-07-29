# PROJECT TITLE:
**REDBUS Data Scraping with Selenium & Dynamic Filtering using STREAMLIT**

**Introduction:**

redBus is an Indian online bus ticket booking company that provides bus ticket booking through its website and iOS and Android mobile apps. It is headquartered in Bangalore and works like a hub, acting as a medium for a network of more than 3500 bus operators, across the countries of India, Malaysia, Indonesia, Singapore, Peru, and Colombia. It claims to have registered over 180 million trips, with a customer base of over 20 million. In 2018, the company achieved a GMV of ₹50 billion (equivalent to ₹67 billion or US$800 million in 2023), with a 70% share in the Indian online bus ticketing segment.

**Problem Statement:**

The "redBus Data Scraping and Filtering with STREAMLIT Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from redBus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

**Packages Used:**

- **Selenium:**

The selenium package is used to automate web browser interaction from Python.

To know more about **selenium**. Click here <https://selenium-python.readthedocs.io/>

- **Streamlit:**

  `                `Streamlit turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience required.

  `                `To know more about **Streamlit**. Click here <https://docs.streamlit.io/>

- **Pandas:**

  `            `Pandas is a powerful and open-source Python library. The Pandas library is used for data manipulation and analysis.

  `            `Pandas consist of data structures and functions to perform efficient operations on data.

  `            `To know more about **Pandas.** Click here [https://pandas.pydata.org/docs/                                ](https://pandas.pydata.org/docs/%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20) 

- **MySQL:**

  `              `MySQL, the most popular Open-Source SQL database management system, is developed, distributed, and supported by 

  `              `Oracle Corporation. 

  `               `To know more about **MySQL**. Click here <https://dev.mysql.com/doc/refman/9.0/en/>

- **Streamlit-Option-Menu:**
  
  `                                         `Streamlit-option-menu is a simple Streamlit component that allows users to select a single item from a

  `                                         `list of options in a menu.

  `                                         `To know more about Streamlit-Option-Menu. Click here [https://discuss.streamlit.io/t/streamlit-option-                                             menu-is-a-simple-streamlit-component-that-allows-users-to-select-a-single-item-from-a-list-of-options-in-a-menu/20514](https://discuss.streamlit.io/t/streamlit-option-%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20menu-is-a-simple-streamlit-component-that-allows-users-to-select-a-single-item-from-a-list-of-options-in-a-menu/20514)

**Install Packages:**

- **Selenium** – pip install selenium
- **Pandas** – pip install pandas
- **Streamlit** – pip install streamlit
- **MySQL** **Connector**– pip install mysql-connector-python
- **Streamlit-Option-Menu** – pip install streamlit-option-menu

**Code Flow Plan:**

This project contains two files

1) Redbus\_Main\_Code.py
1) Webapplication\_Redbus.py

**1) Redbus\_Main\_Code.py**

- The process begins with importing the necessary packages required for web scraping and database operations. 
- The next step involves opening the Redbus website and maximizing the browser window for better visibility. 
- The page is then scrolled down to locate the desired section, where the "ViewAll" button is pressed to display all available options. 
- The scraper then collects state names and their corresponding links, followed by gathering route names and links from the website. Subsequently, it extracts detailed bus information from all routes. 
- This data is logged into two CSV files: route\_data.csv and bus\_data.csv. 
- The workflow continues by establishing a connection between Python and a MySQL database, where any existing tables are dropped if they exist. 
- New tables for route and bus data are created, and the scraped data is inserted into these tables. 
- Finally, the connection to the database is closed to complete the process.

**2) Webapplication\_Redbus.py**

- The process starts with importing the required packages for database operations and web application development. 
- A connection between MySQL and Python is then established, followed by using the specific database intended for the application.
- Page configuration settings are applied to ensure the home page and the bus search page are correctly set up. 
- When a user presses the search button, the application fetches data from the database based on the filtered options provided. 
- The retrieved data is then displayed in a table format. Finally, the MySQL connection is closed to complete the workflow.

**How to use the application:**

- Go to Search Bus Option from the Main Menu
- State and Route Selection: Start by selecting the state you are traveling from. Then choose the specific route you are interested in.
- Seat Type: Use the dropdown to select your preferred type of seat. Whether it's a sleeper, semi-sleeper, or any other type, we have options for you.
- Price Range: Adjust the slider to set your budget. You can filter buses based on your preferred price range.
- Star Rating: Looking for a top-rated bus? Adjust the star rating filter to find buses with the highest ratings.
- Starting Time: Use the slider to choose the departure time that suits you best. Whether you prefer early morning departures or late-night buses.
- After selecting your preferences, simply click on the 'Search' button to view the available options. The results will display here, and you can further refine your choices as needed. 

**How to run the code:**

Initially run the “Redbus\_Main\_Code.py” using command “**python Redbus\_Main\_Code.py**” in terminal. Wait until it completely scraping the 10 bus routes data.

After finishing the scraping process run “Webapplication\_Redbus.py” using command “**streamlit run Webapplication\_Redbus.py**”









