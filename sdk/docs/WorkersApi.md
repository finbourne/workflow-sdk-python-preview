# lusid_workflow.WorkersApi

All URIs are relative to *https://www.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_worker**](WorkersApi.md#create_worker) | **POST** /api/workers | [EXPERIMENTAL] CreateWorker: Endpoint For Creating a Worker
[**get_worker**](WorkersApi.md#get_worker) | **GET** /api/workers/{scope}/{code} | [EXPERIMENTAL] GetWorker: Endpoint for Retrieving a Worker


# **create_worker**
> Worker create_worker(create_worker_request)

[EXPERIMENTAL] CreateWorker: Endpoint For Creating a Worker

If the Worker already exists a failure will be returned

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
    api_instance = lusid_workflow.WorkersApi(api_client)
    create_worker_request = {"id":{"scope":"Quotes","code":"QuoteExceptionWorker"},"displayName":"Quote data quality worker","description":"Find erroneous quotes after quotes inserted","workerConfiguration":{"viewName":"Views.QuoteExceptionProvider","type":"LuminesceView"}} # CreateWorkerRequest | Worker to be created

    try:
        # [EXPERIMENTAL] CreateWorker: Endpoint For Creating a Worker
        api_response = api_instance.create_worker(create_worker_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkersApi->create_worker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_worker_request** | [**CreateWorkerRequest**](CreateWorkerRequest.md)| Worker to be created | 

### Return type

[**Worker**](Worker.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_worker**
> Worker get_worker(scope, code, as_at=as_at)

[EXPERIMENTAL] GetWorker: Endpoint for Retrieving a Worker

Will return a NotFound failure if the Worker does not exist

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
    api_instance = lusid_workflow.WorkersApi(api_client)
    scope = 'scope_example' # str | Scope of the worker
code = 'code_example' # str | Code of the worker
as_at = '2013-10-20T19:20:30+01:00' # datetime | AsAt time of the worker (optional)

    try:
        # [EXPERIMENTAL] GetWorker: Endpoint for Retrieving a Worker
        api_response = api_instance.get_worker(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkersApi->get_worker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the worker | 
 **code** | **str**| Code of the worker | 
 **as_at** | **datetime**| AsAt time of the worker | [optional] 

### Return type

[**Worker**](Worker.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

