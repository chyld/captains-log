/*eslint no-console: "off"*/

const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  console.log("GET /");
  res.json({ hello: "world" });
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
