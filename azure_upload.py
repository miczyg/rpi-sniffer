import os

connection_string = "DefaultEndpointsProtocol=https;AccountName=rpisniffer;AccountKey=WaLsgJS5D4CSZXf6Kdgh98UmLDC62PcU+djuibV+v8MOrX/zTaehQrA99i9QDtNHZpQqr0aYJbcytNZKl4WrCg==;EndpointSuffix=core.windows.net"
container = "sniff-test01"

os.system("export AZURE_STORAGE_CONNECTION_STRING={connection_string}".format(connection_string))



