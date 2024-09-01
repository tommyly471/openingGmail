import webbrowser

chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

gmail_url = "https://mail.google.com/"

# Use the webbrowser module to open Gmail with Chrome
webbrowser.get(f'"{chrome_path}" %s').open(gmail_url)
