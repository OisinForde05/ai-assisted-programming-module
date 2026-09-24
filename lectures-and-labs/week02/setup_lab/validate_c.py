def validate_email(address: str) -> bool:
    """Same decision set as validate_a: intentionally repeated prompt, same strict rules."""
    if not isinstance(address, str):
        return False
    if len(address) > 254:
        return False
    if address != address.strip():
        return False
    if address.count("@") != 1:
        return False

    local, domain = address.rsplit("@", 1)
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    if ".." in local or ".." in domain:
        return False

    allowed_local = set("abcdefghijklmnopqrstuvwxyz0123456789._%-")
    allowed_domain = set("abcdefghijklmnopqrstuvwxyz0123456789.-")

    if any(ch.isupper() for ch in address):
        return False
    if not all(ch in allowed_local for ch in local):
        return False
    if not all(ch in allowed_domain for ch in domain):
        return False

    return True
