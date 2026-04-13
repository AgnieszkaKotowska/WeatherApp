import plotly.express as px
import dash
from dash import dcc, html

# x=[1,2,3,4,5]
# y=[10,15,13,20,17]
#
# fig = px.line(
#     x=x,
#     y=y,
#     title="tytul")
# fig.show()

# produkty = ["A", "B", "C", "D"]
# wyniki = [12, 19, 7, 15]
#
# fig1 = px.bar(x=produkty, y=wyniki, title="Slupkowy", orientation="h")
# fig1.show()

# x = [1,2,3,4,5]
# y = [3,7,4,9,6]
#
# fig2 = px.bar(x=x, y=y, title='xxx')
# fig2.show()

# oceny = [1,2,3,4,5,6,5,4,4,4,1]
#
# fig3 = px.histogram(oceny, x=oceny, nbins=4, title="oceny")
# fig3.show()

# etykiety = ["Py", "JS", "C++", "Java"]
# wartosci = [40,25,15,20]
#
# fig4 = px.pie(names=etykiety, values=wartosci, title="Jezyki")
# fig4.show()

# Wyswietlenie wykresow,dashboarda na localhost
#
# # Dane
# x = [1,2,3,4,5]
# y1 = [10,15,13,20,17]
# y2 = [3,7,4,9,6]
#
# produkty = ["A","B","C","D"]
# wyniki = [12,19,7,15]
#
# oceny = [2,4,5,2,3,4,5,4,3,2,3,4,5]
#
# etykiety = ["Python","Java","C++","Javascript"]
# wartosci = [40,25,15,20]
#
# # Wykresy
# fig_line = px.line(x=x, y=y1, title="Trend", markers=True)
# fig_bar = px.bar(x=produkty, y=wyniki, title="Produkty")
# fig_scatter = px.scatter(x=x, y=y2, title="Relacja")
# fig_hist = px.histogram(x=oceny, nbins=4, title="Oceny")
# fig_pie = px.pie(names=etykiety, values=wartosci, title="Języki")
#
# # Dashboard
# app = dash.Dash(__name__)
#
# app.layout = html.Div(
#     style={"fontFamily": "Arial", "backgroundColor": "#f5f7fa"},
#     children=[
#         html.H1("Mój Dashboard", style={"textAlign": "center"}),
#
#         html.Div([
#             dcc.Graph(figure=fig_line),
#             dcc.Graph(figure=fig_bar),
#         ], style={"display": "flex"}),
#
#         html.Div([
#             dcc.Graph(figure=fig_scatter),
#             dcc.Graph(figure=fig_hist),
#         ], style={"display": "flex"}),
#
#         html.Div([
#             dcc.Graph(figure=fig_pie)
#         ])
#     ]
# )
#
# if __name__ == "__main__":
#     app.run(debug=True)

# Zadania

# Zadanie 4 Plotly
# Stwórz wykres punktowy, który pokaże zależność między:
# - liczbą godzin nauki
# - wynikiem egzaminu

godziny_nauki = [1, 2, 3, 4, 5, 6, 7]
wyniki = [40, 50, 55, 60, 70, 75, 85]

fig = px.scatter(
    x=godziny_nauki,
    y=wyniki,
    title="Zależność między godzinami nauki a wynikiem egzaminu",
    labels={"x": "Liczba godzin nauki", "y": "Wynik egzaminu"}
)
fig.show()

# --------------------------------------------------------------
# Zadanie 5 Plotly
# Stwórz wykres kołowy, który pokaże udział języków programowania używanych przez programistów w projekcie.
jezyki = ["Python", "JavaScript", "Java", "C++", "Go"]
udzial = [35, 30, 15, 10, 10]

fig_pie = px.pie(
    values=udzial,
    names=jezyki,
    title="Jezyki programowania w projekcie"
)
fig_pie.show()

# ------------------------------------------------------------------------------
# Zadanie 6 Plotly
# Stwórz interaktywny wykres liniowy, który pokaże temperaturę w kolejnych dniach tygodnia.
dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
temperatura = [18, 20, 19, 23, 25, 22, 21]

fig_line = px.line(
    x=dni,
    y=temperatura,
    labels={"x": "Dzien tygodnia", "y": "Temperatura"},
)

fig_line.show()

# ------------------------------------------------------------------------------