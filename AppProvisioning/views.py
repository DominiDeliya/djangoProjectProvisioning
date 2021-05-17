import logging

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Customer, Extension, DeviceVendor, DeviceModel, Device, DSS
from .serializers import DeviceSerializer, CustomerSerializer, ExtensionSerializer, DeviceVendorSerializer, DeviceModelSerializer, DSSSerializer
from xml.etree.ElementTree import Element, SubElement, tostring

logger = logging.getLogger(__name__)


@csrf_exempt
def api_devices(request):
    if request.method == 'GET':
        logger.info('API Get all devices')
        devices_list = Device.objects.all()
        serializer = DeviceSerializer(devices_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        logger.info('API POST new devices')
        data = JSONParser().parse(request)
        serializer = DeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('API POST device data validated - save success')
            return JsonResponse(serializer.data, status=201)
        logger.warning('API POST device data - invalid data')
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def api_device(request, pk):
    try:
        device = Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        logging.warning('Unable to find the device with id={}'.format(pk))
        return HttpResponse(status=404)

    if request.method == 'GET':
        logger.info('API Get device with id={}'.format(pk))
        serializer = DeviceSerializer(device)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        logger.info('API update device with id={}'.format(pk))
        data = JSONParser().parse(request)
        serializer = DeviceSerializer(device, data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('API PUT device data validated - update success')
            return JsonResponse(serializer.data)
        logger.warning('API PUT device data - invalid data')
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        logger.info('API delete device with id={}'.format(pk))
        device.delete()
        return HttpResponse(status=204)


@csrf_exempt
def api_customers(request):
    if request.method == 'GET':
        logger.info('API Get all customers')
        customers_list = Customer.objects.all()
        serializer = CustomerSerializer(customers_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        logger.info('API POST new customers')
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('API POST customer data validated - save success')
            return JsonResponse(serializer.data, status=201)
        logger.warning('API POST customer data - invalid data')
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def api_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        logging.warning('Unable to find the customer with id={}'.format(pk))
        return HttpResponse(status=404)

    if request.method == 'GET':
        logger.info('API Get customer with id={}'.format(pk))
        serializer = CustomerSerializer(customer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        logger.info('API update customer with id={}'.format(pk))
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(customer, data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('API PUT customer data validated - update success')
            return JsonResponse(serializer.data)
        logger.warning('API PUT customer data - invalid data')
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        logger.info('API delete customer with id={}'.format(pk))
        customer.delete()
        return HttpResponse(status=204)


@csrf_exempt
def api_extensions(request):
    if request.method == 'GET':
        logger.info('API Get all extensions')
        extensions_list = Extension.objects.all()
        serializer = ExtensionSerializer(extensions_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        logger.info('API POST new extensions')
        data = JSONParser().parse(request)
        serializer = ExtensionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('API POST extension data validated - save success')
            return JsonResponse(serializer.data, status=201)
        logger.warning('API POST extension data - invalid data')
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def api_extension(request, pk):
    try:
        extension = Extension.objects.get(pk=pk)
    except Extension.DoesNotExist:
        logging.warning('Unable to find the extension with id={}'.format(pk))
        return HttpResponse(status=404)

    if request.method == 'GET':
        logger.info('API Get extension with id={}'.format(pk))
        serializer = ExtensionSerializer(extension)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        logger.info('API update extension with id={}'.format(pk))
        data = JSONParser().parse(request)
        serializer = ExtensionSerializer(extension, data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('API PUT extension data validated - update success')
            return JsonResponse(serializer.data)
        logger.warning('API PUT extension data - invalid data')
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        logger.info('API delete extension with id={}'.format(pk))
        extension.delete()
        return HttpResponse(status=204)


@csrf_exempt
def api_vendors(request):
    if request.method == 'GET':
        logger.info('API Get all vendors')
        vendors_list = DeviceVendor.objects.all()
        serializer = DeviceVendorSerializer(vendors_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        logger.info('API POST new vendors')
        data = JSONParser().parse(request)
        serializer = DeviceVendorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('API POST vendor data validated - save success')
            return JsonResponse(serializer.data, status=201)
        logger.warning('API POST vendor data - invalid data')
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def api_vendor(request, pk):
    try:
        vendor = DeviceVendor.objects.get(pk=pk)
    except DeviceVendor.DoesNotExist:
        logging.warning('Unable to find the vendor with id={}'.format(pk))
        return HttpResponse(status=404)

    if request.method == 'GET':
        logger.info('API Get vendor with id={}'.format(pk))
        serializer = DeviceVendorSerializer(vendor)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        logger.info('API update vendor with id={}'.format(pk))
        data = JSONParser().parse(request)
        serializer = DeviceVendorSerializer(vendor, data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('API PUT vendor data validated - update success')
            return JsonResponse(serializer.data)
        logger.warning('API PUT vendor data - invalid data')
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        logger.info('API delete vendor with id={}'.format(pk))
        vendor.delete()
        return HttpResponse(status=204)


@csrf_exempt
def api_models(request):
    if request.method == 'GET':
        logger.info('API Get all models')
        models_list = DeviceModel.objects.all()
        serializer = DeviceModelSerializer(models_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        logger.info('API POST new models')
        data = JSONParser().parse(request)
        serializer = DeviceModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('API POST model data validated - save success')
            return JsonResponse(serializer.data, status=201)
        logger.warning('API POST model data - invalid data')
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def api_model(request, pk):
    try:
        model = DeviceModel.objects.get(pk=pk)
    except DeviceModel.DoesNotExist:
        logging.warning('Unable to find the model with id={}'.format(pk))
        return HttpResponse(status=404)

    if request.method == 'GET':
        logger.info('API Get model with id={}'.format(pk))
        serializer = DeviceModelSerializer(model)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        logger.info('API update model with id={}'.format(pk))
        data = JSONParser().parse(request)
        serializer = DeviceModelSerializer(model, data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('API PUT model data validated - update success')
            return JsonResponse(serializer.data)
        logger.warning('API PUT model data - invalid data')
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        logger.info('API delete model with id={}'.format(pk))
        model.delete()
        return HttpResponse(status=204)


@csrf_exempt
def api_dsss(request):
    if request.method == 'GET':
        logger.info('API Get all dsss')
        dsss_list = DSS.objects.all()
        serializer = DSSSerializer(dsss_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        logger.info('API POST new dsss')
        data = JSONParser().parse(request)
        serializer = DSSSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('API POST dss data validated - save success')
            return JsonResponse(serializer.data, status=201)
        logger.warning('API POST dss data - invalid data')
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def api_dss(request, pk):
    try:
        dss = DSS.objects.get(pk=pk)
    except DSS.DoesNotExist:
        logging.warning('Unable to find the DSS with id={}'.format(pk))
        return HttpResponse(status=404)

    if request.method == 'GET':
        logger.info('API Get DSS with id={}'.format(pk))
        serializer = DSSSerializer(dss)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        logger.info('API update DSS with id={}'.format(pk))
        data = JSONParser().parse(request)
        serializer = DSSSerializer(dss, data=data)
        if serializer.is_valid():
            serializer.save()
            logger.info('API PUT DSS data validated - update success')
            return JsonResponse(serializer.data)
        logger.warning('API PUT DSS data - invalid data')
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        logger.info('API delete DSS with id={}'.format(pk))
        dss.delete()
        return HttpResponse(status=204)



@csrf_exempt
def api_device_mac(request, mac):
    try:
        device = Device.objects.get(mac=mac)
    except Device.DoesNotExist:
        logging.warning('Unable to find the device with mac={}'.format(mac))
        return HttpResponse(status=404)

    if request.method == 'GET':
        logger.info('API Get device with mac={}'.format(mac))
        xml_data = generate_xml_content(device)
        return HttpResponse(xml_data, content_type='text/xml')
    return HttpResponse(status=406)


def generate_xml_content(device):
    settings_tag = Element('settings')

    phone_settings_tag = SubElement(settings_tag, 'phone-settings')

    customer_tag = SubElement(phone_settings_tag, 'customer')
    customer_tag.text = device.customer.description

    description_tag = SubElement(phone_settings_tag, 'description')
    description_tag.text = device.description

    mac_tag = SubElement(phone_settings_tag, 'mac')
    mac_tag.text = device.mac

    dss_tag = SubElement(phone_settings_tag, 'dss')
    dss_list = DSS.objects.filter(devices=device.id)

    for dss in dss_list:
        value_tag = SubElement(dss_tag, 'value.{}'.format(dss.key))
        value_tag.text = dss.value

        label_tag = SubElement(dss_tag, 'label.{}'.format(dss.key))
        label_tag.text = dss.label

        type_tag = SubElement(dss_tag, 'type.{}'.format(dss.key))
        type_tag.text = dss.dss_type

    return tostring(settings_tag, encoding='utf-8', xml_declaration=True)
