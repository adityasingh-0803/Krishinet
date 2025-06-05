// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AgriEscrow {
    address public buyer;
    address public seller;
    uint256 public price;
    bool public delivered;

    constructor(address _buyer, address _seller, uint256 _price) {
        buyer = _buyer;
        seller = _seller;
        price = _price;
        delivered = false;
    }

    function confirmDelivery() public {
        require(msg.sender == buyer, "Only buyer can confirm");
        delivered = true;
    }

    function releasePayment() public {
        require(delivered == true, "Product not confirmed");
        payable(seller).transfer(address(this).balance);
    }

    receive() external payable {}
}
