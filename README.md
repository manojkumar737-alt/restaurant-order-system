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

create tabe query-
CREATE TABLE `Menu` (
  `Food_Item` varchar(100) NOT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`Food_Item`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `Orders` (
  `Order_ID` int NOT NULL AUTO_INCREMENT,
  `Order_Date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Restaurant_ID` varchar(20) DEFAULT NULL,
  `Food_Item` varchar(100) DEFAULT NULL,
  `Quantity` int NOT NULL DEFAULT '1',
  `Status` varchar(50) DEFAULT NULL,
  `Payment_Method` varchar(50) DEFAULT NULL,
  `Done_Time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`Order_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Restaurants` (
  `Restaurant_ID` varchar(20) NOT NULL,
  `Restaurant_Name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Restaurant_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


[Restaurant-order-system-document.pptx](https://github.com/user-attachments/files/20670393/Restaurant-order-system-document.pptx)
