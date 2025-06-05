// src/App.jsx
import { useEffect, useState } from 'react';
import { ethers } from 'ethers';
import './index.css';

function App() {
  const [account, setAccount] = useState(null);
  const [status, setStatus] = useState('Not connected');

  const connectWallet = async () => {
    if (window.ethereum) {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccount(accounts[0]);
      setStatus('Wallet connected');
    } else {
      setStatus('Please install MetaMask');
    }
  };

  useEffect(() => {
    connectWallet();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-4">KrishiNet Dashboard</h1>
      <p>Status: {status}</p>
      {account && <p>Connected Wallet: {account}</p>}
    </div>
  );
}

export default App;
