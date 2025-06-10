# restaurant-order-system
this project for restaurant order system, we can initiate order from frontend, close and cancel order and all open order show in front

Files-
server.py for - frontend
app.py for backend(data fetch from db and insert)
index.html for page layout and dromdown.

For Db-
need to create below tables -
![image](https://github.com/user-attachments/assets/088a4a8b-0722-4022-addf-cf65257c28a4)
![image](https://github.com/user-attachments/assets/7a350513-86b9-441e-a086-3c31c9dd7dab)

![image](https://github.com/user-attachments/assets/be129fae-6dae-4999-a483-5d4c5fca8223)

uvicorn app:app --host 127.0.0.1 --port 8000 --reload > server.log 2>&1  ---initiate frontend api  --check sudo lsof -i :8000  find Ip for this port
curl http://127.0.0.1:8000/get_restaurants-- validate data pick or not if pick then run for backend script for data pick
python3 server.py  --- for backend data pick from Db  -- check netstat -tuln |grep 8080  check 0.0.0.0:8080 find
http://127.0.0.1:8000/static/index.html  -- for main page (if above all validation done then data show on frontnd)




[Restaurant-order-system-document.pptx](https://github.com/user-attachments/files/20670393/Restaurant-order-system-document.pptx)
