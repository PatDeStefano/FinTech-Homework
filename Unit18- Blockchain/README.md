# Unit 18- Blockchain Homework

###### In the assignment shows how to create a Genesis blockchain and send a transaction using the Proof of Authority.

### The following files are used for this assignment and need to be downloaded:
- [Installing Go Ethereum Tools](https://geth.ethereum.org/downloads/)

Geth and Puppeth are used to create the blockchain/ network
I used Git Bash to run these tools


##
## These are the steps for the assignment:

## 1. Create accounts using Geth for two nodes:
CD into your local blockchain-tools directory in order to run geth:

    ./geth account new --datadir node1
    


Do the same for node two:

    ./geth account new --datadir node2

The same message will apart as the first node but you will get a different address.

This is what it should look like in Git Bash:
![Node1](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/AccountOneSetup.PNG)

![Node2](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/AccountTwoSetup.PNG)
##

## 2. Use Puppeth to configure new genesis block:

    ./puppeth

    Network:
    puppeth

    Genesis Network
    333

![Genesis Create](https://github.com/PatDeStefano/PofA-Development-Chain/blob/main/ScreenShots/2.PNG)
##

## 3. Export genesis configuration:
# Here we export the Genesis to a folder or just in blockchain-tools

![Export](https://github.com/PatDeStefano/PofA-Development-Chain/blob/main/ScreenShots/export1.PNG)
![Export2](https://github.com/PatDeStefano/PofA-Development-Chain/blob/main/ScreenShots/export2.PNG)
##



## 4. Then exit by using ctrl + c command in git bash to exit out and use ./geth command to initialize the node and connect to the blockchain

## I had to add this code before to remove errors 
    $ rm -Rf node1/geth node2/geth

    /geth init puppeth.json --datadir node1

The above results in the following (important to see "Successfully wrote genesis state" at the bottom):
![Create Json](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/Create%20Json.PNG)
##


## 5. Do the same as the first node

    /geth init puppeth.json --datadir node2
    
You will get the same message as the first node.

The above results in the following (important to see "Successfully wrote genesis state" at the bottom):
![Create Json](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/Create%20Json.PNG)
##

## 6. Create a tree diagram of the model using one of these two commands:
    cmd //c tree //F

![Create File Tree](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/Filetree1.PNG)

![Create File Tree2](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/Filetree2.PNG)
##

## 7. Mine the first node:

    ./geth --datadir node1 --mine --minerthreads 1
    
![MineNode1](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/MineGenesis.PNG)

![MineNode1](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/MineGenesis2.PNG)

![MineNode1](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/MineGenesis3.PNG)
##

## 8. Mine the second node:
Then open a new Git Bash window and type the following command:

   ./geth --datadir node2 --port 30304 --rpc --bootnodes "enode://e94a9e3eb24df3c68ab040387bfcb89255b80af90063640454f664ef695dea3a1f64a1010d5c34e2ebd3b76cb2b28de8c7f95734c723b014487e798f7753d1b0@127.0.0.1:30303" --ipcdisable
    
![MineNode2](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/MineGenesisNode2.PNG)

![MineNode2](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/MineGenesisNode2part2.PNG)

![MineNode2](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/MineGenesisNode2part3.PNG)
##

## 9. Use MyCrypto program to create a custom node and send a test transaction:

Open MyCrypto, then create a custom node

![MyCrypto](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/Walletpicture.PNG)

![MyCrypto](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/CustomNode2.PNG)

![MyCrypto](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/CustomNode.PNG)

Then send Ethereum from the the first address to the second.

![Send Transacton1](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/SendTransaction.PNG)

![Send Transacton2](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/SendTransaction2.PNG)

![Send Transacton3](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/SendTransaction3.PNG)

![Send Transacton4](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/SendTransaction4.PNG)

![Send Transacton5](https://github.com/PatDeStefano/FinTech-Homework/blob/main/Unit18-%20Blockchain/ScreenShots/SendTransaction5.PNG)
