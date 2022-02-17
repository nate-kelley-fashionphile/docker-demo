const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.send({ message: "Hello World From Node 16!" });
});

app.listen(port, () => {
  console.log(`Example Node 16 app listening at http://localhost:${port}`);
});
