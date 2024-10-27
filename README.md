# Chatbot_With_UI

A simple chatbot with a Flask web interface, designed to provide dynamic responses using OpenAI's API for language understanding. This chatbot integrates retrieval-augmented generation (RAG) to ensure up-to-date responses, leveraging current information from external sources like the LHC Blogpost.

### Tools Used
1. **LangChain Framework**: For query synthesis and response generation
2. **Flask**: Provides the web GUI
3. **GPT-3.5**: Powers natural language understanding
4. **LHC Blogpost**: Used for real-time information retrieval ([link to source](https://www.space.com/large-hadron-collider-particle-accelerator))

---

### **Steps to Run**

1. **Download the Repository**
   - Clone or download this GitHub repository to your local machine.

2. **Create a Virtual Environment**
   - Run the following command:
     ```bash
     python -m venv venv
     ```

3. **Activate the Virtual Environment**
   - For Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     venv/Scripts/activate
     ```

4. **Install Dependencies**
   - Install all necessary packages by running:
     ```bash
     pip install -r requirements.txt
     ```

5. **Add OpenAI API Key**
   - In the project root, create a `.env` file and add your OpenAI API key in the following format:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

6. **Run the Application**
   - Launch the Flask app by executing:
     ```bash
     python app.py
     ```

7. **Access the Application**
   - The app should now be accessible in your web browser. Make sure it is running on a custom port to avoid conflicts with the default localhost port.

---

### **Additional Notes**

- Ensure that all required permissions and network settings allow for the app to run and retrieve data as needed.
- Review and modify `app.py` if necessary to set a specific port or additional configurations.

---

<br>

<p align="center">
<img align="center" width="725" alt="no-image" src="https://github.com/makaveli006/ChatRex/blob/f517271f9d157fdcb6cd4162f5676dc57729d673/assets/chatbox.png" >
</p>
