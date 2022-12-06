pragma solidity 0.8.11;

contract BankTransaction {

    struct Transaction {
        string paymentIdHash;
        string clientIdHash;
        string receiverIdHash;
        uint totalAmount;

        /*function getAmount() public view returns (uint) {
            return amount;*/
        }
        mapping(address => uint256) amount;
        mapping(address => uint256) paymentTimestamps;

        function addNewPayment() public payable{
            totalAmount = totalAmount + msg.value;
            paymentTimestamps[msg.sender] = block.timestamps;
        }

        function getInformation(address userAddress) public view returns(uint){
            string paymentId = paymentIdHash[userAddress];
            string clientId = clientIdHash[userAddress];
            string receiverId = clientIdHash[userAddress];
            return clientId + string(paymentIdHash + receiverIdHash);
        }

        function getAllPayment() public payable {
            address payable paymentTo = payable(msg.sender);
            uint amountToTransfer = getPayment(msg.sender);
            uint paymentTo.transfer(amountToTransfer);
            totalpayment = totalAmount - amountToTransfer;
            balances[msg.receiver] = 0;
        }
        
    }


