import express, { Request, Response, NextFunction } from "express";

const app = express();
const port = 3000;

app.get("/", (req: Request, res: Response, next: NextFunction) => {
  res.send({ message: "Hello World From Node 17 with TS!" });
});

app.listen(port, () => {
  console.log(`Application is running on port ${port}.`);
});
