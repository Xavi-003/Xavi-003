import urllib.request
import base64

def fetch_icon(name, urls):
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                if response.status != 200:
                    continue
                data = response.read()
                if len(data) < 50 or b'<svg' not in data:
                    continue
                
                b64 = base64.b64encode(data).decode('utf-8')
                return b64
        except Exception:
            continue
    return None

icons_to_fetch = {
    "mysql": ["https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"],
    "vite": ["https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vitejs/vitejs-original.svg"],
    "webpack": ["https://cdn.jsdelivr.net/gh/devicons/devicon/icons/webpack/webpack-original.svg"],
    "linux": ["https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg"],
    "vscode": ["https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"],
    "tensorflow": ["https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg"]
}

print("icons_data = {")
for name, urls in icons_to_fetch.items():
    b64 = fetch_icon(name, urls)
    if b64:
        print(f'    "{name}": "{b64}",')
    else:
        print(f'    "{name}": "FAILED",')
print("}")
