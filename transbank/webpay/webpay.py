from transbank import webpay
from tbk.commerce import Commerce
from tbk.services import WebpayService

class Webpay(object):
    def __init__(self, configuration):
        self.configuration = configuration

    def get_normal_transaction(self):
        return WebpayNormal(self.configuration)

class WebpayNormal(object):
    def __init__(self, configuration):
        self.configuration = configuration
        self.mode = configuration.environment
        self.commerce_code = configuration.commerce_code

        self.commerce = Commerce(
            commerce_code=self.configuration.commerce_code,
            key_data=self.configuration.private_key,
            cert_data=self.configuration.public_cert,
            tbk_cert_data=webpay.TBK_CERT_DATA,
            environment=self.mode)

        self.webpay_service = WebpayService(self.commerce)

    def init_transaction(self, amount, session_id, buy_order, return_url, final_url):
        init_transaction_response = self.webpay_service.init_transaction(
            amount=amount,
            buy_order=buy_order,
            return_url=return_url,
            final_url=final_url,
            session_id=session_id
        )

        return init_transaction_response.result

    def get_transaction_result(self, token):
        transaction = self.webpay_service.get_transaction_result(token)
        self.webpay_service.acknowledge_transaction(token)
        return transaction
