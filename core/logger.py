import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/audit.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
)

logger = logging.getLogger("KeycloakJML")


class AuditLogger:

    @staticmethod
    def login(username):
        logger.info(f"[LOGIN] Admin '{username}' authenticated successfully.")

    @staticmethod
    def create_user(username):
        logger.info(f"[JOINER] User '{username}' created.")

    @staticmethod
    def delete_user(username):
        logger.info(f"[LEAVER] User '{username}' deleted.")

    @staticmethod
    def assign_group(username, group):
        logger.info(f"[GROUP] '{username}' assigned to '{group}'.")

    @staticmethod
    def remove_group(username, group):
        logger.info(f"[GROUP] '{username}' removed from '{group}'.")

    @staticmethod
    def assign_role(username, role):
        logger.info(f"[ROLE] '{username}' assigned role '{role}'.")

    @staticmethod
    def custom(message):
        logger.info(message)