from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    """Задача отправки email-уведомлений при успешной оформлении заказа."""
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dead {},\n\nYou have successfully placed an order.\
        You order id is {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.mail])
    return mail_sent