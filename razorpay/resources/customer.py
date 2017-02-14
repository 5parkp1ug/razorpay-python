from .base import Resource
from .Url import URL


class Customer(Resource):
    def __init__(self, client=None):
        self.client = client
        self.base_url = URL.CUSTOMER_URL

    def fetch(self, customer_id, data={}, **kwargs):
        """"
        Fetch Customer for given Id

        Args:
            customer_id : Id for which customer object has to be retrieved

        Returns:
            Order dict for given customer Id
        """
        return super(Customer, self).fetch(customer_id, data, **kwargs)

    def create(self, data={}, **kwargs):
        """"
        Create Customer from given dict

        Returns:
            Customer Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def edit(self, data={}, **kwargs):
        """"
        Create Customer from given dict

        Returns:
            Customer Dict which was created
        """
        url = self.base_url
        return self.put_url(url, data, **kwargs)
