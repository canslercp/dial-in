# dial-in
An app that helps people brew the tastiest coffee possible

## To Run Locally
run the following commands from the root directory of dial-in:

```python3 -m venv venv```

```. venv/bin/activate```

```pip install -r requirements.txt```

Next, create a .env file in the root directory of the project, and add the following line to it:

```DB_URL=mongodb+srv://<username>:<password>@cluster0.p5bbjdq.mongodb.net/?retryWrites=true&w=majority```

Make sure to change ```<username>``` and ```<password>``` to the username and password of your of your MongoDB login.

```python3 seeds.py```

```python -m flask run```
