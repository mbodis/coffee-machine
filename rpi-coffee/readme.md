
1. rpi clean install 

2. enable ssh on RPI

```
sudo ifconfig 
```

3. copy script via SCP to RPI
```
sshpass -p 'PASS' scp ./rpi-coffee/*.py USER@192.168.0.38:/home/USER/Documents/coffee
```

4. create file: /etc/systemd/system/my_coffee.service 
```
[Unit]
Description=My Coffee Project
After=network.target

[Service]
WorkingDirectory=/home/USER/Documents/coffee/
ExecStart=python /home/USER/Documents/coffee/coffee_server.py
Restart=always

[Install]
WantedBy=multi-user.target
```

5. register script on OS level as service
```
sudo systemctl start my_coffee
sudo systemctl status my_coffee
sudo systemctl stop my_coffee
```

6. enable script on startup
```
sudo systemctl enable my_coffee
```

