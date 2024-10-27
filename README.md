# Chatbot_With_UI

Simple chatbot with a flask web interface.

The chatbot leverages OpenAI API for user query comprehension complemented with RAG for up-to-date information retrieval.

Tools Used: 
  1. LangChain framework: for user query synthesis and reply generation
  2. Flask: for web gui
  3. GPT-3.5: for language understanding
  4. LHC Blogpost: for current information retrieval; [Link](https://www.space.com/large-hadron-collider-particle-accelerator)

<br>


### **Steps to run:**

1. Download this github repository
2. Create a virtual environment

     `python -m venv venv`
3. Activate the virtual environment

    `source venv/bin/activate` or `venv/Scripts/activate` [for Windows]

4. Install the requirements

   `pip install -r requirements.txt`

5. Add your OpenAI API key in a .env file
6. On the terminal run the command below 

     `python app.py`

7. App should not be running on localhost default port

<br>

<p align="center">
<img align="center" width="725" alt="no-image" src="https://github.com/makaveli006/ChatRex/blob/f517271f9d157fdcb6cd4162f5676dc57729d673/assets/chatbox.png" >
</p>
