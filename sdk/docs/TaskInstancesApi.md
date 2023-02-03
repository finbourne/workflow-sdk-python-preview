# lusid_workflow.TaskInstancesApi

All URIs are relative to *https://www.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task_instance**](TaskInstancesApi.md#get_task_instance) | **GET** /api/taskinstances/{id} | [EXPERIMENTAL] GetTaskInstance: Get a Task Instance.


# **get_task_instance**
> TaskInstance get_task_instance(id, as_at=as_at, task_instance_scope=task_instance_scope)

[EXPERIMENTAL] GetTaskInstance: Get a Task Instance.

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
    api_instance = lusid_workflow.TaskInstancesApi(api_client)
    id = 'id_example' # str | Id of the task instance to retrieve
as_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
task_instance_scope = 'default' # str | The scope of the task instance to retrieve from; 'default' if not provided. (optional) (default to 'default')

    try:
        # [EXPERIMENTAL] GetTaskInstance: Get a Task Instance.
        api_response = api_instance.get_task_instance(id, as_at=as_at, task_instance_scope=task_instance_scope)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskInstancesApi->get_task_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the task instance to retrieve | 
 **as_at** | **datetime**|  | [optional] 
 **task_instance_scope** | **str**| The scope of the task instance to retrieve from; &#39;default&#39; if not provided. | [optional] [default to &#39;default&#39;]

### Return type

[**TaskInstance**](TaskInstance.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No Task Instance exists in current scope |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

