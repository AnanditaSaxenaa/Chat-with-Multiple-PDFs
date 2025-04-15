css = '''
<style>
.chat-message {
  display: flex;
  padding: 1.5rem;
  border-radius: 0.5rem;
  margin-bottom: 1rem;
}

.chat-message.user {
  background-color: #2b313e;
}

.chat-message.bot {
  background-color: #475063;
}

.chat-message .avatar {
  width: 15%;
}

.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}

.chat-message .message {
  width: 85%;
  padding: 0 1.5rem;
  color: #fff;
}
</style>
'''
from pathlib import Path
import streamlit as st

# Put this at the top of your file (after imports)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

import base64

image_path = "graident-ai-robot-vectorart.png"
image_base64 = get_base64_of_bin_file(image_path)

bot_template = f'''
<div class="chat-message bot"> 
  
  <div class="message">{{{{MSG}}}}</div> 
</div>
'''



user_template = '''
<div class="chat-message user"> 
  
  <div class="message">{{MSG}}</div> 
</div>
'''
