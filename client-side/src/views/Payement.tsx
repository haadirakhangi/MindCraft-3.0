import React, { useState, useEffect } from 'react';
import { BeaconWallet } from "@taquito/beacon-wallet";
import { NetworkType } from "@airgap/beacon-types";
import { TezosToolkit } from "@taquito/taquito";
import axios from 'axios';

interface Transaction {
  id: number;
  wallet_address: string;
  balance: number;
  timestamp: string;
}

const App: React.FC = () => {
  const rpcUrl = "https://ghostnet.ecadinfra.com";
  const Tezos = new TezosToolkit(rpcUrl);
  const contractAddress = "KT1R4i4qEaxF7v3zg1M8nTeyrqk8JFmdGLuu";

  const [wallet, setWallet] = useState<BeaconWallet | undefined>(undefined);
  const [address, setAddress] = useState<string | undefined>(undefined);
  const [balance, setBalance] = useState<string | undefined>(undefined);
  const [transactions, setTransactions] = useState<Transaction[]>([]);

  const [depositAmount, setDepositAmount] = useState<number>(1);
  const [depositButtonActive, setDepositButtonActive] = useState<boolean>(false);
  const [depositButtonLabel, setDepositButtonLabel] = useState<string>("Deposit");

  const [withdrawButtonActive, setWithdrawButtonActive] = useState<boolean>(true);
  const [withdrawButtonLabel, setWithdrawButtonLabel] = useState<string>("Withdraw");

  useEffect(() => {
    fetchTransactions();
  }, []);

  const connectWallet = async () => {
    const newWallet = new BeaconWallet({
      name: "Simple dApp tutorial",
      network: {
        type: NetworkType.GHOSTNET,
      },
    });
    await newWallet.requestPermissions();
    const userAddress = await newWallet.getPKH();
    setAddress(userAddress);
    await getWalletBalance(userAddress);
    setWallet(newWallet);
    setDepositButtonActive(true);
  };

  const disconnectWallet = () => {
    if (wallet) {
      wallet.client.clearActiveAccount();
      setWallet(undefined);
      setAddress(undefined);
      setBalance(undefined);
      setDepositButtonActive(false);
    }
  };

  const getWalletBalance = async (walletAddress: string) => {
    const balanceMutez = await Tezos.tz.getBalance(walletAddress);
    const balanceTez = balanceMutez.div(1000000).toFormat(2);
    setBalance(balanceTez);
    await storeTransaction(walletAddress, balanceTez);
  };

  const storeTransaction = async (walletAddress: string, balance: string) => {
    try {
      await axios.post('http://localhost:5000/api/transaction', {
        address: walletAddress,
        balance: balance
      });
      await fetchTransactions();
    } catch (error) {
      console.error('Error storing transaction:', error);
    }
  };

  const fetchTransactions = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/transactions');
      setTransactions(response.data);
    } catch (error) {
      console.error('Error fetching transactions:', error);
    }
  };

  const deposit = async () => {
    setDepositButtonActive(false);
    setDepositButtonLabel("Depositing...");

    if (wallet) {
      Tezos.setWalletProvider(wallet);
      const contract = await Tezos.wallet.at(contractAddress);

      try {
        const transactionParams = await contract.methods
          .deposit()
          .toTransferParams({
            amount: depositAmount,
          });
        const estimate = await Tezos.estimate.transfer(transactionParams);

        const operation = await Tezos.wallet
          .transfer({
            ...transactionParams,
            ...estimate,
          })
          .send();

        console.log(`Waiting for ${operation.opHash} to be confirmed...`);

        await operation.confirmation(2);

        console.log(
          `Operation injected: https://ghost.tzstats.com/${operation.opHash}`
        );

        if (address) {
          await getWalletBalance(address);
        }
      } catch (error) {
        console.error("Error during deposit:", error);
      }
    }

    setDepositButtonActive(true);
    setDepositButtonLabel("Deposit");
  };

  const withdraw = async () => {
    setWithdrawButtonActive(false);
    setWithdrawButtonLabel("Withdrawing...");

    if (wallet) {
      Tezos.setWalletProvider(wallet);
      const contract = await Tezos.wallet.at(contractAddress);

      try {
        const transactionParams = await contract.methods
          .withdraw()
          .toTransferParams();
        const estimate = await Tezos.estimate.transfer(transactionParams);

        const operation = await Tezos.wallet
          .transfer({
            ...transactionParams,
            ...estimate,
          })
          .send();

        console.log(`Waiting for ${operation.opHash} to be confirmed...`);

        await operation.confirmation(2);

        console.log(
          `Operation injected: https://ghost.tzstats.com/${operation.opHash}`
        );

        if (address) {
          await getWalletBalance(address);
        }
      } catch (error) {
        console.error("Error during withdrawal:", error);
      }
    }

    setWithdrawButtonActive(true);
    setWithdrawButtonLabel("Withdraw");
  };

  return (
    <main>
      <h1>Tezos bank dApp</h1>

      <div className="card">
        {wallet ? (
          <>
            <p>The address of the connected wallet is {address}.</p>
            <p>Its balance in tez is {balance}.</p>
            <p>
              To get tez, go to <a
                href="https://faucet.ghostnet.teztnets.com/"
                target="_blank"
                rel="noopener noreferrer"
              >
                https://faucet.ghostnet.teztnets.com/
              </a>.
            </p>
            <p>
              Deposit tez:
              <input
                type="number"
                value={depositAmount}
                onChange={(e) => setDepositAmount(Number(e.target.value))}
                min="1"
                max="100"
              />
              <input
                type="range"
                value={depositAmount}
                onChange={(e) => setDepositAmount(Number(e.target.value))}
                min="1"
                max="100"
              />
              <button onClick={deposit} disabled={!depositButtonActive}>
                {depositButtonLabel}
              </button>
            </p>
            <p>
              Withdraw tez:
              <button onClick={withdraw} disabled={!withdrawButtonActive}>
                {withdrawButtonLabel}
              </button>
            </p>
            <p>
              <button onClick={disconnectWallet}>Disconnect wallet</button>
            </p>
          </>
        ) : (
          <button onClick={connectWallet}>Connect wallet</button>
        )}
      </div>

      <div className="transactions">
        <h2>Recent Transactions</h2>
        <ul>
          {transactions.map(transaction => (
            <li key={transaction.id}>
              Address: {transaction.wallet_address}, 
              Balance: {transaction.balance} tez, 
              Time: {new Date(transaction.timestamp).toLocaleString()}
            </li>
          ))}
        </ul>
      </div>
    </main>
  );
};

export default App;