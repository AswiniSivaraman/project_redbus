# import required packages
import streamlit as st
from streamlit_option_menu import option_menu
import time
import mysql.connector as sconn
from mysql.connector import Error
import pandas as pd
import numpy as np

def timedelta_to_hhmm(value):
    #this function will convert the timedelta format into HH:MM
    t_seconds = value.seconds
    hours = t_seconds//3600  # 1hour = 3600 seconds
    minutes = (t_seconds%3600)//60 #1hour = 60minutes and 3600seconds
    return f"{hours:02}:{minutes:02}" #formatiing to display the time in 00:00 format

def configuration():
    # configure the sql connector 
    try:
        config = {
            "user":"root",
            "password":"Aa25@04@2002",
            "host":"localhost",
            "database":"project_redbus"
        }
        print("Configuration completed")
        return config
    
    except Error as e:
        print("Error occurred during configuration:",e)

def connection():
    # configure the connection between python and mysql
    try:
        config=configuration()
        if config is None:
            return None
        conn=sconn.connect(**config)

        if conn.is_connected():
            print("connection completed")
        return conn
    
    except Error as e:
        print("Error occurred when open connection:",e)

def use_database(conn,query_database):
    # this function will execute the use database query
    c=conn.cursor()
    try:
        c.execute(query_database)
        print("using the selected database")
    except Error as e:
        print("Error occured when select the use database",e)

def fetch_distinct_value(conn,query_distinct):
    # this function will fetch the distinct state name
    c=conn.cursor()
    try:
        c.execute(query_distinct)
        state_name = [state[0] for state in c.fetchall()]
        print("state name fetched from the table")
        return state_name
    except Error as e:
        print("Error occured when fetching distinct values",e)

def fetch_route_names(conn,query_routes_names):
    # this function will fetch the route names  
    c=conn.cursor()
    try:
        c.execute(query_routes_names)
        route_names= [route[0] for route in c.fetchall()]
        print("Route names got fetched")
        return route_names
    except Error as e:
        print("Error occurred when fetching route name based on state value")

def fetch_distinct_bustype(conn,query_distinct_bustype):
    c=conn.cursor()
    # this function will fetch the distinct bus type
    try:
        c.execute(query_distinct_bustype)
        seat_type = [seattype[0] for seattype in c.fetchall()]
        print("distinct bustypes fetched successfully")
        return seat_type
    except Error as e:
        print("Error occurred when fetching bustype",e)

def fetch_filtered_value(conn,query_filtered_value):
    # this function will fetch the value based on the filtering options
    c=conn.cursor()
    try:
        c.execute(query_filtered_value)
        column = [col[0] for col in c.description]
        filtered_value = c.fetchall()
        print(filtered_value)
        df = pd.DataFrame(filtered_value, columns=column, index=[index+1 for index in range (len(filtered_value))])
        if "departing_time" in df.columns:
            df["departing_time"] = df["departing_time"].apply(timedelta_to_hhmm)  #change the format of the delta format to HH:MM format
        if "reaching_time" in df.columns:
            df["reaching_time"] = df["reaching_time"].apply(timedelta_to_hhmm) #change the format of the delta format to HH:MM format
        if "star_rating" in df.columns:
            df['star_rating'] = df['star_rating'].replace(0.0, np.nan) #if star rating is not given change it as NA
        return df
    except Error as e: 
        print("Error occurred when fetching filtered value",e)
        return pd.DataFrame()
    
#this function will close the connection 
def close_connection(conn):
    try:
        conn.close()
        print("connection closed successfully")
    except Error as e:
        print('Error occurred when closing the connection: ',e)    

conn=connection()

# enable the database to use
use_database(conn,"use project_redbus;")

# setting the page configuration data
st.set_page_config(
    page_title="Redbus",
    page_icon=":oncoming_bus:",
    layout="wide",      #if wide full page will cover , centered means centre part of the page is covered
    initial_sidebar_state="auto"
    )

data="https://i.pinimg.com/564x/04/6b/38/046b3884bbd9d16ba053a80c95b8f295.jpg"  #bus image link

#sidebar styling 
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #FFFFFF;
        margin-right: 20px;
        border-right: 2px solid #FFFFFF
    }
</style>
""", unsafe_allow_html=True)

#options styling in sidebar and added image in sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=['Home','Search Bus'],
        icons=['house-door-fill','search'],
        menu_icon='truck-front-fill',
        default_index=0,
        styles={
            "container": {'padding':'5!important','background-color':'#FAF9F6'},
            "icon": {'color':"#000000", "font-size":"23px"},
            "nav-link": {'font-size':'16px','text-align':'left','margin':'0px','--hover-color':'#EDEADE','font-weight':'bold'},
            "nav-link-selector":{'background-color':'#E6E6FA','font-weight':'bold'}
        }
    )

    st.sidebar.image(data,use_column_width=False)

# if selected option is home means then add these in the page
if selected=="Home":
    st.title(":red[REDBUS] - Book Your Ride in Bus 🚌")
    
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    st.subheader("""Redbus is an online platform that facilates bus ticket booking services accross india and several other countries""")

    st.markdown("""Redbus is an online bus ticketing platform founded in 2006 in India. 
                It allows users to book bus tickets through its website and mobile app, 
                providing access to a wide network of bus operators across various routes. 
                Redbus offers additional services such as hotel bookings and car rentals, 
                aiming to provide a comprehensive travel solution. It operates in multiple 
                countries, including India, Malaysia, Indonesia, Singapore, Peru, and Colombia,
                and is part of the Ibibo Group, a subsidiary of MakeMyTrip Limited.""")

    with st.container():
        st.markdown("""
        <div class="container">
            <div style="display: flex; justify-content: space-around;">
                <figure>
                    <img src="https://upload.wikimedia.org/wikipedia/en/c/c4/Andhra_Pradesh_State_Road_Transport_Corporation_logo.png" width="150" height="150">
                    <figcaption>APSRTC</figcaption>
                </figure>
                <figure>
                    <img src="https://upload.wikimedia.org/wikipedia/en/e/ed/Uttar_Pradesh_State_Road_Transport_Corporation_logo.png" width="150" height="150">
                    <figcaption>UPSRTC</figcaption>
                </figure>
                <figure>
                    <img src="https://th-i.thgim.com/public/migration_catalog/article10538854.ece/alternates/FREE_1200/13hyskm06-TSRTChy14TSRTC-emblem.jp.jpg" width="150" height="150">
                    <figcaption>TSRTC</figcaption>
                </figure>
                <figure>
                    <img src="https://play-lh.googleusercontent.com/1x8dsoOUxPdQ7ForqkpRr65qRfvg5Uo8NgdEoOURgcm7zYl1F4F_t81WhlDS2kwcelY" width="150" height="150">
                    <figcaption>BSRTC</figcaption>
                </figure>
            </div>
            <div style="display: flex; justify-content: space-around; margin-top: 10px;">
                <figure>
                    <img src="https://upload.wikimedia.org/wikipedia/en/0/05/Kadamba_Transport_Corporation_logo.png" width="150" height="150">
                    <figcaption>KTCL</figcaption>
                </figure>
                <figure>
                    <img src="https://cryptologos.cc/logos/wrapped-bitcoin-wbtc-logo.png" width="150" height="150">
                    <figcaption>BSRTC</figcaption>
                </figure>
                <figure>
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4a/HRTCHP.jpg" width="150" height="150">
                    <figcaption>HRTC</figcaption>
                </figure>
                <figure>
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKqNc_vJkOrXS8gf1_fubJwSiFRwUxEUoDWw&s" width="150" height="150">
                    <figcaption>JKSRTC</figcaption>
                </figure>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="scan-playstore">
        <div>
            <h3>Scan to download</h3>
            <img src="https://pngimg.com/d/qr_code_PNG33.png" alt="Scan Code">
        </div>
        <div class="bus-image">
            <img src="https://content.jdmagicbox.com/comp/chennai/k5/044pxx44.xx44.130504183442.e9k5/catalogue/www-redbus-in-adyar-chennai-bus-ticketing-agents-tj1jv.jpg" alt="Bus Image">
        </div>
        <div>
            <h3>Download the App on</h3>
            <img src="https://i2.wp.com/zeevector.com/wp-content/uploads/2021/01/Google-Play-Store-Logo-PNG.png?fit=1024%2C500&ssl=1" alt="Play Store">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRY_o-G9mMFogqWSeYzzRALpqqr8E-pvKn39w&s" alt="Play Store">
        </div>
    </div>
    """, unsafe_allow_html=True)

# if selected option is Search Bus means then add these in the page
if selected=="Search Bus":
    st.title(":red[REDBUS] - 🔍 Search Bus")

    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
    col1, col2 = st.columns([4, 1])

    with col1:

        st.write("""
        Welcome to the Redbus search page! We're here to help you find the perfect bus for your journey. 
        Using our intuitive search and filtering options, you can easily customize your search according to your needs. Below given are steps to use this page
        1. **State and Route Selection**: Start by selecting the state you are traveling from. Then choose the specific route you are interested in.
        2. **Seat Type**: Use the dropdown to select your preferred type of seat. Whether it's a sleeper, semi-sleeper, or any other type, we have options for you.
        3. **Price Range**: Adjust the slider to set your budget. You can filter buses based on your preferred price range.
        4. **Star Rating**: Looking for a top-rated bus? Adjust the star rating filter to find buses with the highest ratings.
        5. **Starting Time**: Use the slider to choose the departure time that suits you best. Whether you prefer early morning departures or late-night buses, 
                 we've got you covered😉.
                 
        _After selecting your preferences, simply click on the 'Search' button to view the available options. The results will display here, and you can further refine your choices as needed._
        """)
 
        # fetching distinct state name for state name drop down
        query_distinct_state="select distinct state_name from route_data;"
        statename=fetch_distinct_value(conn,query_distinct_state) # the state name stored here (for state name dropdown)
        state_name = st.selectbox("State Name", ['--- select the state name ---'] + statename)
        
        # fetching route name based on state name for route_name drop down
        state=state_name #provide the name from statename
        filter_routes=f"select route_name from route_data where state_name = '{state}';"
        routename = fetch_route_names(conn,filter_routes)  # the route name stored here (for route name dropdown)
        route_name = st.selectbox("Route Name", ['--- select the route name --'] + routename)

    with col2:
        st.subheader("Filters")

        # fetching distinct seat type values
        query_bus_type="select distinct bus_type from bus_data;"
        bustype=fetch_distinct_bustype(conn,query_bus_type) # the bus type stored here ( for bus type dropdown)
        bus_type=st.selectbox("Seat Type", ['--- select bus type ---'] + ['All'] + bustype)
        
        price=st.slider("Price Range", min_value=0, max_value=3000, value=(0, 3000), step=100)
        starting_price , ending_price = price

        rating=st.slider("Star Rating", min_value=0, max_value=5, value=(0,5), step=1)
        start_rating , end_rating = rating
        
        s_time=st.slider("Starting Time", min_value=0, max_value=24, value=(0, 24), step=1)
        start_time , end_time = s_time

    st.markdown("""
    <style>
        .stButton > button {
            background-color: #E6E6FA;
            color: #EE4B2B; 
            border: none; 
            padding: 10px 600px;
            text-align: center;
            display: inline-block;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
        }
    </style>
    """, unsafe_allow_html=True)
    if st.button("SEARCH"):
        query_fetch_filter_data=f"""select 
            r.route_name, 
            r.route_link, 
            b.bus_name, 
            b.bus_type, 
            b.departing_time, 
            b.duration, 
            b.reaching_time, 
            b.star_rating,
            b.price,
            b.seat_available
            from 
                route_data r
            join 
                bus_data b on r.route_no = b.bus_no
            where
                r.state_name = '{state_name}'
                and r.route_name = '{route_name}'
                and (b.bus_type = '{bus_type}' or '{bus_type}' = 'All')  
                and b.star_rating between {start_rating} and {end_rating}
                and b.price between {starting_price} and {ending_price}
                and extract(hour from b.departing_time) between {start_time} and {end_time};"""
        
        
        with st.spinner('loading..'):
            time.sleep(2)

        #fetch the bus data based on the filtering options     
        filtered_data=fetch_filtered_value(conn,query_fetch_filter_data)

        #check if the filtered data is empty or not
        if not filtered_data.empty:
            st.dataframe(data=filtered_data)
        else:
            st.markdown("""
            <div style="text-align: center;">
                <h4>**Sorry🫠 No bus is available for the selected filtering options**</h4>
            </div>
            """, unsafe_allow_html=True)


## close connection
close_connection(conn)
