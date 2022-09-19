#streamlit-wizard
This is an example of creating a wizard within streamlit.

To use it, create your page objects by inheriting from the `Page` class in components,
and pass the resulting pages into the `Wizard` class as illustrated in `main.py`.

## Styling
Some custom CSS styling is used for the container. You can fiddle with it in `static/style.css`

## State
Streamlit session state is used to store the current page. You could store other data in there too if you liked!

## Running
```
pip install -r requirements.txt
streamlit run main.py
```

