const express = require("express");
require("dotenv").config();
const port = process.env.PORT || 3000;
const colors = require("colors");
const cors = require("cors");
const schema = require("./schema/schema");
const { graphqlHTTP } = require("express-graphql");
const connectDB = require("./config/db");

const app = express();
// Connect to Database
connectDB();

app.use(cors());

app.use(
  "/graphql",
  graphqlHTTP({
    schema,
    graphiql: true,
  })
);

app.listen(port, console.log(`listening to ${port}`));
