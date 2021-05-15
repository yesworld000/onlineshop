import logging
import os
import shutil

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete

from api.models import Category, Photo
from auth_.models import Profile, MainUser


logger = logging.getLogger(__name__)


@receiver(post_delete, sender=Category)
def delete_image_on_category_delete(sender, instance, *args, **kwargs):
    img = instance.img
    if img:
        os.remove(img.path)
        logger.debug(f'Image deleted ID: {instance.img}')
        logger.info(f'Image deleted ID: {instance.img}')
        logger.warning(f'Image deleted ID: {instance.img}')
        logger.error(f'Image deleted ID: {instance.img}')
        logger.critical(f'Image deleted ID: {instance.img}')


@receiver(post_delete, sender=Photo)
def delete_image_on_photo_delete(sender, instance, *args, **kwargs):
    img = instance.img
    if img:
        os.remove(img.path)
        logger.debug(f'Image deleted ID: {instance.img}')
        logger.info(f'Image deleted ID: {instance.img}')
        logger.warning(f'Image deleted ID: {instance.img}')
        logger.error(f'Image deleted ID: {instance.img}')
        logger.critical(f'Image deleted ID: {instance.img}')
