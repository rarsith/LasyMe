import random
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.figure_factory as ff

app = dash.Dash(__name__)

# Sample data with 5 tasks and random timelines
tasks = []
colors = []

for i in range(1, 6):
    start_time = random.randint(0, 50)
    end_time = start_time + random.randint(1, 10)
    task_name = f'Task {i}'
    tasks.append(dict(Task=task_name, Start=start_time, Finish=end_time))

    # Generate random RGB color
    color = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
    colors.append(color)

fig = ff.create_gantt(tasks, colors=colors, index_col='Task', show_colorbar=True)

app.layout = html.Div([
    dcc.Graph(figure=fig, id='gantt-chart')
])


@app.callback(
    Output('gantt-chart', 'figure'),
    Input('gantt-chart', 'relayoutData')
)
def update_chart(relayoutData):
    # Implement logic to update the chart based on user interaction
    # relayoutData will contain information about the resized task
    # You would need to update the task data and return a new figure
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
