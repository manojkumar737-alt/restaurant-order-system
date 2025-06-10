#uvicorn app:app --host 127.0.0.1 --port 8000 --reload
#curl http://127.0.0.1:8000/get_restaurants-- validate data pick or not
#python3 server.py
#http://127.0.0.1:8000/static/index.html  -- for main page
import mysql.connector
import ssl
import json
ssl_context = ssl.create_default_context()


from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
                 
            print(f"🔍 Received request for: {self.path}")  # Debugging output
            if self.path.strip() == "/":
                response = json.dumps({"message": "Welcome to the Restaurant API!"})
            # Database connection for other endpoints

            db = mysql.connector.connect(host="172.17.168.79", user="Mahi", password="Mahi@1992", database="restaurant_db", ssl_disabled=True)
            cursor = db.cursor(dictionary=True)
        # Fetch restaurant data
                       
           
            if self.path == "/get_restaurants":
                cursor.execute("SELECT Restaurant_ID, Restaurant_Name FROM Restaurants")
                restaurants = cursor.fetchall()  # Assign fetched data
                response = json.dumps(restaurants)  # Use it in response

        # Fetch food items data

            elif self.path == "/get_food_items":
                cursor.execute("SELECT Food_Item FROM Menu")
                food_items = cursor.fetchall()  # Assign fetched data
                response = json.dumps(food_items)  # Use it in response

            else:
                print(f"⚠️ Invalid request: {self.path}")  # Debugging output
                response = json.dumps({"message": "Welcome to the Restaurant API!"})

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response.encode())
        except BrokenPipeError:
            print("⚠️ Client disconnected before response was sent.")

# Initialize and run server

server = HTTPServer(("0.0.0.0", 8080), MyHandler)
print("Server running on http://localhost:8080")
server.serve_forever()