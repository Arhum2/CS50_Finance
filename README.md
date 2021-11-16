<h1> Welcome to my CS50_Finance project! </h1>

*This project was done as a part of Harvard’s CS50 on EdX, more information and its requirements can be found [here](https://cs50.harvard.edu/x/2021/psets/9/finance/)*

In this project I created a practice stock trading web app using Python, Flask, HTML, CSS, and SQLite 3 for my database
the following pages I created are...

1. Register - Allows users to register an account on the site. a username and password are submitted via Flask and a hash is generated to encrypt the password which is then stored in an SQLite 3 data base
2. Quote - Allows users to lookup stock's and their price in real time using [iex's cloud API](https://iexcloud.io/)
3. Buy - Allows users to enter a stock symbol and the number of shares they would like to purchase. 'buy' and 'history' tables are updated on stocks bought and cash spent
4. Index - Displays the user’s stock portfolio such as stocks owned, cash, portfolio value, etc...
5. Sell - Allows users to sell their stocks. 'buy' and 'history' tables are updated on stocks sold and cash gained
6. History - Displays the 'history' table, showing all the users purchases and sales along with their price and time of sale/purchase

Code outside of this was provided by CS50.

![Capture](https://user-images.githubusercontent.com/82200170/141901981-e3de964c-a4c6-4cb8-ae7b-de62d5008901.JPG)
1. User registers and logs in and the 'users' table updates in the database

![2](https://user-images.githubusercontent.com/82200170/141902619-9d5496b3-364d-4520-94be-2a29d363c354.JPG)
2. index page opens and displays the users’ holdings 

![3](https://user-images.githubusercontent.com/82200170/141902998-035ca9ff-a6fd-41cb-a9f6-5be164674441.JPG)
3. Next the Quote page is used to determine the current price of a stock using Iex's cloud API

![4](https://user-images.githubusercontent.com/82200170/141904086-3b7bad4c-d1ca-4a66-af25-a943d8f7ca5f.JPG)
4. The stock and the number of shares is then bought through the buy page and the 'buy' and 'history' page are updated on money spent and stocks bought

![6](https://user-images.githubusercontent.com/82200170/141897383-2cbf710b-b173-4b5d-9575-6f02620db8e0.JPG)
![6 1](https://user-images.githubusercontent.com/82200170/141904770-ddecfd25-36c7-4d47-b025-fb3640f72b01.JPG)
5. The stock can then be sold on the sell page along with the desired number of shares, the 'buy' and 'history' tables are updated on money earned and stocks sold

![5](https://user-images.githubusercontent.com/82200170/141898131-a1c56905-db51-4890-9104-e65d1d6cd167.JPG)
6. Users can then view all their transaction history on the history page where the 'history' table is displayed
