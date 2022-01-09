walletool ~ a tool for reading wallet.dat files
===============================================

Installation
------------

* Install Python 3.x.
* Install the `bsddb3` module (if you're on Windows, use Gohlke's site).
* pip3 install bsddb3
* Install the `request` module:
*    pip3 install request

Extracting private keys from Bitcoin-QT/Litecoin-QT wallets
-----------------------------------------------------------

* Have your `wallet.dat` handy.
* For Bitcoin, run `python3 wt_extract_keys.py -d wallet.dat -v 0 > keys.txt`
* For Litecoin, run `python3 wt_extract_keys.py -d wallet.dat -v 48`
* For Ravencoin, run `python3 wt_extract_keys.py -d wallet.dat -v 60` 

A list of addresses / private keys is printed.

To query explorer:
`python3 check_bchain.py --coin BTC keys.txt > balance.txt`

YMMV :)
