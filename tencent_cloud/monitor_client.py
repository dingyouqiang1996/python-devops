from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.monitor.v20180724 import monitor_client, models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

def get_tencent_cloud_monitor_platform_client(ak, sk, region) -> monitor_client.MonitorClient:
    try:
        cred = credential.Credential(ak, sk)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "monitor.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = monitor_client.MonitorClient(cred, region, clientProfile)
        return client
    except TencentCloudSDKException as err:
        print(err)