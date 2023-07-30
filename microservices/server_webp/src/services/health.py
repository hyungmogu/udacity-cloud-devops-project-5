class HealthServices:
    """
    Object for checking the health of the service.
    """
    def check_health(self) -> dict:
        """
        Checks the health of the service. Returns response if service is well.

        Returns: dict
        """
        return {"status": "ok"}