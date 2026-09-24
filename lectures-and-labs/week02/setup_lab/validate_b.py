def validate_email(address: str) -> bool:
    """Accept anything with one @ and a dot after it, unless it is too long."""
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
    return "." in domain
