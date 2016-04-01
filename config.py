from paypal import PayPalConfig
from paypal import PayPalInterface

config = PayPalConfig(API_USERNAME = "admin-facilitator_api1.trumpbobble.com",
                      API_PASSWORD = "VHD5LBSTVY5F2LVY",
                      API_SIGNATURE = "AFcWxV21C7fd0v3bYYYRCpSSRl31A31AGwDGKoQXB-ZlN1VRvKP2zDyu",
                      DEBUG_LEVEL=0)

interface = PayPalInterface(config=config)
