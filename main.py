import asyncio
import requests
from pytoniq_core.crypto.keys import mnemonic_new
from tonutils.client import LiteserverClient
from tonutils.wallet import WalletV5R1


async def main():
    liteserver_TU = LiteserverClient(requests.get('https://ton.org/global-config.json').json())
    with open("wallets.txt", "a") as file:
        while True:
            mnemo = mnemonic_new(24)
            wallet, _, _, _ = WalletV5R1.from_mnemonic(liteserver_TU, mnemo)
            result = f"{wallet.address.to_str(is_bounceable=False)} {mnemo}\n"
            file.write(result)
            file.flush()
            print(result.strip())

asyncio.run(main())
