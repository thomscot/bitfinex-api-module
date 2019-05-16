from bfxapi.rest.BfxRest import BfxRest
import unittest
import asyncio
import os
from dateutil.tz import tzutc
from datetime import datetime


class TestBfxRest(unittest.TestCase):
    API_KEY = os.getenv('BALANCE_TRACER_BITFINEX_KEY')
    API_SECRET = os.getenv('BALANCE_TRACER_BITFINEX_SECRET')


    def test_get_currency_movements(self):
        loop = asyncio.new_event_loop()
        bfx = BfxRest(self.API_KEY, self.API_SECRET, loop=loop, logLevel='DEBUG')

        movements = asyncio.run(bfx.get_currency_movements('BTC', datetime(2015, 9, 1, tzinfo=tzutc()),
                                                           datetime(2019, 5, 1, tzinfo=tzutc())))
        self.assertIsNotNone(movements)

        loop.close()


if __name__ == '__main__':
    unittest.main()
