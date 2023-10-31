import nodemailer from 'nodemailer';
import User from '@/models/userModel';
import bcryptjs from 'bcryptjs';

export const sendEmail = async({email, emailType, userId}: any) => {
    try {
        // create a hashed token  
        const hashedToken = await bcryptjs.hash(userId.toString(), 10);

        if(emailType === "VERIFY"){
        await User.findByIdAndUpdate(userId, 
            {verifyToken: hashedToken,
            verifyTokenExpiry: Date.now() + 3600000})}
        
        else if(emailType === "RESET"){
            
            await User.findByIdAndUpdate(userId, 
            {forgotPasswordToken: hashedToken,
            forgotPasswordTokenExpiry: Date.now() + 3600000})

        }

        var transport = nodemailer.createTransport({
            host: "sandbox.smtp.mailtrap.io",
            port: 2525,
            auth: {
              user: "1a670b865d65db",
              pass: "4440d8cae591b9"
            }
          });

        const mailOptions = {
            from: 'sumanjeet0012@gmail.com',
            to: email,
            subject: emailType === "VERIFY" ? "Verify Email" : "Reset Password",
            html: `<p>Click <a href="${process.env.DOMAIN}/verifyemail?token=${hashedToken}">here<a/> to ${emailType === "VERIFY" ? "verify your email" : "reset your password"}
            or paste the link in the browser. ${process.env.DOMAIN}/verifyemail?token=${hashedToken}</p>`
        }
        
        const mailResponce = await transport.sendMail(mailOptions);
        return mailResponce;
        

    } catch (error: any) {
        throw new Error(error.message);
        
        
    }
}


