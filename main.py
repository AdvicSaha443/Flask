from flask import Flask, json, jsonify, request

app = Flask(__name__)

#creating the array of task
contacts = [{
    "id": 1,
    "Name": u"Advic",
    "Contact": u"132456",
    "done": False
},{
    "id": 2,
    "Name": u"Advic 2",
    "Contact": u"132465",
    "done": False
}]

@app.route('/add_data', methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please Provide The Data"
        }, 400)
    contact = {
        "id": contacts[-1]["id"]+1,
        "Name": request.json["Name"],
        "Contact": request.json.get("Contact", ""),
        "done": False
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "Task Added Successfuly"
    })

@app.route("/get_data")
def get_task():
    return jsonify({
        "data":contacts
    })

if __name__ == "__main__":
    app.run(debug=True)