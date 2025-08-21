from utils.payfast import generate_signature, build_payment_url
import os

def handler(request):
    if request.method != "POST":
        return {"error": "Invalid method"}, 405
    
    data = request.json
    MERCHANT_ID = os.getenv("MERCHANT_ID")
    MERCHANT_KEY = os.getenv("MERCHANT_KEY")

    payment_data = {
        "merchant_id": MERCHANT_ID,
        "merchant_key": MERCHANT_KEY,
        "return_url": os.getenv("RETURN_URL"),
        "cancel_url": os.getenv("CANCEL_URL"),
        "notify_url": os.getenv("NOTIFY_URL"),
        "amount": f"{data['amount']:.2f}",
        "item_name": data["itemName"],
        "custom_str1": data["passType"],
        "custom_str2": data["userId"]
    }

    payment_data["signature"] = generate_signature(payment_data)
    payment_url = build_payment_url("https://sandbox.payfast.co.za/eng/process", payment_data)
    
    return ({"paymentUrl": payment_url})




