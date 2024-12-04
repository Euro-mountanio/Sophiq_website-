from flask import Flask, render_template, redirect, flash, request
from flask_mail import Mail, Message

app = Flask(__name__, static_folder='static')
app.secret_key = "your_secret_key"

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'your_email_password'  # Your email password

mail = Mail(app)


@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/contacts" ,methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash("All fields are required!", "danger")
            return redirect(request.url)

        # Prepare and send email
        msg = Message(subject=f"Message from {name}",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['recipient_email@gmail.com'])  # Replace with your recipient email
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            mail.send(msg)
            flash("Message sent successfully!", "success")
        except Exception as e:
            flash(f"Failed to send message: {e}", "danger")

        return "Thank you for your message!"
    return render_template("contacts.html", title="contacts")
@app.route('/about', methods=['GET', 'POST'])
def about_page():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Process form data
        return "Form submitted successfully!"
    return render_template('about.html')

@app.route("/features")
def services():
    return render_template("features.html", title="features")



@app.route("/pricing")
def gallery():
    return render_template("pricing.html", title="pricing")

if __name__ == "__main__":
    app.run(debug=True)
