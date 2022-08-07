// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EncodingTest {
	function testEncoding(address toTest) public view returns (address) {
		bytes memory addrEncoded = abi.encode(toTest);
		return abi.decode(addrEncoded, (address));
	}
}
