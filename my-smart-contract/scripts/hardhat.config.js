module.exports = {
    solidity: "0.8.0",
    networks: {
      localhost: {
        url: "http://127.0.0.1:8545",
        accounts: [`0x${process.env.PRIVATE_KEY}`]
      },
      // Add other networks if needed (e.g., ropsten, rinkeby, etc.)
    }
  };
  