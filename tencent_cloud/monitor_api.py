from tencentcloud.monitor.v20180724 import monitor_client, models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from typing import Callable
from util.get_time import get_current_time_YYYYmmddTHHMMSZ, timestamp_2_HHMM

import json


def get_metric_and_time(tencent_client, namespace, metric_name, dimensions, get_end_time_fn: Callable[[int], str]) -> (list, list):
    try:
        # 可观测平台api：GetMonitorDataRequest, 获取监控指标
        req = models.GetMonitorDataRequest()
        # 组装http请求体参数
        params = {
            "Namespace": namespace,
            "MetricName": metric_name,
            "Period": 3600,
            "StartTime": get_end_time_fn(),
            "EndTime": get_current_time_YYYYmmddTHHMMSZ(),
            "Instances": [
                {
                    "Dimensions": dimensions
                }
            ]
        }
        req.from_json_string(json.dumps(params))
        # 调用api, 返回数据
        resp = tencent_client.GetMonitorData(req)
        # 取出数据, 返回时间列表, 监控数据列表
        time_list, metric_data_list = resp.DataPoints[0].Timestamps, resp.DataPoints[0].Values
        time_list = [timestamp_2_HHMM(i) for i in time_list]
        return time_list, metric_data_list
    except TencentCloudSDKException as err:
        print(err)