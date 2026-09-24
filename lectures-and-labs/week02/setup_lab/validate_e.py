def validate_email(address: str) -> bool:
    """Middle-ground variant: ASCII-only, no spaces, no consecutive dots, but allows + and uppercase."""
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
    if any(ch.isspace() for ch in local):
        return False
    if not all(ch.isascii() for ch in address):
        return False

    return True
