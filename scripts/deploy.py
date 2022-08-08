from brownie import ERC721Store, StoreUpdater
from brownie import accounts, network, config
from time import sleep


LOCAL_ENVS = ['development', 'ganache']

get_acc = lambda: accounts[0] if (
    network.show_active() in LOCAL_ENVS
) else accounts.add(config['wallets']['from_key'])

ask_for_verify = lambda x: input(f'Should verify {x}? y/N: ').lower() == 'y'

from_me = lambda: {'from': get_acc()}


def deploy_updater():
    return StoreUpdater.deploy(
        config['networks'][network.show_active()]['checkpoint_manager'],
        config['networks'][network.show_active()]['fx_root'],
        from_me(),
        publish_source=ask_for_verify('StoreUpdater')
    )

def deploy_store():
    return ERC721Store.deploy(
        config['networks'][network.show_active()]['fx_child'],
        from_me(),
        publish_source=ask_for_verify('ERC721Store')
    )

def test_adding_new_addr():
    ADDR = '0x1352149Cd78D686043B504e7e7D96C5946b0C39c'
    network.disconnect()

    if input('ADDR already added? Y/n: ').lower() == 'n':
        network.connect('goerli')
        tx = StoreUpdater[-1].addCollection(ADDR, from_me())
        tx.wait(1)
        network.disconnect()

    network.connect('polygon-test')
    store = ERC721Store[-1]
    while True:
        print('Checking if addr received...')
        dirs = store.collections()
        if ADDR in dirs: break
        print('Still not received :(')
        sleep(5)
        
    print('ADDR received throught cross chain message!')
    network.disconnect()

def deploy_on_testnet():
    network.disconnect()

    network.connect('goerli')
    deploy_updater()
    updater_addr = StoreUpdater[-1].address
    network.disconnect()

    network.connect('polygon-test')
    deploy_store()
    store_addr = ERC721Store[-1].address
    tx = ERC721Store[-1].setFxRootTunnel(updater_addr, from_me())
    tx.wait(1)
    network.disconnect()

    network.connect('goerli')
    tx = StoreUpdater[-1].setFxChildTunnel(store_addr, from_me())
    tx.wait(1)

def main():
    deploy_on_testnet()
    test_adding_new_addr()


