import urllib.request
import base64

icons = {
    "node": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg",
    "docker": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg",
    "go": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original-wordmark.svg",
    "mongodb": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg",
    "typescript": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg",
    "nextjs": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg",
    "redis": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg",
    "javascript": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
    "bun": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bun/bun-original.svg",
    "grpc": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/grpc/grpc-original.svg" # trying standard path, might fail
}

print("icons_data = {")
for name, url in icons.items():
    try:
        # Using jsdelivr as it's often more reliable/faster for raw github content
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = response.read()
            if len(data) < 100: # Suspiciously small
                print(f'    "{name}": "", # Warning: Data too small')
            else:
                b64 = base64.b64encode(data).decode('utf-8')
                print(f'    "{name}": "{b64}",')
    except Exception as e:
        print(f'    "{name}": "", # Error: {e}')
print("}")
