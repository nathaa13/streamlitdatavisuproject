from multiapp import MultiApp
from apps import home, steps, spotify

app = MultiApp()

app.add_app("Home", home.app)
app.add_app("Step Data", steps.app)
app.add_app("Spotify Data", spotify.app)
# The main app

app.run()
