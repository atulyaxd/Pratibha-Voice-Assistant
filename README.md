# Pratibha-Voice-Assistant

To use this tool in **Terminal**

1. clone repository using `git clone https://github.com/imatulya21/Pratibha-Voice-Assistant.git`. 
2. Add a Virtual Environment `python3 -m venv venv` **(If needed)**
3. Activate the Virtual Environment `source venv/bin/activate` **(If needed)**
4. change the directory using `cd Pratibha-Voice-Assistant`. 
5. install the libraries using `pip install -r requirements.txt`.
6. run the code using `python3 pratibha.py`.

## Libraries and API's used

1. SpeechRecognition 
2. pyttsx3
3. pyaudio for windows (if the pip was unable to install, consider this website https://www.lfd.uci.edu/~gohlke/pythonlibs/ and install PyAudio wheel file)
4. **additional** pyaudio for raspberry pi  `sudo apt-get install python-pyaudio python3-pyaudio`.  
5. wolframalpha (get your api_id from here https://account.wolfram.com/login/oauth2/sign-in and paste it in the required variables)
6. requests
7. datetime
8. time

## Configuration

If you are using this in windows then no extra configuration is needed, but if you are planning to use this in raspberry pi then kindly configure the Raspberry Pi for more context consider https://developers.google.com/assistant/sdk/guides/service/python/embed/audio for configuring Raspberry Pi 3

