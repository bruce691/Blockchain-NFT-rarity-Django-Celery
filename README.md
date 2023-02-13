# Blockchain (web3) | NFT-rarity | Django | Celery | Redis | PostgreSQL

This project uses `Django`, `celery` and `flower` for asynchronous tasks and `web3.py` to interact with the `Ethereum blockchain` in order to fetch `NFT collection metadata`. 

You need two things to interact with a smart contract:

- The smart contract address
- The Application Binary Interface (ABI)
- Infura API Key in order to talk to ETH blockchain

Both of these can be found on [Etherscan](https://etherscan.io/)

<img src="https://github.com/Aback231/Blockchain-NFT-rarity-Django-Celery/blob/main/APES.png"> <img src="https://github.com/Aback231/Blockchain-NFT-rarity-Django-Celery/blob/main/add_collection.png"> 

<img src="https://github.com/Aback231/Blockchain-NFT-rarity-Django-Celery/blob/main/progress.png"> <img src="https://github.com/Aback231/Blockchain-NFT-rarity-Django-Celery/blob/main/finished.png"> 

`NFT JSON metadata` consists of `text and images` stored on `InterPlanetary File System (IPFS)`, which represents a distributed file system. [Rarity Tools](https://rarity.tools/) was one of the first projects that one could use to calculate NFT rarity. We calculate rarity using the very same formula:

`[Rarity Score for a Trait Value] = 1 / ([Number of Items with that Trait Value] / [Total Number of Items in Collection])`

`Celery` and `Redis` are used to offload `NFT fetching` into `Async tasks`, as one could try to fetch hundreds of NFTs at once, but also because free Infura API enforces rate limiting.
