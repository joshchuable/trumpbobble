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

@app.route("/confirmation/")
def confirmation():
    #if zip in 
    return render_template("confirmation.html", quantity=1, price=20, key=stripe_keys['publishable_key'])

@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    customer = stripe.Customer.create(
        email='customer@example.com',
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        currency='usd',
    )

    return render_template('thankyou.html', amount=amount)

if __name__ == "__main__":
	app.run(debug=True)

