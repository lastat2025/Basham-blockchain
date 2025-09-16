# Basham-blockchain<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basham Blockchain</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #fff;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            padding: 30px 0;
            margin-bottom: 30px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        h1 {
            font-size: 2.8rem;
            margin-bottom: 10px;
            color: #4ecdc4;
            text-shadow: 0 0 10px rgba(78, 205, 196, 0.5);
        }
        
        .tagline {
            font-size: 1.2rem;
            opacity: 0.8;
        }
        
        .dashboard {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
        
        .card h2 {
            color: #4ecdc4;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .stats {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        
        .stat {
            text-align: center;
        }
        
        .stat-value {
            font-size: 2rem;
            font-weight: bold;
            color: #ff6b6b;
        }
        
        .stat-label {
            font-size: 0.9rem;
            opacity: 0.7;
        }
        
        .actions {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        
        input, textarea, button {
            padding: 12px;
            border: none;
            border-radius: 5px;
            background: rgba(255, 255, 255, 0.1);
            color: white;
            font-size: 1rem;
        }
        
        button {
            background: #4ecdc4;
            color: #0f2027;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        button:hover {
            background: #ff6b6b;
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }
        
        .blocks-container {
            margin-top: 30px;
        }
        
        .blocks {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        
        .block {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
        }
        
        .block:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
        }
        
        .block-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .block-id {
            font-weight: bold;
            color: #4ecdc4;
            font-size: 1.2rem;
        }
        
        .block-hash {
            font-family: monospace;
            font-size: 0.8rem;
            word-break: break-all;
            margin: 10px 0;
            color: #ff6b6b;
        }
        
        .block-data {
            margin: 10px 0;
            padding: 10px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 5px;
            font-size: 0.9rem;
        }
        
        .timestamp {
            font-size: 0.8rem;
            opacity: 0.7;
            text-align: right;
        }
        
        .mining-animation {
            display: none;
            text-align: center;
            margin: 20px 0;
        }
        
        .mining-animation.active {
            display: block;
        }
        
        .spinner {
            width: 40px;
            height: 40px;
            margin: 0 auto;
            border: 4px solid rgba(255, 255, 255, 0.1);
            border-left: 4px solid #4ecdc4;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        @media (max-width: 768px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
            
            .stats {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Basham Blockchain</h1>
            <p class="tagline">A simple blockchain implementation running in your browser</p>
        </header>
        
        <div class="dashboard">
            <div class="card">
                <h2>Blockchain Stats</h2>
                <div class="stats">
                    <div class="stat">
                        <div class="stat-value" id="block-count">1</div>
                        <div class="stat-label">Blocks</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value" id="difficulty">3</div>
                        <div class="stat-label">Difficulty</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value" id="mining-time">0</div>
                        <div class="stat-label">Avg Mining Time (ms)</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value" id="chain-valid">Yes</div>
                        <div class="stat-label">Chain Valid</div>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <h2>Actions</h2>
                <div class="actions">
                    <input type="text" id="block-data" placeholder="Enter data for new block">
                    <button id="mine-button">Mine New Block</button>
                    <button id="validate-button">Validate Chain</button>
                    <button id="difficulty-up">Increase Difficulty</button>
                    <button id="difficulty-down">Decrease Difficulty</button>
                </div>
                
                <div class="mining-animation" id="mining-animation">
                    <div class="spinner"></div>
                    <p>Mining block... This may take a moment</p>
                </div>
            </div>
        </div>
        
        <div class="blocks-container">
            <h2>Blocks in Chain</h2>
            <div class="blocks" id="blocks">
                <!-- Blocks will be displayed here -->
            </div>
        </div>
    </div>

    <script>
        class Block {
            constructor(index, timestamp, data, previousHash = '') {
                this.index = index;
                this.timestamp = timestamp;
                this.data = data;
                this.previousHash = previousHash;
                this.hash = this.calculateHash();
                this.nonce = 0;
            }
            
            calculateHash() {
                return SHA256(this.index + this.previousHash + this.timestamp + JSON.stringify(this.data) + this.nonce).toString();
            }
            
            mineBlock(difficulty) {
                const startTime = performance.now();
                while (this.hash.substring(0, difficulty) !== Array(difficulty + 1).join('0')) {
                    this.nonce++;
                    this.hash = this.calculateHash();
                }
                const endTime = performance.now();
                return endTime - startTime;
            }
        }
        
        class Blockchain {
            constructor() {
                this.chain = [this.createGenesisBlock()];
                this.difficulty = 3;
                this.miningTimes = [];
            }
            
            createGenesisBlock() {
                return new Block(0, new Date().toISOString(), 'Genesis Block', '0');
            }
            
            getLatestBlock() {
                return this.chain[this.chain.length - 1];
            }
            
            addBlock(newBlock) {
                newBlock.previousHash = this.getLatestBlock().hash;
                const miningTime = newBlock.mineBlock(this.difficulty);
                this.miningTimes.push(miningTime);
                this.chain.push(newBlock);
                return miningTime;
            }
            
            isChainValid() {
                for (let i = 1; i < this.chain.length; i++) {
                    const currentBlock = this.chain[i];
                    const previousBlock = this.chain[i - 1];
                    
                    if (currentBlock.hash !== currentBlock.calculateHash()) {
                        return false;
                    }
                    
                    if (currentBlock.previousHash !== previousBlock.hash) {
                        return false;
                    }
                }
                return true;
            }
            
            getAverageMiningTime() {
                if (this.miningTimes.length === 0) return 0;
                return this.miningTimes.reduce((a, b) => a + b, 0) / this.miningTimes.length;
            }
        }
        
        // Simple SHA256 implementation for demonstration purposes
        const SHA256 = function(input) {
            // This is a simplified version for demonstration only
            // In a real implementation, you would use a proper SHA256 library
            let hash = 0;
            if (input.length === 0) return hash;
            for (let i = 0; i < input.length; i++) {
                const char = input.charCodeAt(i);
                hash = ((hash << 5) - hash) + char;
                hash = hash & hash;
            }
            return Math.abs(hash).toString(16).padStart(64, '0');
        };
        
        // Initialize the blockchain
        const bashamCoin = new Blockchain();
        
        // DOM elements
        const blockCountElement = document.getElementById('block-count');
        const difficultyElement = document.getElementById('difficulty');
        const miningTimeElement = document.getElementById('mining-time');
        const chainValidElement = document.getElementById('chain-valid');
        const blockDataElement = document.getElementById('block-data');
        const mineButton = document.getElementById('mine-button');
        const validateButton = document.getElementById('validate-button');
        const difficultyUpButton = document.getElementById('difficulty-up');
        const difficultyDownButton = document.getElementById('difficulty-down');
        const blocksContainer = document.getElementById('blocks');
        const miningAnimation = document.getElementById('mining-animation');
        
        // Display blocks function
        function displayBlocks() {
            blocksContainer.innerHTML = '';
            bashamCoin.chain.forEach(block => {
                const blockElement = document.createElement('div');
                blockElement.className = 'block';
                blockElement.innerHTML = `
                    <div class="block-header">
                        <span class="block-id">Block #${block.index}</span>
                    </div>
                    <div class="timestamp">${new Date(block.timestamp).toLocaleString()}</div>
                    <div class="block-data">
                        <strong>Data:</strong> ${block.data}
                    </div>
                    <div class="block-hash">
                        <strong>Hash:</strong> ${block.hash}
                    </div>
                    <div class="block-hash">
                        <strong>Previous Hash:</strong> ${block.previousHash}
                    </div>
                    <div class="block-hash">
                        <strong>Nonce:</strong> ${block.nonce}
                    </div>
                `;
                blocksContainer.appendChild(blockElement);
            });
            
            // Update stats
            blockCountElement.textContent = bashamCoin.chain.length;
            difficultyElement.textContent = bashamCoin.difficulty;
            miningTimeElement.textContent = bashamCoin.getAverageMiningTime().toFixed(2);
            chainValidElement.textContent = bashamCoin.isChainValid() ? 'Yes' : 'No';
            chainValidElement.style.color = bashamCoin.isChainValid() ? '#4ecdc4' : '#ff6b6b';
        }
        
        // Mine new block
        mineButton.addEventListener('click', () => {
            const data = blockDataElement.value || `Block ${bashamCoin.chain.length} data`;
            
            // Show mining animation
            miningAnimation.classList.add('active');
            
            // Use setTimeout to allow the UI to update before starting the mining process
            setTimeout(() => {
                const newBlock = new Block(bashamCoin.chain.length, new Date().toISOString(), data);
                const miningTime = bashamCoin.addBlock(newBlock);
                
                // Update UI
                displayBlocks();
                blockDataElement.value = '';
                
                // Hide mining animation
                miningAnimation.classList.remove('active');
                
                console.log(`Block mined in ${miningTime.toFixed(2)}ms`);
            }, 100);
        });
        
        // Validate chain
        validateButton.addEventListener('click', () => {
            const isValid = bashamCoin.isChainValid();
            alert(isValid ? 'Blockchain is valid!' : 'Blockchain is invalid!');
            displayBlocks();
        });
        
        // Adjust difficulty
        difficultyUpButton.addEventListener('click', () => {
            bashamCoin.difficulty++;
            displayBlocks();
        });
        
        difficultyDownButton.addEventListener('click', () => {
            if (bashamCoin.difficulty > 1) {
                bashamCoin.difficulty--;
                displayBlocks();
            }
        });
        
        // Initial display
        displayBlocks();
    </script>
</body>
</html>
