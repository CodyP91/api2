import flask
import mariadb
import json

app = flask.Flask(__name__)

# Setup MariaDB connection
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'password',
    'database': 'api2'
}

# A function to handle database connection and procedure execution.
def execute_procedure(procedure, *args):
    conn = mariadb.connect(user="your_user", password="your_password", host="localhost", port=3306, database="your_db")
    cursor = conn.cursor()
    cursor.callproc(procedure, args)
    result = [item for item in cursor.fetchall()]
    cursor.close()
    conn.close()
    return result

@app.route('/api/item', methods=['GET'])
def get_items():
    items = execute_procedure('GetAllItems')
    return flask.Response(json.dumps(items), mimetype='application/json')

@app.route('/api/item', methods=['POST'])
def insert_item():
    name = flask.request.json['name']
    description = flask.request.json['description']
    price = flask.request.json['price']
    new_item_id = execute_procedure('InsertNewItem', name, description, price)
    return flask.Response(json.dumps(new_item_id), mimetype='application/json')

@app.route('/api/item', methods=['PATCH'])
def update_item():
    item_id = flask.request.json['id']
    new_price = flask.request.json['price']
    updated_price = execute_procedure('UpdateItemPrice', item_id, new_price)
    return flask.Response(json.dumps(updated_price), mimetype='application/json')

@app.route('/api/item', methods=['DELETE'])
def delete_item():
    item_id = flask.request.json['id']
    execute_procedure('DeleteItem', item_id)
    return flask.Response(json.dumps({'status': 'success'}), mimetype='application/json')

@app.route('/api/employee', methods=['GET'])
def get_employee():
    employee_id = flask.request.args.get('id')
    employee_details = execute_procedure('GetEmployeeDetails', employee_id)
    return flask.Response(json.dumps(employee_details), mimetype='application/json')

@app.route('/api/employee', methods=['POST'])
def insert_employee():
    name = flask.request.json['name']
    position = flask.request.json['position']
    hourly_wage = flask.request.json['hourly_wage']
    new_employee_id = execute_procedure('InsertNewEmployee', name, position, hourly_wage)
    return flask.Response(json.dumps(new_employee_id), mimetype='application/json')

@app.route('/api/employee', methods=['PATCH'])
def update_employee():
    employee_id = flask.request.json['id']
    new_wage = flask.request.json['hourly_wage']
    updated_wage = execute_procedure('UpdateEmployeeWage', employee_id, new_wage)
    return flask.Response(json.dumps(updated_wage), mimetype='application/json')

@app.route('/api/employee', methods=['DELETE'])
def delete_employee():
    employee_id = flask.request.json['id']
    execute_procedure('DeleteEmployee', employee_id)
    return flask.Response(json.dumps({'status': 'success'}), mimetype='application/json')

if __name__ == '__main__':
    app.run()
