"""
Module used to describe Movements as returned by Bitfinex API
"""


class Movement:
    """
    ID  String  Movement identifier
    CURRENCY    String  The symbol of the currency (ex. "BTC")
    CURRENCY_NAME   String  The extended name of the currency (ex. "BITCOIN")
    MTS_STARTED Date    Movement started at
    MTS_UPDATED Date    Movement last updated at
    STATUS  String  Current status
    AMOUNT  String  Amount of funds moved. Negative numbers correspond to withdrawals
    FEES    String  Tx Fees applied
    DESTINATION_ADDRESS String  Destination address
    TRANSACTION_ID  String  Transaction identifier
    """


    def __init__(self, movement_id, currency, currency_name, movement_start_time, movement_update_time, 
                 status, amount, fees, destination_address, transaction_id):
        # pylint: disable=invalid-name
        self.id = movement_id
        self.currency = currency
        self.currency_name = currency_name
        self.movement_start_time = movement_start_time
        self.movement_update_time = movement_update_time
        self.status = status
        self.amount = amount
        self.fees = fees
        self.destination_address = destination_address
        self.transaction_id = transaction_id


    @staticmethod
    def from_raw_rest_movement(raw_movement):
        """
        Generate a Movement object from a raw movement array
        """
        # [24224048, 'BTC', 'BITCOIN', 2019-01-01, 2019-01-02, None, 1.0, 0.0001, 
        #  '3A9iiUAHG4ti3HCfSG4VmeFtMcSVyFjRLL', 'a5b9ff7a66aceb5f575f8ff43c7962dda6b6f6302814d2470b35d4b202befa28']
        return Movement(*raw_movement)


    def __str__(self):
        return "Movement '{}': {} {} -> {} fee={}>".format(
            self.movement_start_time, self.amount, self.currency, self.destination_address, self.fee)
