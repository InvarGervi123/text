````markdown
# Text Saver Web App

This is a simple Flask-based web application that allows users to input, save, and view custom text notes. The data is stored locally in a `text.txt` file.

## Features

- 📝 Add and save any text input
- 📂 Automatically loads and displays saved text from the `text.txt` file
- 🌐 Simple and clean HTML user interface

## How It Works

1. The app uses Flask to run a local web server.
2. The text from the `textarea` is saved to `text.txt` upon clicking the **Save** button.
3. When the page loads, the contents of `text.txt` are read and shown in the `textarea`.

## Installation

```bash
git clone https://github.com/InvarGervi123/text.git
cd text
pip install flask
````

## Running the App

```bash
python app.py
```

Then open your browser at: `http://localhost:5000/`

## File Structure

```
text/
├── app.py           # Main Flask application
├── templates/
│   └── index.html   # Front-end HTML with form
├── text.txt         # File to store the saved text
```

## Requirements

* Python 3.x
* Flask

Install Flask with:

```bash
pip install flask
```

## License

This project is open-source and free to use.
