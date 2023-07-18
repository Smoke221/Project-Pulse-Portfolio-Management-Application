const express = require("express");
const { managerModel } = require("../models/managerModel");
const getManagerById = require("../middlewares/getManagerById");
const router = express.Router();

router.post("/portfolio-managers", async (req, res) => {
  try {
    const portfolioManager = new managerModel(req.body);
    const savedManager = await portfolioManager.save();

    res
      .status(201)
      .json({ msg: "New manager successfully added", data: savedManager });
  } catch (error) {
    res.status(400).json({ msg: error.message });
  }
});

// Get all Portfolio Managers
router.get("/portfolio-managers", async (req, res) => {
  try {
    const portfolioManagers = await managerModel.find();
    res.json(portfolioManagers);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Get a specific Portfolio Manager
router.get("/portfolio-managers/:id", getManagerById, (req, res) => {
  res.json(res.portfolioManager);
});

module.exports = { router };
