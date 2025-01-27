async function main() {
    const [deployer] = await ethers.getSigners();
  
    console.log("Deploying contracts with the account:", deployer.address);
  
    // Replace with your contract's name
    const ContractFactory = await ethers.getContractFactory("InvestmentToken");
    const contract = await ContractFactory.deploy();
  
    console.log("Contract deployed to address:", contract.address);
  }
  
  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error);
      process.exit(1);
    });
  