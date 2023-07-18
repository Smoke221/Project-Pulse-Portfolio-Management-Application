const mongoose = require("mongoose");

const managerSchema = new mongoose.Schema({
  name: { type: String, required: true },
  bio: { type: String },
  startDate: { type: Date, required: true },
  status: { type: Boolean, default: true },
  role: { type: String, enum: ["Administrator", "Viewer"], default: "Viewer" },
});

const managerModel = mongoose.model("manager", managerSchema);

module.exports = { managerModel };
