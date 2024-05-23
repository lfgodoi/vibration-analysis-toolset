# Importing packages and modules
from flask import Flask

# Setting up the app
app = Flask(__name__)
app.config["SECRET_KEY"] = "ViBRaTioNANAlySiSTooLSet"

# Running the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)