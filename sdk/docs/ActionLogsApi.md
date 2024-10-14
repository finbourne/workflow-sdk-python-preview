# lusid_workflow.ActionLogsApi

All URIs are relative to *https://www.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_action_logs**](ActionLogsApi.md#get_action_logs) | **GET** /api/actionlogs/{id} | [EXPERIMENTAL] GetActionLogs: Get the Action Logs for an Action Id


# **get_action_logs**
> ActionLog get_action_logs(id)

[EXPERIMENTAL] GetActionLogs: Get the Action Logs for an Action Id

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_workflow
from lusid_workflow.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/workflow
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_workflow.Configuration(
    host = "https://www.lusid.com/workflow"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_workflow.Configuration(
    host = "https://www.lusid.com/workflow"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_workflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_workflow.ActionLogsApi(api_client)
    id = 'id_example' # str | The Action Id

    try:
        # [EXPERIMENTAL] GetActionLogs: Get the Action Logs for an Action Id
        api_response = api_instance.get_action_logs(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ActionLogsApi->get_action_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Action Id | 

### Return type

[**ActionLog**](ActionLog.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | Action Log not found. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

