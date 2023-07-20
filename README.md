# Project-Pulse-Portfolio-Management-Application
Project Pulse is a powerful and user-friendly web application designed to streamline the process of project and task management for portfolio managers. It serves as a holistic Portfolio Management System, empowering managers to efficiently oversee a collection of projects and associated tasks, ensuring seamless coordination of resources.

#### ER Diagram
![ER Diagram)](https://github.com/Smoke221/Project-Pulse-Portfolio-Management-Application/assets/114225283/20e1f914-0fec-44f4-ba52-d13534ca6765)

#### [Mock UI](https://app.moqups.com/toCtUSWlceueWbNYFBWSnMjTzdI2Dr7C/view/page/ad64222d5?ui=0)
You can explore the initial frontend section of my application here, where you'll find an opportunity for further enhancement and refinement.

# API Endpoints

## Managers

- `GET /pulse/managers`: Fetches all portfolio managers' profiles.
- `POST /pulse/managers`: Creates a new portfolio manager profile.
- `PATCH /pulse/managers/:id`: Updates an existing portfolio manager's profile by ID.
- `DELETE /pulse/managers/:id`: Deletes a portfolio manager's profile by ID.

## Projects

- `GET /pulse/projects`: Fetches all projects' details.
- `POST /pulse/projects`: Creates a new project with its details.
- `PATCH /pulse/projects/:id`: Updates an existing project's details by ID.
- `DELETE /pulse/projects/:id`: Deletes a project by ID.

## Tasks

- `GET /pulse/tasks`: Fetches all tasks' details.
- `POST /pulse/tasks`: Creates a new task with its details.
- `PATCH /pulse/tasks/:id`: Updates an existing task's details by ID.
- `DELETE /pulse/tasks/:id` : Deletes a task by ID.
