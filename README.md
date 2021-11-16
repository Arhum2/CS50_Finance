<h1> Welcome to my CS50_Finance project! </h1>

*This project was done as a part of Harvards CS50 on EdX, more information and its requirments can be found [here](https://cs50.harvard.edu/x/2021/psets/9/finance/)*

In this project i created the following pages...

1. Register - Allows users to register a account on the site. a username and password are submitted via Flask and a hash is generated to enrypt the password wich is then stored in a SQLite 3 data base
2. Quote - Allows users to lookup stock's and thier price in real time using [iex's cloud API](https://iexcloud.io/)
3. Buy - Allows users to enter a stock symbol and the number of shares they would like to purchase. 'buy' and 'history' tables are updated on stocks bought and cash spent
4. Index - Displays the users stock portfollio such as stocks owned, cash, protfolio value, etc...
5. Sell - Allows users to sell thier stocks. 'buy' and 'history' tables are updated on stocks sold and cash gained
6. History - Displays the 'history' table, showing all of the users purchases and sales alon with thier price and time of sale/purchase

Code outside of this was provided by CS50.
