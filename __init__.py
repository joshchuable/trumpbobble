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

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("contents.html", quantity_values=range(1,10), price=20)

if __name__ == "__main__":
	app.run(debug=True)


@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    if state == "MO":
        amount = subtotal * 1.425
    else:
        amount = subtotal

    customer = stripe.Customer.create(
        email='customer@example.com',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('thankyou.html', amount=amount)