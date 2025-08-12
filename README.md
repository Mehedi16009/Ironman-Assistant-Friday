# 🦾 Iron Man Assistant – Friday


##📌 Overview
In 2020–2021, during the COVID-19 pandemic when ChatGPT was not yet available in my country, I developed Friday, a Python-based voice-activated virtual assistant inspired by Marvel's Iron Man.
This project was created during my academic gap years in my B.Sc. degree (2016–2022) as a way to continue learning and building my programming skills despite the global shutdown.
Although the assistant is built with relatively simple code, it was the result of intensive brainstorming, trial-and-error, and self-learning.

---------

A real-time demo of Friday was originally posted on my Facebook account here: [Facebook Demo Link](https://www.facebook.com/100007577161371/videos/2526623644266850/)

---------

# ✨ Features
Voice Recognition – Listens to user commands via microphone input.

Text-to-Speech – Responds in a human-like voice using pyttsx3.

Wikipedia Search – Fetches and summarizes information from Wikipedia.

Web Automation – Opens YouTube, Google, Stack Overflow, Google Maps, etc.

Time and Date – Reads out the current time.

Play Music – Plays music from a local directory.

Email Sending – Sends emails via SMTP.

Fun Interactions – Responds to casual greetings and questions in a conversational manner.


# 🛠️ Technologies Used
Python 3.x

[pyttsx3 – Text-to-Speech engine](https://pypi.org/project/pyttsx3/)

[SpeechRecognition – Speech-to-Text](https://pypi.org/project/SpeechRecognition/)

Wikipedia API – Wikipedia queries

smtplib – Sending emails

webbrowser – Opening websites

datetime & os – System operations

# 📥 Installation Code:

1. Clone this repository:
 

```bash
git clone https://github.com/yourusername/ironman-friday.git
cd ironman-friday
```



2. Install the dependencies:


```bash
pip install -r requirements.txt
```
3. Ensure your microphone is enabled and functional.

4. Run the assistant:

```bash
python friday.py
```




# ⚠️ Security Note:


This project was originally created for learning purposes.
If you wish to use the email functionality, never hardcode passwords in your code. Instead:

Use environment variables

Or a secure credentials manager



# 🎯 Possible Improvements:


Integration with OpenAI API for smarter responses

Adding face recognition for personalized interactions

Voice wake word detection

Cross-platform GUI interface


#  📬 Author Contact:

Md. Mehedi Hasan

Prospective Ph.D. Student

Lecturer, Dept. of Computer Science & Engineering

Global Institute of Information Technology (GIIT), Bangladesh

📧 Email: [mehedi.hasan.ict@mbstu.ac.bd](mehedi.hasan.ict@mbstu.ac.bd) | [mehedi.hasan.ict13@gmail.com](mehedi.hasan.ict13@gmail.com)

📞 Phone: +880 1789 113 669 | +880 1334 110 929

🌐 Portfolio: [My Website Link](https://md-mehedi-hasan-resume.vercel.app/)
