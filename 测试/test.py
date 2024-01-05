from tencent_cloud.monitor_client import get_tencent_cloud_monitor_platform_client
from tencent_cloud.monitor_api import get_metric_and_time
from util.get_time import get_ndays_ago_time_YYYYmmddTHHMMSZ

if __name__ == '__main__':
    ak = input("请输入ak: ")
    sk = input("请输入sk: ")
    region = "ap-guangzhou"
    namespace = "QCE/CVM"
    dimensions = [{'Name': 'InstanceId', 'Value': 'ins-afhblg4q'}]
    client = get_tencent_cloud_monitor_platform_client(ak, sk, region)
    print(get_metric_and_time(client, namespace, 'CpuUsage', dimensions, get_ndays_ago_time_YYYYmmddTHHMMSZ))