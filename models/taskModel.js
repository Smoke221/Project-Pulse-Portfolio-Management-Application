const mongoose = require("mongoose");
const projectModel = require("./projectModel");

const taskSchema = new mongoose.Schema({
  taskName: { type: String, required: true },
  status: {
    type: String,
    enum: ["To Do", "In Progress", "Completed"],
    default: "To Do",
  },
  project: { type: mongoose.Schema.Types.ObjectId, ref: "projectModel", required: true },
});

const taskModel = mongoose.model("task", taskSchema);

module.exports = { taskModel };
