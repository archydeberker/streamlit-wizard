from streamlit_wizard import components

import example_pages

intro = example_pages.IntroPage(name="intro")
data = example_pages.FirstPageOfQuestions(name="questions")

wizard = components.Wizard(pages=[intro, data])

wizard.render()
