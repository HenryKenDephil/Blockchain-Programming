pragma solidity 0.8.11;

contract BankTransaction {

    struct Transaction {
        string messageHash;
        string signature;
        string pubKey;
    }

    mapping (string => Transaction) transactions;

    function addMessage(string memory _messageHash, string memory _signature, string memory _pubKey) public returns (uint) {
    }

    function getMessage(string memory _messageHash) public view returns(string memory, string memory, string memory) {
    }
}
