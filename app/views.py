"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from .form import ContactForm
from app import mail
from flask_mail import Message

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")
###
# The functions below should be applicable to all Flask apps.
###

@app.route("/contact", methods = ["GET","POST"])
def contact():
   form = ContactForm()
   form_name = "Contact Form"
   description = "Please enter information below to contact owner of site"
   name1_explain = "Please enter your First name"
   name2_explain = "Please enter your Last name"
   email_explain = "Please enter your Email"
   sub_explain = "Please enter your Subject"
   message_explain = "Please enter your message"
   required = "(Required)"
   Firstname = form.Firstname.data
   Lastname = form.Lastname.data
   Email = form.Email.data
   Subject = form.Subject.data
   your_message = form.your_message.data
   if request.method == "POST" and form.validate():
       flash("Successfully Completed")
       msg = Message(form.Subject.data, sender = form.Firstname.data, recipients = [""])
       msg.body = form.your_message.data
       mail.send(msg)
       return render_template("my_result.html", Firstname = Firstname, Lastname = Lastname, Email = Email, Subject = Subject, your_message = your_message)

   flash_errors(form)
   return render_template("contact.html", form = form, Firstname = Firstname, Lastname = Lastname, Email = Email, Subject = Subject, your_message = your_message, form_name = form_name, description = description, name1_explain = name1_explain, name2_explain = name2_explain, email_explain = email_explain, sub_explain = sub_explain, message_explain = message_explain, required = required)


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
