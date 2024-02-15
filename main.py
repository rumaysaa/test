from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods=['get'])
def get():
    if 'X-Forwarded-For' in request.headers:
# The header can contain a comma-separated list of IPs, the first one being the client's IP
client_ips = request.headers['X-Forwarded-For'].split(',')
        client_ip = client_ips[0].strip()
    else:
        client_ip = request.remote_addr
    return f"Your real IP address is: {client_ip}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000,debug=True)
