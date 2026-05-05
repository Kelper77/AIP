"""Standalone script to detect the blockchain from agent info."""


def detect_chain(agent_info: dict) -> str:
    """Determine the blockchain based on *agent_info*.

    Parameters
    ----------
    agent_info : dict
        Must contain ``"chat_url"`` (str) and ``"wallet"`` (str).

    Returns
    -------
    str
        ``"base"`` if the chat URL contains "base" (case-insensitive) or the
        wallet starts with ``"0x"``.  Otherwise ``"solana"``.
    """
    chat_url: str = agent_info.get("chat_url", "")
    wallet: str = agent_info.get("wallet", "")

    if "base" in chat_url.lower() or wallet.startswith("0x"):
        return "base"
    return "solana"


if __name__ == "__main__":
    print(detect_chain({"chat_url": "https://base.chat/room", "wallet": "0xABC"}))
    print(detect_chain({"chat_url": "https://solchat.io", "wallet": "Vine123"}))
    print(detect_chain({"chat_url": "https://example.com", "wallet": "0xDEF"}))
    print(detect_chain({"chat_url": "https://example.com", "wallet": "SolAddr"}))
