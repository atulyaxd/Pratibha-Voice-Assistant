# Pratibha-Voice-Assistant

A simple voice operated python assistant for simple tasks and time-pass.

## Libraries
* [Pyttsx3](https://pypi.org/project/pyttsx3/)
* [Speech Recognition](https://pypi.org/project/SpeechRecognition/)
* [PyAudio](https://pypi.org/project/PyAudio/)
* [Wolfram Alpha](https://pypi.org/project/wolframalpha/)
* [Wikipedia](pip install wikipedia)
* [Requests](https://pypi.org/project/requests/)

## for windows
* clone my repo
* change the directory to root folder, `cd Pratibha-Voice-Assistant`.
* install the requirements, `pip install -r requirements.txt`.
* for **pyaudio** download the .whl file [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it.
* explore the [code](https://github.com/itsatulya/Pratibha-Voice-Assistant/blob/d79340004db1be5360e550fdaf26a934b9f425eb/pratibha.py), Understood ?
* run the code, `python pratibha.py`.

## for raspberry pi
* clone my repo
* change the directory to root folder, `cd Pratibha-Voice-Assistant`.
* install the requirements, `pip3 install -r requirements.txt`.
* installing **pyaudio**:
    * `sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0`
    * `sudo apt-get install ffmpeg libav-tools`
    * `sudo pip install pyaudio` 
* setup your microphone and speaker using [Google Dev Docs](https://developers.google.com/assistant/sdk/guides/service/python/embed/audio).
* explore the [code](https://github.com/itsatulya/Pratibha-Voice-Assistant/blob/d79340004db1be5360e550fdaf26a934b9f425eb/pratibha.py), Understood ?
* run the code, `python pratibha.py`

## Functions
* Wikipedia search - **[category] + [subject]**, ex: monument Taj Mahal
* Google search - **[subject]**, ex: Taj Mahal
* Study timer - **[study]**
* Calculator - **[calculate] + [problem]**, ex: add 2 + 2

## Additional
* generate your [wolframaplha](https://www.wolframalpha.com/) api id [here](https://account.wolfram.com/login/oauth2/sign-in) and paste it in the called variable, here **api_id**.
* **Virtual Environment** : 
   * `python3 -m venv venv` for installation, 
   * `source venv/bin/activate` for activation.  
