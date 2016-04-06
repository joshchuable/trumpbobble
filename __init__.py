import sys
from flask import Flask, request, render_template, make_response
from io import StringIO
from pscripts.send_email import ContactForm
from flask_mail import Mail, Message
import datetime
import stripe
import os

stripe_keys = {
    'secret_key': "sk_test_BnQz5NQauCGFT5lWsQROeTX6",
    'publishable_key': "pk_test_U2NHMtMm8NmjPT9m8ZWyjf8t"
}

stripe.api_key = stripe_keys['secret_key']

#mo_zip =

app = Flask(__name__)
app.secret_key = 'the_R4nD0M_Things___4keys--true'
# Email Configs
app.config['MAIL_SERVER'] = 'smtp.zoho.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'admin@trumpbobble.com'
app.config['MAIL_PASSWORD'] = 'taoist-terrier-sleeve-tingly-debate'
# Mailer
mail = Mail(app)

@app.route('/')
def index():
	return render_template('contents.html')

@app.route('/checkout/')
def checkout():
    return render_template('checkout-form.html', key=stripe_keys['publishable_key'])

@app.route('/contact/', methods=['POST','GET'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
        return 'Please fill out all sections of the form and resubmit.'
    else:
        msg = Message(form.subject.data, sender='admin@trumpbobble.com', recipients=['admin@trumpbobble.com','rye@trumpbobble.com'])
        msg.body = """
        From: %s <%s>
        %s
        """ % (form.name.data, form.email.data, form.message.data)
        mail.send(msg)

        return 'Message sent! Hit back to return to the site.'

  elif request.method == 'GET':
    return render_template('contact.html', form=form)

@app.route('/charge/<amount>', methods=['POST'])
def charge(amount):
    # Amount in cents
    token = request.form['stripeToken']
    dollar_amount = int(amount)/100
    country = request.form['stripeShippingAddressCountry']
    state = request.form['stripeShippingAddressState']
    customer = stripe.Customer.create(
                source=token
            )
    if country not in ["US", "United States"] or state in ['Alaska','AK','Hawaii','HI']:
        return render_template('error.html', error="Sorry, we only take orders from the continental U.S. at this time. Your card will not be charged. For international inquiries, please email us at contact@trumpbobble.com")
    else:
        try:
            charge = stripe.Charge.create(
                customer=customer.id,
                amount=amount,
                currency='usd',
            )

            return render_template('thankyou.html',amount=dollar_amount)
        except stripe.CardError:
            return render_template('error.html', error="Your card was declined. Please try again or call your credit card company.")

@app.route("/terms")
def terms():
    return render_template("terms.html")

if __name__ == "__main__":
	app.run(debug=True)



