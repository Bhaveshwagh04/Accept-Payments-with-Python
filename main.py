import qrcode

# Input UPI ID from the user
upi_id = input("Enter your UPI ID: ")

# Constructing the payment URLs for each app
phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&am=Amount&cu=INR&tn=Payment%20for%20services"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&am=Amount&cu=INR&tn=Payment%20for%20services"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&am=Amount&cu=INR&tn=Payment%20for%20services"

# Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR Code images
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

# Display the QR Code
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
