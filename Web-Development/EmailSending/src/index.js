const nodemailer = require('nodemailer')

const receipient = "<Receipient email>";
const subject = "This is a mail from nodemailer";

const transporter = nodemailer.createTransport({
    service: 'hotmail',
    auth: {
        user:'<Senders Email>',
        pass: '<Senders Password>'
    }
});

const mailOptions = {
    from: '<Senders Email>',
    to: receipient,
    subject: subject,
    text: 'Hello from world beyond the edge!'
};

transporter.sendMail(mailOptions, function(error, info){
    if(error){
        console.log(error);
        // res.status(500).send("Error sending email")
    }else{
        console.log('Email sent: ' + info.response)
        // res.status(200).send("Email sent")
    }
});
