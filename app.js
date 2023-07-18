const express = require("express");
const cors = require("cors");
const { connection } = require("./configs/db");
const { router } = require("./routes/managerRoutes");
const { taskRouter } = require("./routes/taskRoute");
const app = express();
require("dotenv").config();

app.use(express.json());
app.use(cors());

app.get("/", (req, res) => {
  res.send("Sample route is working fine!");
});

app.use("/api", router);
app.use("/pulse", taskRouter)

port = process.env.PORT || 3000;
app.listen(port, async () => {
  try {
    await connection;
    console.log("Connected to database");
  } catch (error) {
    console.log("Something went wrong:" + error.message);
  }
  console.log(`App is running on port ${process.env.port}`);
});
