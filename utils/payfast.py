import hashlib, urllib.parse

def generate_signature(payment_data):
    pf_string = "&".join([f"{key}={urllib.parse.quote_plus(str(value))}" for key, value in payment_data.items()])
    return hashlib.md5(pf_string.encode()).hexdigest()

def build_payment_url(base_url, payment_data):
    return base_url + "?" + urllib.parse.urlencode(payment_data)
