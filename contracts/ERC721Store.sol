// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@fxportal/contracts/tunnel/FxBaseChildTunnel.sol";

contract ERC721Store is FxBaseChildTunnel {
	
	address[] private _collections; 

	constructor(address _fxChild) FxBaseChildTunnel(_fxChild) { }
	
	/*
	 * @param message abi encoded ERC721 address to store
	 */
	function _processMessageFromRoot(
		uint256 stateId, address sender, bytes memory message
	) internal virtual override {
		_collections.push(abi.decode(message, (address)));
	}

	function collections() public view returns (address[] memory) {
		return _collections;
	}

}
