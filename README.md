
# Club Registration Form
This is an application for a Club Registration Form. This application will be used by a club at a club fair. 
Students who stop by the club's table can input their email address and other information into the application. 
The application then store these information for the club to use. 

This was inpisred by the react comment box example from [the React tutorial](http://facebook.github.io/react/docs/tutorial.html).

## To use

### Python

```sh
pip install -r requirements.txt
pytest server.py # Build and test
python server.py
```
If the data needs to be stored in PostgreSQL database, another package is required
```sh
sudo apt-get install python-psycopg2
```
And visit <http://localhost:3001/>. Try opening multiple tabs!

## Build and test snapshot
#### * Testcase input on webpage
![Testcase](/test_input.png)
#### * Testcase output in PostgreSQL database
![Testcase](/test.png)
