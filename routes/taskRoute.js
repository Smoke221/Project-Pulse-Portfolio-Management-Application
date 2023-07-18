const express = require("express");
const taskRouter = express.Router();
const { taskModel } = require("../models/taskModel");

// Create a new Task
taskRouter.post("/tasks", async (req, res) => {
  try {
    const task = new taskModel(req.body);
    const savedTask = await task.save();

    res
      .status(201)
      .json({ msg: "New task successfully added", data: savedTask });
  } catch (error) {
    res.status(400).json({ msg: error.message });
  }
});

// Get all Tasks
taskRouter.get("/tasks", async (req, res) => {
  try {
    const tasks = await taskModel
      .find()
      .populate("project")
      .populate("resources");
    res.json(tasks);
  } catch (error) {
    res.status(500).json({ msg: error.message });
  }
});

// Update a Task
taskRouter.patch("/tasks/:id", getTask, async (req, res) => {
  try {
    // Update the task fields based on the request body
    for (const [key, value] of Object.entries(req.body)) {
      res.task[key] = value;
    }
    const updatedTask = await res.task.save();
    res.json(updatedTask);
  } catch (error) {
    res.status(400).json({ msg: error.message });
  }
});

// Delete a Task
taskRouter.delete("/tasks/:id", getTask, async (req, res) => {
  try {
    await res.task.remove();
    res.json({ msg: "Task deleted successfully" });
  } catch (error) {
    res.status(500).json({ msg: error.message });
  }
});

// Middleware function to get Task by ID
async function getTask(req, res, next) {
  try {
    const task = await taskModel.findById(req.params.id);
    if (!task) {
      return res.status(404).json({ msg: "Task not found" });
    }
    res.task = task;
    next();
  } catch (error) {
    res.status(500).json({ msg: error.message });
  }
}

module.exports = { taskRouter };
