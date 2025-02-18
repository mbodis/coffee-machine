
1. rpi clean install 

2. on RPI enable ssh and set wifi

```
sudo raspi-config 
```

3. reboot 
```
sudo reboot
```

4. ssh to RPI and create new folder
```
mkdir ~/coffee
```

5. copy script via SCP to RPI
```
sshpass -p 'PASS' scp ./*.py USER@192.168.0.38:/home/USER/coffee
```
6. make sure files have `+x`
```
chmod +x coffee_*
```

7. install dependencies
```
sudo apt install python3-pip
sudo pip install flask
```

8. create file: /etc/systemd/system/my_coffee.service

```
sudo touch /etc/systemd/system/my_coffee.service
sudo chmod +x /etc/systemd/system/my_coffee.service
```
with content:
```
[Unit]
Description=My Coffee Project
After=network.target

[Service]
WorkingDirectory=/home/USER/coffee/
ExecStart=python /home/USER/coffee/coffee_server.py
Restart=always

[Install]
WantedBy=multi-user.target
```

9. register script on OS level as service
```
sudo systemctl start my_coffee
sudo systemctl status my_coffee
sudo systemctl stop my_coffee
```

10. enable script on startup
```
sudo systemctl enable my_coffee
```

