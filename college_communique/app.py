from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'jnqssnzeskfyjbyc'  # Required for flashing messages

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'atharvashivange04@gmail.com'
app.config['MAIL_PASSWORD'] = 'jnqssnzeskfyjbyc'  # Use an app password
app.config['MAIL_DEFAULT_SENDER'] = 'atharvashivange04@gmail.com'

mail = Mail(app)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle email sending
@app.route('/send-email', methods=['POST'])
def send_email():
    user_email = request.form.get('email')

    # Read the email content from the file
    try:
        with open('emailContent.txt', 'r') as file:
            email_content = file.read()
    except FileNotFoundError:
        flash('Error: Email content file not found.')
        return redirect('/')

    # Send the email
    try:
        msg = Message(subject="Welcome to the Newsletter!",
                      recipients=[user_email],
                      body=email_content)

        # Optionally add attachments
        msg.attach("Newsletter.pdf", "application/pdf", open("Newsletter.pdf", "rb").read())
        mail.send(msg)

        flash('Email sent successfully!')
    except Exception as e:
        print(f"Error: {e}")
        flash('Failed to send the email.')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
