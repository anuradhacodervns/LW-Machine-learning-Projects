from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'anumaurya2690@gmail.com'  
app.config['MAIL_PASSWORD'] = '12345'  

mail = Mail(app)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    subject = data['subject']
    recipient = data['recipient']
    body = data['body']

    msg = Message(subject, recipients=[recipient], body=body, sender='mauryaanuradha292@gmail.com')
    mail.send(msg)
    
    return jsonify({'message': 'Email sent successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
