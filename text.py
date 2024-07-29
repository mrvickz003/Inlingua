import pdfkit

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/5.1.3/css/bootstrap.min.css" rel="stylesheet">
    <title>Payment Receipt</title>
</head>
<body>
    <div class="px-3 my-5 border">
        <div class="row mb-4 border-bottom">
            <div class="col-12 text-end">
                <h4 class="p-3">PAYMENT RECEIPT</h4>
            </div>
        </div>
        <div class="row mb-4 border-bottom">
            <div class="col-6">
                <img src="https://inlinguachennai.com/wp-content/uploads/2022/07/L1.png" alt="" width="200">
                <p class="mt-2">1481 Northern Street<br>
                    Greater South Avenue<br>
                    New York, New York 10001<br>
                    USA<p>
            </div>
            <div class="col-6 text-end">
                <p class="mb-1 p-0">Payment Bill : INV-000031</p>
                <p class="mb-1 p-0">Bill Date : 18 May 2023</p>
                <p class="mb-1 p-0">Bill Time : 12:40 PM</p>
            </div>
        </div>
        <div class="row mb-4 border-bottom">
            <div class="col-6">
                <h6>Bill To:</h6>
                <p>Ms. Mary D. Dunton<br>
                    +91 9876543210<br>
                    test@inlinguachennai.com</p>
            </div>
            <div class="col-6 text-end">
                <h6>Ship To:</h6>
                <p>Ms. Mary D. Dunton<br>
                    +91 9878654022<br>
                    marydunton@gmail.com</p>
            </div>
        </div>
        <div class="row mb-4">
            <div class="col-12">
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Account Holder Name</th>
                            <th>Transaction ID</th>
                            <th>Payment Type</th>
                            <th>Amount Paid</th>
                            <th>Balance Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>Vignesh Muthaiyan</td>
                            <td>76756545444227</td>
                            <td>Full Payment</td>
                            <td>Rs 500.00</td>
                            <td>Rs 0.00</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="row">
            <div class="col-12 d-flex justify-content-end">
                <div class="d-flex flex-column ">
                    <strong class="text-center mb-3">Received By</strong>
                    <img src="https://inlinguachennai.com/wp-content/uploads/2022/07/L1.png" alt="" width="200">
                </div>
            </div>
        </div>
        <div class="row mt-4">
            <div class="col-12 text-center">
                <p>Thanks for your business.</p>
                <p><small>Terms & Conditions: Full payment is due upon receipt of this invoice. Late payments may incur
                        additional charges or interest as per the applicable laws.</small></p>
            </div>
        </div>
    </div>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/5.1.3/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

pdfkit.from_string(html_content, 'payment_receipt.pdf')
