import pandas as pd
import plotly.express as px
import plotly.graph_objects as pg

#read the data from the CSV file -- table with 5 rows and 20 columns
data = pd.read_csv("D:\Projects_Unlimited\DataScience_IPL-Analysis\Book_ipl22_ver_33.csv")
print(data.head())

#no. of matches won by each team in IPL 2022 -- bar graph
figure = px.bar(data, x=data["match_winner"],
            title="Number of Matches Won in IPL 2022")
figure.show()

#whether most of the teams win by defending or chasing -- pie chart
data["won_by"] = data["won_by"].map({"Wickets": "Chasing", "Runs": "Defending"})
won_by = data["won_by"].value_counts()
label = won_by.index
counts = won_by.values
colors = ['gold','lightgreen']

fig = pg.Figure(data=[pg.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches Won By Defending Or Chasing')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30, marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()

#let's see what most teams prefer after winning toss
toss = data["toss_decision"].value_counts()
label = toss.index
counts = toss.values
colors = ['skyblue','yellow']

fig = pg.Figure(data=[pg.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Toss Decision')
fig.update_traces(hoverinfo='label+percent',
                  textinfo='value', textfont_size=30,
                  marker=dict(colors=colors,
                              line=dict(color='black', width=3)))
fig.show()

#let's see the top scorers of most IPL 2022 matches
figure = px.bar(data, x=data["top_scorer"], title="Top Scorers in IPL 2022")
figure.show()

#runs scored by top scorers
figure = px.bar(data, x=data["top_scorer"], y = data["highscore"], color = data["highscore"], title="Top Scorers in IPL 2022")
figure.show()

#most player of the match awards in IPL 2022
figure = px.bar(data, x = data["player_of_the_match"], title="Most Player of the Match Awards")
figure.show()

#let's have a look at the best bowling figures in most of the matches
figure = px.bar(data, x=data["best_bowling"], title="Best Bowlers in IPL 2022")
figure.show()

#know whether most of the wickets fall while setting the target or while chasing the target
figure = pg.Figure()
figure.add_trace(pg.Bar(
    x=data["venue"],
    y=data["first_ings_wkts"],
    name='First Innings Wickets',
    marker_color='gold'
))
figure.add_trace(pg.Bar(
    x=data["venue"],
    y=data["second_ings_wkts"],
    name='Second Innings Wickets',
    marker_color='lightgreen'
))
figure.update_layout(barmode='group', xaxis_tickangle=-45)
figure.show()
