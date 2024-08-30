import webbrowser

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

gmail_url = "https://mail.google.com/"

webbrowser.get(chrome_path).open(gmail_url)
