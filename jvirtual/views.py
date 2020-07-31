from django.shortcuts import render
from django.views import View
import pymysql
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.


class VirtualInfo(View):
    """
    虚拟机信息
    """
    def get(self, request):
        # print(request.method)
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root", password="1qaz!QAZ",
            database="machineadmin",
            charset="utf8")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = """select vmid,vmname,vmgroup,hostname,hostid,mem_size,num_vcpu,power_status,ip_address,total_storage,used_storage,description from vm_info"""
        cursor.execute(sql)
        data = cursor.fetchall()
        # print(data, type(data))
        # ret = json.dumps(data)
        # print(ret, type(ret))
        # 关闭连接
        cursor.close()
        conn.close()
        # print(data)
        # json_list = []
        # for i in data:
        #     json_dict = {}
        #     json_dict["vmid"] = i[0]
        #     json_dict["vmname"] = i[1]
        #     json_dict["vmgroup"] = i[2]
        #     json_dict["hostname"] = i[3]
        #     json_dict["hostid"] = i[4]
        #     json_dict["mem_size"] = i[5]
        #     json_dict["num_vcpu"] = i[6]
        #     json_dict["power_status"] = i[7]
        #     json_dict["ip_address"] = i[8]
        #     json_dict["total_storage"] = i[9]
        #     json_dict["used_storage"] = i[10]
        #     json_dict["description"] = i[11]

        #     json_list.append(json_dict)
        #
        # ret = json.dumps(json_list, ensure_ascii=False)
        # print(ret, type(ret))
        return JsonResponse(data, safe=False)
        # return HttpResponse('ok')



