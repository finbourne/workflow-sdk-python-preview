# lusid_workflow.WorkersApi

All URIs are relative to *https://www.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_worker**](WorkersApi.md#create_worker) | **POST** /api/workers | [EXPERIMENTAL] CreateWorker: Create a new Worker
[**get_worker**](WorkersApi.md#get_worker) | **GET** /api/workers/{scope}/{code} | [EXPERIMENTAL] GetWorker: Get a Worker
[**list_workers**](WorkersApi.md#list_workers) | **GET** /api/workers | [EXPERIMENTAL] ListWorkers: List Workers
[**run_worker**](WorkersApi.md#run_worker) | **POST** /api/workers/{scope}/{code}/$run | [EXPERIMENTAL] RunWorker: Run a Worker


# **create_worker**
> Worker create_worker(create_worker_request)

[EXPERIMENTAL] CreateWorker: Create a new Worker

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
    create_worker_request = {"id":{"scope":"Health","code":"HealthCheckWorker"},"displayName":"ASP.Net Health Check worker","description":"Calls /health to check a service is running","workerConfiguration":{"type":"HealthCheck","url":"http://localhost.lusid.com:8282"}} # CreateWorkerRequest | Worker to be created

    try:
        # [EXPERIMENTAL] CreateWorker: Create a new Worker
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

[EXPERIMENTAL] GetWorker: Get a Worker

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
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Worker. Defaults to returning the latest version of the Worker if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetWorker: Get a Worker
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
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Worker. Defaults to returning the latest version of the Worker if not specified. | [optional] 

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

# **list_workers**
> PagedResourceListOfWorker list_workers(as_at=as_at, limit=limit, page=page)

[EXPERIMENTAL] ListWorkers: List Workers

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
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Workers. Defaults to return the latest version of each Worker if not specified. (optional)
limit = 10 # int | When paginating, limit the number of returned results to this many. (optional) (default to 10)
page = 'page_example' # str | The pagination token to use to continue listing workers from a previous call to list workers. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)

    try:
        # [EXPERIMENTAL] ListWorkers: List Workers
        api_response = api_instance.list_workers(as_at=as_at, limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkersApi->list_workers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Workers. Defaults to return the latest version of each Worker if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing workers from a previous call to list workers. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfWorker**](PagedResourceListOfWorker.md)

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

# **run_worker**
> RunWorkerResponse run_worker(scope, code, run_worker_request, as_at=as_at)

[EXPERIMENTAL] RunWorker: Run a Worker

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
run_worker_request = {"parameters":[{"name":"test-parameter","value":true}]} # RunWorkerRequest | 
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Worker. Defaults to returning the latest version of the Worker if not specified. (optional)

    try:
        # [EXPERIMENTAL] RunWorker: Run a Worker
        api_response = api_instance.run_worker(scope, code, run_worker_request, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkersApi->run_worker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the worker | 
 **code** | **str**| Code of the worker | 
 **run_worker_request** | [**RunWorkerRequest**](RunWorkerRequest.md)|  | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Worker. Defaults to returning the latest version of the Worker if not specified. | [optional] 

### Return type

[**RunWorkerResponse**](RunWorkerResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

