from flask import Flask
from Routes.process import (
    welcome,
    get_managers,
    get_manager,
    create_manager,
    update_manager,
    delete_manager
)
from Routes.projects_process import (
    get_all_projects,
    get_project,
    create_project,
    update_project,
    get_projects_with_empty_manager,
    delete_project,
    update_project_manager,
    # get_projects_by_manager_id
)
from Routes.task_process import (
    get_all_tasks,
    get_task,
    create_task,
    update_task,
    delete_task,
    count_tasks_by_resource,
    get_all_tasks_by_manager_id,
    get_all_tasks_by_project_id
)
from Routes.resource_process import (
    get_all_resources,
    get_resource,
    create_resource,
    update_resource,
    delete_resource,
    get_all_resources_by_task_id
)
app = Flask(__name__)

# Welcome route - A simple welcome message.
app.route("/", methods=["GET"])(welcome)

# --- Manager Routes ---
# Get all managers - Fetches a list of all managers from the database.
app.route('/pulse/managers', methods=['GET'])(get_managers)

# Get manager by ID - Fetches a specific manager by their unique manager_id.
app.route('/pulse/managers/<string:manager_id>', methods=['GET'])(get_manager)

# Create a new manager - Adds a new manager to the database.
app.route('/pulse/managers', methods=['POST'])(create_manager)

# Update manager - Modifies an existing manager in the database.
app.route('/pulse/managers/<string:manager_id>', methods=['PATCH'])(update_manager)

# Delete manager - Removes a manager from the database.
app.route('/pulse/managers/<string:manager_id>', methods=['DELETE'])(delete_manager)

# --- Project Routes ---
# Get all projects - Fetches a list of all projects from the database.
app.route('/projects', methods=['GET'])(get_all_projects)

# Get a single project - Fetches a specific project by its unique project_id.
app.route('/projects/<string:project_id>', methods=['GET'])(get_project)

# Get all projects where manager is empty - Fetches projects without an assigned manager.
app.route('/projects/empty_manager', methods=['GET'])(get_projects_with_empty_manager)

# Create a new project - Adds a new project to the database.
app.route('/projects', methods=['POST'])(create_project)

# Update a project - Modifies an existing project in the database.
app.route('/projects/<string:project_id>', methods=['PUT'])(update_project)

# Update the manager of a project - Modifies the manager assigned to a project.
app.route('/projects/manager/<string:project_id>', methods=['PUT'])(update_project_manager)

# Delete a project - Removes a project from the database.
app.route('/projects/<string:project_id>', methods=['DELETE'])(delete_project)

# --- Task Routes ---
# Get all tasks - Fetches a list of all tasks from the database.
app.route('/tasks', methods=['GET'])(get_all_tasks)

# Get a single task by task_id - Fetches a specific task by its unique task_id.
app.route('/tasks/<string:task_id>', methods=['GET'])(get_task)

# Get all tasks by manager id - Fetches tasks assigned to a specific manager.
app.route('/tasks/manager/<string:manager_id>', methods=['GET'])(get_all_tasks_by_manager_id)

# Get all tasks by project id - Fetches tasks associated with a specific project.
app.route('/tasks/project/<string:project_id>', methods=['GET'])(get_all_tasks_by_project_id)

# Get the count of tasks assigned to a specific resource.
app.route('/tasks/resources/<string:resource_id>', methods=['GET'])(count_tasks_by_resource)

# Create a new task - Adds a new task to the database.
app.route('/tasks', methods=['POST'])(create_task)

# Update a task by task_id - Modifies an existing task in the database.
app.route('/tasks/<string:task_id>', methods=['PUT'])(update_task)

# Delete a task by task_id - Removes a task from the database.
app.route('/tasks/<string:task_id>', methods=['DELETE'])(delete_task)


# --- Resource Routes ---
# Get all resources - Fetches a list of all resources from the database.
app.route('/resources', methods=['GET'])(get_all_resources)

# Get all resources by task_id - Fetches resources associated with a specific task.
app.route('/resources/task/<string:task_id>', methods=['GET'])(get_all_resources_by_task_id)

# Get a specific resource by resource_id - Fetches a specific resource by its unique resource_id.
app.route('/resources/<string:resource_id>', methods=['GET'])(get_resource)

# Create a new resource - Adds a new resource to the database.
app.route('/resources', methods=['POST'])(create_resource)

# Update a resource by resource_id - Modifies an existing resource in the database.
app.route('/resources/<string:resource_id>', methods=['PUT'])(update_resource)

# Delete a resource by resource_id - Removes a resource from the database.
app.route('/resources/<string:resource_id>', methods=['DELETE'])(delete_resource)


if __name__ == '__main__':
    app.run(debug=True)