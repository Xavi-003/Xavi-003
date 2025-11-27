import requests
import base64

icons = {
    "react": "https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original.svg",
    "node": "https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original.svg",
    "python": "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg",
    "docker": "https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg"
}

for name, url in icons.items():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            b64 = base64.b64encode(response.content).decode('utf-8')
            print(f"{name}: data:image/svg+xml;base64,{b64}")
        else:
            print(f"Failed to fetch {name}")
    except Exception as e:
        print(f"Error fetching {name}: {e}")
