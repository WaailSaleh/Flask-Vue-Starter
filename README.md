# Flask + Vue Template

## Starting Flask Development Server

```sh
cd flask-app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
source venv/bin/activate
flask run --reload --host=0.0.0.0
```

## Starting VueJS Development Server

```sh
cd vue-app
npm run serve
```

### Your Task
You are currently working to create a simple SPA that can render a users financial transactions from a variety of banks.
You've partnered up with three financial data providers, DataFast, DastSecure and DataVast who each provide the financial data form their partnered institutions. You're task is to connect to their API from your backend Flask application and filter the data so that only unique transactions are sent to and displayed by your SPA.

#### Accessing the API
Your interviewer will provide you with a url for your backend to interface with. Aside from that there are four endpoints to take note of, 
```
/token 
/DataFast
/DataSecure
/DataVast
```
You are to access the api using the token provided by the `/token` endpoint which returns the bearer token that you will attach as a header in all of your other requests. The other three endpoints will return a list of transactions that that specific provider has.
