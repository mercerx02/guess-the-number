from flask import Flask
import random
app = Flask(__name__)
num = random.randint(1, 10)
@app.route("/")
def hello_world():


    return "<h1>Guees the number</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<var>",methods=["GET"])
def guees_numb(var):
    if int(var) < num:
        return "<h1>TO LOW!</h1>" \
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif int(var) > num:
        return "<h1>TO HIGH!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
        return "<h1>CORRECT!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"



if __name__ == "__main__":
    app.run()

