## Python: Code, Test, Deploy

# Deploy Flask App to Heroku
 ---

# Synopsis

Source: https://github.com/datademofun/heroku-basic-flask

## Barebones Flask to Heroku

1. `pip install flask gunicorn`
2. `touch app.py`
3. 
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Appland!"

if __name__ == "__main__":
    app.run()
``` 
4. `pip install jinja werkzeug`
5. `pip freeze > requirements.txt`
6. `touch Procfile'
7.
```

```



# Tutorials
[5 Min Flask to Heroko](https://youtu.be/pmRT8QQLIqk)
