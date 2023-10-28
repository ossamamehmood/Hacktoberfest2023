const express = require('express');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt'); //for password hashing

//Registration Route
app.post('/register',async (req,res) =>{
    const {username,email,password} = req.body;

    //Hash the password before storing it
    const hashedPassword = await bcrypt.hash(password,10);

    const sql = 'INSERT INTO registration (username, email, password) VALUES (?,?,?)';
    db.query(sql,[username,email,hashedPassword],(err,result) =>{
        if(err){
            console.error('Error registering user: ', err);
            res.status(500).json({error: 'An error occured'});
        }
        else{
            res.status(201).json({messsage : "An user registered successfully"});
        }
    });
});

app.get('/register', (req, res) => {
    res.send('This endpoint is for user registration. Use a POST request to register a user.');
  });
  
