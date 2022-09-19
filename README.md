# streamlit-wizard
This is an example of creating a wizard within Streamlit.

To use it, create your page objects by inheriting from the `Page` class in components,
and pass the resulting pages into the `Wizard` class as illustrated in `main.py`.

## Styling
Some custom CSS styling is used for the container. You can fiddle with it in `static/style.css`

## State
Streamlit session state is used to store the current page and to move data between pages. See `example_pages.py`
for an example of how you can retrieve data stored on previous pages. I've not thought this pattern through
very deeply, please let me know if there's a better way of doing it - obviously handling state in nested
components in complex, see Redux.

## Running
```
pip install -r requirements.txt
streamlit run main.py
```

