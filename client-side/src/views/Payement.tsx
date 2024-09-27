import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

const PaymentComponent = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState('');
  const [amount, setAmount] = useState('');

  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        try {
          // Request account access
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          setWeb3(web3Instance);
        } catch (error) {
          console.error("User denied account access");
        }
      }
      else if (window.web3) {
        setWeb3(new Web3(window.web3.currentProvider));
      }
      else {
        console.log('No web3? You should consider trying MetaMask!');
      }
    };

    initWeb3();
  }, []);

  useEffect(() => {
    const getAccountInfo = async () => {
      if (web3) {
        const accounts = await web3.eth.getAccounts();
        setAccount(accounts[0]);
        const balance = await web3.eth.getBalance(accounts[0]);
        setBalance(web3.utils.fromWei(balance, 'ether'));
      }
    };

    getAccountInfo();
  }, [web3]);

  const handlePayment = async () => {
    if (!web3 || !account) {
      alert('Please connect to MetaMask first.');
      return;
    }

    try {
      const amountInWei = web3.utils.toWei(amount, 'ether');
      const gasPrice = await web3.eth.getGasPrice();
      const gasLimit = 21000; // Standard gas limit for a simple transaction

      const tx = await web3.eth.sendTransaction({
        from: account,
        to: '0xFBaE2615B1937B25aD10CDd7277F4ADAD9Ca0049', // Replace with your recipient address
        value: amountInWei,
        gasPrice: gasPrice,
        gas: gasLimit,
      });

      console.log('Transaction successful:', tx);
      alert('Payment successful!');
    } catch (error) {
      console.error('Payment failed:', error);
      alert('Payment failed. Please check the console for details.');
    }
  };

  return (
    <div>
      <h1>MetaMask Polygon Payment</h1>
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
          <p>Balance: {balance} MATIC</p>
          <input
            type="text"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            placeholder="Amount in MATIC"
          />
          <button onClick={handlePayment}>Send Payment</button>
        </div>
      ) : (
        <p>Please connect to MetaMask</p>
      )}
    </div>
  );
};

export default PaymentComponent;