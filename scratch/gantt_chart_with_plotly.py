import plotly.figure_factory as ff
import random

# Sample data with 100 tasks and random timelines
tasks = []
colors = []

for i in range(1, 101):
    start_time = random.randint(0, 50)
    end_time = start_time + random.randint(1, 10)
    task_name = f'Task {i}'
    tasks.append(dict(Task=task_name, Start=start_time, Finish=end_time))

    # Generate random RGB color
    color = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'
    colors.append(color)

# Create a Gantt chart using Plotly figure_factory
fig = ff.create_gantt(tasks, colors=colors, index_col='Task', show_colorbar=True)

# Customize the appearance of the Gantt chart
fig.update_layout(title='Gantt Chart with Timelines and Random Colors', height=1600)  # Double the height

# Save the Gantt chart as an HTML file
chart_filename = 'gantt_chart.html'
fig.write_html(chart_filename)

# Show the Gantt chart
fig.show()

print(f'Gantt chart saved as {chart_filename}')
