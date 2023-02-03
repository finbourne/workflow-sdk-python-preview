# lusid_workflow.UpdatesApi

All URIs are relative to *https://www.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_raise**](UpdatesApi.md#call_raise) | **POST** /api/updates | [EXPERIMENTAL] Raise: Process an inbound Update.


# **call_raise**
> call_raise(scope, update_task_request)

[EXPERIMENTAL] Raise: Process an inbound Update.

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
    api_instance = lusid_workflow.UpdatesApi(api_client)
    scope = 'scope_example' # str | 
update_task_request = {"field":"fieldName","value":"aaa"} # UpdateTaskRequest | Update request

    try:
        # [EXPERIMENTAL] Raise: Process an inbound Update.
        api_instance.call_raise(scope, update_task_request)
    except ApiException as e:
        print("Exception when calling UpdatesApi->call_raise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **update_task_request** | [**UpdateTaskRequest**](UpdateTaskRequest.md)| Update request | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

