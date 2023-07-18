const { managerModel } = require("../models/managerModel");

// Middleware function to get Portfolio Manager by ID
async function getPortfolioManager(req, res, next) {
  try {
    const portfolioManager = await managerModel.findById(req.params.id);
    if (portfolioManager == null) {
      return res.status(404).json({ message: "Portfolio Manager not found" });
    }
    res.portfolioManager = portfolioManager;
    next();
  } catch (err) {
    return res.status(500).json({ message: err.message });
  }
}

module.exports = getPortfolioManager;
