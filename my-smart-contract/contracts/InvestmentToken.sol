// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract InvestmentToken is ERC20 {
    address public admin;

    constructor() ERC20("InvestmentToken", "ITK") {
        admin = msg.sender;
    }

    function mint(address to, uint256 amount) external {
        //require(msg.sender == admin, "Only admin can mint tokens");
        _mint(to, amount);
    }

    function redeem(uint256 amount) external {
        _burn(msg.sender, amount);
        payable(msg.sender).transfer(amount / 100); // Example: 1 token = 0.01 ETH
    }

    receive() external payable {}
}