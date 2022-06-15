import fitz # install using: pip install PyMuPDF
from gtts import gTTS

with fitz.open("aaa.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()

print(text)

language = "en"

myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("example.mp3")
