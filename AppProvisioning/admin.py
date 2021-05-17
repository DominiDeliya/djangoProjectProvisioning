from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from django.utils import timezone
from django.core import serializers
from .models import Customer, Extension, DeviceVendor, DeviceModel, Device, DSS
import logging

logger = logging.getLogger(__name__)

admin.site.register(Customer)
admin.site.register(Extension)
admin.site.register(DeviceVendor)
admin.site.register(DeviceModel)
admin.site.register(DSS)


@admin.display(description='Last Update')
def readable_cfg_last_update(device):
    now = timezone.now()
    diff_seconds = (now - device.cfg_last_update).total_seconds()
    diff_min = int(diff_seconds / 60)
    if diff_min < 60:
        return '{} minutes ago'.format(diff_min)
    else:
        return '{} hours ago'.format(int(diff_min / 60))


@admin.display(description='DSS Count')
def get_dss_count(device):
    result = DSS.objects.filter(devices=device.id)
    return len(result)


def download_xml(self, request, queryset):
    logger.info('Generating xml config for the device(s) size={}'.format(len(queryset)))
    for device in queryset:
        device.cfg_last_update = timezone.now()
        device.save()
        logger.info('Device cfg_last_update attribute updated to id={} cfg_last_update={}'
                    .format(device.id, device.cfg_last_update))

    xml_data = serializers.serialize("xml", queryset)
    response = HttpResponse(xml_data, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename=device.xml'
    logger.info('XML config generated for the devices size={}'.format(len(queryset)))
    return response


def download_button(device):
    return format_html('<a class="button" href="{}">Download</a>&nbsp;',
                       reverse('admin:download-xml', args=[device.id]))


def download(request, device_id):
    logger.info('Downloading xml config for the device id={}'.format(device_id))
    device = Device.objects.get(id=device_id)
    device.cfg_last_update = timezone.now()
    device.save()
    logger.info('Device cfg_last_update attribute updated to cfg_last_update={}'.format(device.cfg_last_update))

    file_name = 'device_' + device.description + '.xml'
    xml_data = serializers.serialize("xml", [device])
    response = HttpResponse(xml_data, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    logger.info('XML config generated for the device id={}'.format(device_id))
    return response


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('description', 'mac', readable_cfg_last_update, get_dss_count, download_button)
    list_filter = ('customer', 'model')
    search_fields = ['mac', 'description', 'customer__description', 'model__name']
    actions = [download_xml]

    download_xml.short_description = 'Download XML Config'
    download_button.short_description = 'Download XML'
    download_button.allow_tags = True

    def get_urls(self):
        urls = super().get_urls()
        download_url = [
            url(
                r'^(?P<device_id>.+)/download-xml/$',
                self.admin_site.admin_view(download),
                name='download-xml',
            )
        ]
        return download_url + urls

