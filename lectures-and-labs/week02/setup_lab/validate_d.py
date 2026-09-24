def validate_email(address: str) -> bool:
    """A permissive variant: trims the ends, then checks for @ and a dot later on."""
    if not isinstance(address, str):
        return False
    address = address.strip()
    if not address or len(address) > 254:
        return False
    if address.count("@") != 1:
        return False

    local, domain = address.rsplit("@", 1)
    if not local or not domain:
        return False
    return "." in domain
