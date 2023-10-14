css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #2b313e;
    color: white;
    text-align: center;
}

.footer p {
    margin: 0;
    padding: 1rem;
}

a:link {
        color: #00ffff;
        background-color: transparent;
        text-decoration: none;
        }

</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://iu.yesbhautik.co.in/wp-content/uploads/2022/10/yesbhautik_logo_50x50.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://youareunique.co.in/wp-content/uploads/2023/04/Bhautik-Bavadiya-Yesbhautik-Yesbhautik-Youareunique.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
"""

footer = """
        <div class="footer">
        <p>Made by <a href="https://yesbhautik.co.in">Yesbhautik</a> with <a href="https://streamlit.io">Streamlit</a></p>
        </div>
"""
        