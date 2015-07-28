from flask import Flask
from data import insertThanks, GetAllThanks

app = Flask(__name__)

insertThanks('test', 'thanks mate')

@app.route("/")
def GetAllThanksFromDb():
	result = "<ul>"
	for thanks in GetAllThanks():
		result += "<li>" + thanks.message + "</li>"
	result += "</ul>"
	return result

if __name__ == "__main__":
	app.run()