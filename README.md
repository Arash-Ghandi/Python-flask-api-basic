# Flask Server Setup

This guide explains how to set up and run a simple Flask-based server.

Prerequisites

Ensure that the following software is installed on your system:

Python 3.x: Download and install from python.org.

Pip: Python's package installer should be installed with Python.

Flask: Flask is the micro web framework used for this project.


## Installation

Follow these steps to install the required dependencies and run the Flask server.

## 1. Clone the Project or Create the File

``` bash

git clone https://github.com/Arash-Ghandi/Python-flask-api-basic.git

```
``` bash

cd Python-flask-api-basic

```

## 2. Install Flask

You can install Flask via pip by running the following command in your terminal or command prompt:

``` bash
pip install flask

```
3. Running the Server

To run the Flask server, navigate to the folder where app.py is located and use this command:

``` bash

python app.py

```

After running the command, you should see an output similar to this:

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## 4. Accessing the Server

Open your browser and go to the following address:

http://127.0.0.1:5000/


## Customization

To change the server’s behavior, you can edit the app.py file and modify the route functions.

If you want the server to be accessible from other devices on the same network, make sure host='0.0.0.0' is set in the app.run() method.


Troubleshooting

Ensure Python and Flask are installed correctly. Run python --version and pip show flask to check.

If the server does not start, verify that there are no syntax errors in the code and ensure you are in the correct directory when running python app.py.


License

This project is licensed under the MIT License - see the LICENSE file for details.