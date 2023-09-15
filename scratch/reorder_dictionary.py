tasks = {
    2: {
        'task_title': 'Mikkels Job Dexcription update',
        'parent': 'root',
        'created_by': 'arsithra',
        'date_created': '2023-09-14',
        'time_created': '17:13',
        'assigned_to': 'arsithra',
        'start_date_interval': '2023-09-13',
        'end_date_interval': '2023-09-20',
        'hours_allocated': '90',
        'prio': 'CRITICAL',
        'status': 'InProgress',
        'active': True,
        'task_details': ['', 'need to update Mikkels job description as of deadline', 'Like tomorrow latest'],
        'tags': []
    },
    3: {
        'task_title': 'soon',
        'parent': 'root',
        'created_by': 'arsithra',
        'date_created': '2023-09-15',
        'time_created': '08:17',
        'assigned_to': 'arsithra',
        'start_date_interval': '2023-09-13',
        'end_date_interval': '2023-09-19',
        'hours_allocated': '30',
        'prio': 'Medium',
        'status': 'InProgress',
        'active': True,
        'task_details': ['', 'asdfsdf'],
        'tags': []
    },
    4: {
        'task_title': 'talk to Tara',
        'parent': 'root',
        'created_by': 'arsithra',
        'date_created': '2023-09-15',
        'time_created': '09:34',
        'assigned_to': 'arsithra',
        'start_date_interval': '2023-09-13',
        'end_date_interval': '2023-09-29',
        'hours_allocated': '',
        'prio': 'Normal',
        'status': 'InProgress',
        'active': True,
        'task_details': ['', 'get some updates', '', 'talk some more about more stuff'],
        'tags': []
    },
    5: {
        'task_title': 'Test Parent - Should not Load',
        'parent': 'root',
        'created_by': 'arsithra',
        'date_created': '2023-09-15',
        'time_created': '11:18',
        'assigned_to': 'arsithra',
        'start_date_interval': '2023-09-15',
        'end_date_interval': '2023-09-15',
        'hours_allocated': '',
        'prio': 'Low',
        'status': 'Init',
        'active': True,
        'task_details': [],
        'tags': ''
    }
}

tt = {"2": {"task_title": "Mikkels Job Dexcription update", "parent": "root", "created_by": "arsithra", "date_created": "2023-09-14", "time_created": "17:13", "assigned_to": "arsithra", "start_date_interval": "2023-09-13", "end_date_interval": "2023-09-20", "hours_allocated": "90", "prio": "CRITICAL", "status": "InProgress", "active": True, "task_details": ["", "need to update Mikkels job description as od deadline", "Like tomorrow latest"], "tags": []}, "3": {"task_title": "soon", "parent": "root", "created_by": "arsithra", "date_created": "2023-09-15", "time_created": "08:17", "assigned_to": "arsithra", "start_date_interval": "2023-09-13", "end_date_interval": "2023-09-19", "hours_allocated": "30", "prio": "Medium", "status": "InProgress", "active": True, "task_details": ["", "asdfsdf"], "tags": []}, "4": {"task_title": "talk to Tara", "parent": "root", "created_by": "arsithra", "date_created": "2023-09-15", "time_created": "09:34", "assigned_to": "arsithra", "start_date_interval": "2023-09-13", "end_date_interval": "2023-09-29", "hours_allocated": "", "prio": "Normal", "status": "InProgress", "active": True, "task_details": ["", "get some updates", "", "talk some more about more stuff"], "tags": []}, "5": {"task_title": "Test Parent - Should not Load", "parent": "root", "created_by": "arsithra", "date_created": "2023-09-15", "time_created": "11:18", "assigned_to": "arsithra", "start_date_interval": "2023-09-15", "end_date_interval": "2023-10-15", "hours_allocated": "", "prio": "Low", "status": "Init", "active": True, "task_details": [], "tags": ""}}

# Reorder the tasks based on the "end_date_interval"
sorted_tasks = dict(sorted(tt.items(), key=lambda item: item[1]['end_date_interval']))
print(sorted_tasks)
# Print the reordered tasks
for task_id, task_data in sorted_tasks.items():
    print(f"{task_id}: {task_data['task_title']} - {task_data['end_date_interval']}")



# Define the dictionary of tasks
tasks = {
    2: {
        'task_title': 'Mikkels Job Description update',
        'prio': 'CRITICAL',
        # ... other fields
    },
    3: {
        'task_title': 'soon',
        'prio': 'Medium',
        # ... other fields
    },
    4: {
        'task_title': 'talk to Tara',
        'prio': 'Normal',
        # ... other fields
    },
    5: {
        'task_title': 'Test Parent - Should not Load',
        'prio': 'Low',
        # ... other fields
    }
}

# Define the priority order
priority_order = ["Low", "Normal", "Medium", "High", "CRITICAL"]

# Reorder the tasks based on priority
sorted_tasks = dict(sorted(tasks.items(), key=lambda item: priority_order.index(item[1]['prio'].capitalize())))

# Print the reordered tasks
for task_id, task_data in sorted_tasks.items():
    print(f"{task_id}: {task_data['task_title']} - {task_data['prio']}")
