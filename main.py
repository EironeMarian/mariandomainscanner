import requests, json, socket

print("███╗░░░███╗░█████╗░██████╗░██╗░█████╗░███╗░░██╗\n████╗░████║██╔══██╗██╔══██╗██║██╔══██╗████╗░██║\n██╔████╔██║███████║██████╔╝██║███████║██╔██╗██║\n██║╚██╔╝██║██╔══██║██╔══██╗██║██╔══██║██║╚████║\n██║░╚═╝░██║██║░░██║██║░░██║██║██║░░██║██║░╚███║\n╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚══╝")
domain = input('enter a domain: ')

file = open('subdomains.txt')

con = file.read()
subdomains = con.splitlines()

for subdomain in subdomains:
  try:
    url = f"http://{subdomain}.{domain}"
   
    requests.get(url)
    


  except requests.ConnectionError:
    pass
  else:
    ip = socket.gethostbyname(f"{subdomain}.{domain}")
    res = requests.get(f"http://ip-api.com/json/{ip}?fields=49664")
    res_data = json.loads(res.text)
    print("Bingo! domain:", url, ip, res_data["isp"])
