from utils.firestore import create_pass

def handler(request):
    if request.method != "POST":
        return {"error": "Invalid method"}, 405
    
    pass_type = request.form.get("custom_str1")
    user_id = request.form.get("custom_str2")
    payment_status = request.form.get("payment_status")

    if payment_status == "COMPLETE":
        create_pass(user_id, pass_type)

    return "OK", 200
