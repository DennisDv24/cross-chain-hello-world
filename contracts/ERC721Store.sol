// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@fxportal/contracts/tunnel/FxBaseChildTunnel.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";


contract ERC721Store is FxBaseChildTunnel {
	
	address[] private _collections; 

	constructor(address _fxChild) FxBaseChildTunnel(_fxChild) {
		// TODO
	}
	

	bytes private _toStore;
	function _processMessageFromRoot(
		uint256 stateId, address sender, bytes memory message
	) internal virtual override {
		// TODO
		_toStore = message;
	}

	function testEncoding(address toTest) public returns (address) {
		bytes memory addrEncoded = abi.encode(toTest);
		return abi.decode(addrEncoded, (address));
	}
		

}
