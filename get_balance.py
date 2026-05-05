"""Standalone script to query native token balances on Base (EVM) and Solana."""

import json
import urllib.request
import urllib.error

from web3 import Web3

BASE_RPC = "https://mainnet.base.org"
SOLANA_RPC = "https://api.mainnet-beta.solana.com"


def get_balance(wallet: str, chain: str) -> float:
    """Return the native token balance (in decimal) for *wallet* on *chain*.

    Parameters
    ----------
    wallet : str
        The wallet address to query.
    chain : str
        ``"base"`` for Base (ETH) or ``"solana"`` for Solana (SOL).

    Returns
    -------
    float
        The balance expressed in the chain's native decimal unit
        (ETH for Base, SOL for Solana).  Returns ``0`` on any error.
    """
    chain = chain.strip().lower()
    try:
        if chain == "base":
            return _get_base_balance(wallet)
        if chain == "solana":
            return _get_solana_balance(wallet)
        raise ValueError(f"Unsupported chain: {chain}")
    except Exception:
        return 0


def _get_base_balance(wallet: str) -> float:
    w3 = Web3(Web3.HTTPProvider(BASE_RPC))
    balance_wei = w3.eth.get_balance(Web3.to_checksum_address(wallet))
    return float(w3.from_wei(balance_wei, "ether"))


def _get_solana_balance(wallet: str) -> float:
    payload = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBalance",
            "params": [wallet],
        }
    ).encode()

    req = urllib.request.Request(
        SOLANA_RPC,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())

    lamports = data["result"]["value"]
    return lamports / 1e9


if __name__ == "__main__":
    # Quick demo — replace with real addresses to test.
    demo_evm = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    demo_sol = "vines1vzrYbzLMRdu58ou5XTby4qAqVRLmqo36NKPTg"

    print(f"Base  balance: {get_balance(demo_evm, 'base')} ETH")
    print(f"Solana balance: {get_balance(demo_sol, 'solana')} SOL")
