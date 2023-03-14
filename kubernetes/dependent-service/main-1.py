from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    r = requests.get("http://backend:9990/")
    return "Hello from FrontEnd + " + r.content.decode("utf-8") 
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9990, debug=False)