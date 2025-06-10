from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import mysql.connector

app = FastAPI()

# Serve static files (index.html)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_homepage():
    return FileResponse("static/index.html")

# Database connection details
DB_CONFIG = {
    "host": "172.17.168.79",
    "user": "Mahi",
    "password": "Mahi@1992",
    "database": "restaurant_db"
}

@app.get("/get_restaurants")
def get_restaurants():
    db = mysql.connector.connect(**DB_CONFIG)
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT Restaurant_ID, Restaurant_Name FROM Restaurants")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

@app.post("/add_order")
def add_order(
    Restaurant_ID: int = Form(...),
    Food_Item: str = Form(...),
    Quantity: int = Form(1),  # Default quantity = 1
    Payment_Method: str = Form(...)
):
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()

        # Insert order into database
        query = "INSERT INTO Orders (Restaurant_ID, Food_Item, Quantity, Payment_Method, Order_Date, Status) VALUES (%s, %s, %s, %s, NOW(), 'Open')"
        cursor.execute(query, (Restaurant_ID, Food_Item, Quantity, Payment_Method))
        db.commit()

        cursor.close()
        db.close()

        return {"message": "Order placed successfully!"}
    
    except mysql.connector.Error as err:
        return {"error": f"Database error: {err}"}

@app.get("/get_food_items")
def get_food_items():
    db = mysql.connector.connect(**DB_CONFIG)
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT Food_Item FROM Menu")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

@app.get("/order_status")
def get_order_status():
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor(dictionary=True)

        # Fetch the latest order details
        cursor.execute("""
            SELECT Order_ID, Order_Date, Status, Done_Time
            FROM Orders ORDER BY Order_Date DESC LIMIT 1
        """)
        data = cursor.fetchone()

        cursor.close()
        db.close()

        # Ensure response format
        return {
            "order_number": data["Order_ID"] if data else "---",
            "open_time": data["Order_Date"].strftime("%Y-%m-%d %H:%M:%S") if data else "---",
            "done_time": data["Done_Time"].strftime("%Y-%m-%d %H:%M:%S") if data and data["Done_Time"] else "---",
            "status": data["Status"] if data else "Open"
        }

    except mysql.connector.Error as err:
        return {"error": f"Database error: {err}"}
    
@app.post("/update_order_status")
def update_order_status(
    order_id: int = Form(...),
    new_status: str = Form(...)
):
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()

        # Update order status and set done time when closed
        if new_status in ["Closed", "Cancelled"]:
            query = "UPDATE Orders SET Status = %s, Done_Time = NOW() WHERE Order_ID = %s"
        else:
            query = "UPDATE Orders SET Status = %s WHERE Order_ID = %s"

        cursor.execute(query, (new_status, order_id))
        db.commit()

        cursor.close()
        db.close()

        return {"message": f"Order {order_id} updated to {new_status} successfully!"}
    
    except mysql.connector.Error as err:
        return {"error": f"Database error: {err}"}
    
@app.get("/open_orders")
def get_open_orders():
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor(dictionary=True)

        cursor.execute("""
            SELECT Order_ID, Order_Date FROM Orders 
            WHERE Status = 'Open' ORDER BY Order_Date ASC
        """)
        orders = cursor.fetchall()

        cursor.close()
        db.close()

        return {"open_orders": orders} if orders else {"open_orders": []}

    except mysql.connector.Error as err:
        return {"error": f"Database error: {err}"}