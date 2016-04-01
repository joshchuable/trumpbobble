from flask import Flask, request, render_template, make_response
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

@app.route('/charge/stripe/<amount>', methods=['POST'])
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

@app.route("/paypal/redirect")
def paypal_redirect():
    kw = {
        'amt': '10.00',
        'currencycode': 'USD',
        'returnurl': url_for('paypal_confirm', _external=True),
        'cancelurl': url_for('paypal_cancel', _external=True),
        'paymentaction': 'Sale'
    }

    setexp_response = interface.set_express_checkout(**kw)
    return redirect(interface.generate_express_checkout_redirect_url(setexp_response.token))     

@app.route("/paypal/confirm")
def paypal_confirm():
    getexp_response = interface.get_express_checkout_details(token=request.args.get('token', ''))

    if getexp_response['ACK'] == 'Success':
        return """
            Everything looks good! <br />
            <a href="%s">Click here to complete the payment.</a>
        """ % url_for('paypal_do', token=getexp_response['TOKEN'])
    else:
        return """
            Oh noes! PayPal returned an error code. <br />
            <pre>
                %s
            </pre>
            Click <a href="%s">here</a> to try again.
        """ % (getexp_response['ACK'], url_for('index'))


@app.route("/paypal/do/<string:token>")
def paypal_do(token):
    getexp_response = interface.get_express_checkout_details(token=token)
    kw = {
        'amt': getexp_response['AMT'],
        'paymentaction': 'Sale',
        'payerid': getexp_response['PAYERID'],
        'token': token,
        'currencycode': getexp_response['CURRENCYCODE']
    }
    interface.do_express_checkout_payment(**kw)   

    return redirect(url_for('paypal_status', token=kw['token']))

@app.route("/paypal/status/<string:token>")
def paypal_status(token):
    checkout_response = interface.get_express_checkout_details(token=token)

    if checkout_response['CHECKOUTSTATUS'] == 'PaymentActionCompleted':
        # Here you would update a database record.
        return """
            Awesome! Thank you for your %s %s purchase.
        """ % (checkout_response['AMT'], checkout_response['CURRENCYCODE'])
    else:
        return """
            Oh no! PayPal doesn't acknowledge the transaction. Here's the status:
            <pre>
                %s
            </pre>
        """ % checkout_response['CHECKOUTSTATUS']

@app.route("/paypal/cancel")
def paypal_cancel():
    return redirect(url_for('index'))

@app.route("/terms")
def terms():
    return render_template("terms.html")

if __name__ == "__main__":
	app.run(debug=True)



