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

# Example Usage
```
from streamlit_wizard import components

class IntroPage(Page):
    def render(self) -> dict:
        st.title("Intro")
        st.write("This is the intro page")
        accept = st.radio(
            "Do you understand that",
            options=["Yes", "No", "Can you repeat the question"],
        )
        return dict(accept=accept)


class FirstPageOfQuestions(Page):
    def render(self) -> dict:
        st.title("Question Page")
        st.write("We will have some questions here")

        # We can access the other page state via session storage if we know what it is called
        # This is presumably not a very robust solution

        did_they_accept = st.session_state["page_state"]["intro"]["accept"]
        st.write(f"On the previous page you selected {did_they_accept}")
        fave_bean = st.selectbox(
            "What is your favourite jelly bean colour", ["Red", "Orange", "Green"]
        )
        return dict(fave_bean=fave_bean)


intro = example_pages.IntroPage(name="intro")
data = example_pages.FirstPageOfQuestions(name="questions")

wizard = components.Wizard(pages=[intro, data])

wizard.render()

```

# Publishing
```
python3 -m build && python3 -m twine upload dist/*
```

