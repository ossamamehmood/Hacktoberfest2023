import express from "express";
import axios from "axios";
import bodyParser from "body-parser";

const app = express();
app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));
const port=3000;
const bored_url="https://bored-api.appbrewery.com/random";
const animal_url="http://shibe.online/api/";
const animal=["cats","birds","shibes"];
const joke_url="https://v2.jokeapi.dev/joke/Any?format=txt&amount=1";
app.get("/",(req,res)=>
{
    res.render("index.ejs");
});
app.get("/bored",async(req,res)=>
{
    try {
        const response = await axios.get(bored_url);
        const result = response.data;
        res.render("bored_activity.ejs", { data: result });
      } catch (error) {
        console.error("Failed to make request:", error.message);
        res.render("index.ejs", {
          error: error.message,
        });
      }
});
app.post("/activitytype", async (req, res) => {
  var i;
  const type=req.body.type;
  const part=req.body.participants;

  try {
    const response = await axios.get(`https://bored-api.appbrewery.com/filter?type=${type}&participants=${part}`);
    const result = response.data;
    i=Math.floor(Math.random()*result.length);
    res.render("bored_activity.ejs", { data: result[i]});
  } catch (error) {
    console.error("Failed to make request:", error.message);
    res.render("bored_activity.ejs", {
      error: error.message,
    });
  }
});
app.get("/animal",async(req,res)=>
{
    let i=Math.floor(Math.random()*3);
    try {
        const response = await axios.get(animal_url+animal[i]);
        const result = response.data;
        res.render("animal.ejs", { data: result[0] });
        console.log(result[0]);
      } catch (error) {
        console.error("Failed to make request:", error.message);
        res.render("index.ejs", {
          error: error.message,
        });
      }
});
app.post("/animaltype",async(req,res)=>
{
  var type=req.body.choice;
  try {
    console.log(animal_url+type);
    const response = await axios.get(animal_url+type);
    const result=response.data;
    res.render("animal.ejs", { data: result[0]});
  } catch (error) {
    console.error("Failed to make request:", error.message);
    res.render("animal.ejs", {
      error: error.message,
    });
  }
});

app.listen(port,()=>{
    console.log(`Server running on port: ${port}`);
})
