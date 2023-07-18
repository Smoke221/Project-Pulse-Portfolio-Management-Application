const mongoose = require("mongoose");
const managerModel = require("./managerModel");

const projectSchema = new mongoose.Schema({
  projectName: { type: String, required: true },
  status: {
    type: String,
    enum: ["Planned", "In Progress", "Completed"],
    default: "Planned",
  },
  startDate: { type: Date },
  endDate: { type: Date },
  portfolioManager: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "managerModel",
    required: true,
  },
});

const projectModel = mongoose.model("project", projectSchema);

module.exports = { projectModel };
