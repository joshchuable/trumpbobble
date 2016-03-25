from flask import Flask, request, render_template, make_response
#from flask.ext.sqlalchemy import SQLAlchemy
from io import StringIO
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

@app.route("/")
def index():
	return render_template("contents.html")

@app.route("/checkout/")
def checkout():
    return render_template("checkout-form.html", key=stripe_keys['publishable_key'])

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

            return render_template('error.html', error="Sorry, we're all out of stock. Leave us your email and we'll let you know when we have move available" )
        except stripe.CardError:
            return render_template('error.html', error="Your card was declined. Please try again or call your credit card company.")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
	app.run(debug=True)



