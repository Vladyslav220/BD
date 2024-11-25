from .general_controller import GeneralController
from ..service import customer_service
from ..dao import customer_dao

class CustomerController(GeneralController):
    _service = customer_service

    def has_active_orders(self, customer_id: int) -> bool:
        """
        Перевіряє, чи є у клієнта активні замовлення.
        """
        return customer_dao.has_active_orders_for_customer(customer_id)

    def delete(self, customer_id: int) -> None:
        """
        Видаляє клієнта, якщо у нього немає активних замовлень.
        """
        if self.has_active_orders(customer_id):
            raise Exception("Cannot delete customer with active orders.")  # Обробка винятку

        super().delete(customer_id)  # Виклик основного методу видалення
