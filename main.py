from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

@app.route('/ip', methods=['POST'])
def receive_local_ip():
    data = request.json
    client_ip = data.get('ip')
    # Do whatever you need to do with the client's local IP address
    print("Client's local IP address:", client_ip)
    return jsonify({'message': 'Local IP address received successfully'})

@app.route('/',methods=['get'])
def main():
    return render_template('page.html')

if __name__ == '__main__':
    app.run(debug=True)
