// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@fxportal/contracts/tunnel/FxBaseRootTunnel.sol";

contract StoreUpdater is FxBaseRootTunnel {

    constructor(
		address _checkpointManager, address _fxRoot
	) FxBaseRootTunnel(_checkpointManager, _fxRoot) { }

    function _processMessageFromChild(bytes memory message) 
		internal 
		virtual
		override
	{
		// PASS
	}

	function addCollection(address newCollection) public {
		_sendMessageToChild(abi.encode(newCollection));
	}


}
