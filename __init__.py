from flask import Flask, request, render_template, make_response
from io import StringIO
import datetime
import stripe
import os

stripe_keys = {
    'secret_key': "sk_test_LvcrElgTuPTXOYn06XtSshgN",
    'publishable_key': "pk_test_gZGO4hFofN2dMsUz5cAexmAz"
}

stripe.api_key = stripe_keys['secret_key']

#mo_zip =

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("contents.html", quantity_values=range(1,10), price=20)

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
        return render_template('error.html', error="We only take orders from the continental U.S. at this time. For international inquiries, please email us at contact@trumpbobble.com")
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

if __name__ == "__main__":
	app.run(debug=True)

