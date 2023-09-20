import plotly.express as px
import pandas as pd
import random




# Sample data with tasks, start dates, and durations
data = {
    'Task': ['Task 1', 'Task 2', 'Task 3','Task 4', 'Task 5', 'Task 6','Task 7', 'Task 8', 'Task 9',
             'Task 10', 'Task 11', 'Task 12','Task 13', 'Task 14', 'Task 15','Task 16', 'Task 17', 'Task 18'],
    'Start': ['2023-09-10', '2023-09-15', '2023-09-20', '2023-09-20','2023-09-20','2023-09-20','2023-09-20', '2023-09-20','2023-09-20',
              '2023-09-10', '2023-09-15', '2023-09-20', '2023-09-20','2023-09-20','2023-09-20','2023-09-20', '2023-09-20','2023-09-20',],
    'Finish': ['2023-09-15', '2023-09-22', '2023-09-25', '2023-09-25','2023-09-25','2023-09-25','2023-09-25','2023-09-25','2023-09-25',
               '2023-09-15', '2023-09-22', '2023-09-25', '2023-09-25','2023-09-25','2023-09-25','2023-09-25','2023-09-25','2023-09-25'],
}

df = pd.DataFrame(data)

fig = px.timeline(df, x_start='Start', x_end='Finish', y='Task')
fig.update_yaxes(categoryorder='total ascending')

# Make the Gantt chart interactive
fig.update_traces(
    selector=dict(type='bar'),
    hoverinfo='x+name',  # Show task name and duration on hover
    hoverlabel=dict(namelength=-1)  # Show full task name
)

# Update the font properties (e.g., make the font size smaller)
fig.update_layout(
    font=dict(size=10)  # Set the font size to 10
)

# Save the Gantt chart as an HTML file
fig.write_html('interactive_gantt_chart.html')

# Show the chart
fig.show()