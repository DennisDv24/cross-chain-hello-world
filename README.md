# MATIC-ETH communication test via MATIC architecture
scripts/deploy.py will deploy a ERC721Store contract (on matic) and a StoreUpdater one (on ethereum).
Then, the script will add a address to the ERC721Store through StoreUpdater `addCollection` function,
after some time ERC721Store will receive that address and the script will communicate that 
in the `test_adding_new_addr` function.
