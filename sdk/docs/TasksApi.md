# lusid_workflow.TasksApi

All URIs are relative to *https://www.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](TasksApi.md#create_task) | **POST** /api/tasks | [EXPERIMENTAL] CreateTask: Create a new Task
[**delete_task**](TasksApi.md#delete_task) | **DELETE** /api/tasks/{id} | [EXPERIMENTAL] DeleteTask: Delete a Task
[**get_task**](TasksApi.md#get_task) | **GET** /api/tasks/{id} | [EXPERIMENTAL] GetTask: Get a Task
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /api/tasks | [EXPERIMENTAL] ListTasks: List Tasks
[**update_task**](TasksApi.md#update_task) | **POST** /api/tasks/{id} | [EXPERIMENTAL] UpdateTask: Update a Task


# **create_task**
> Task create_task(create_task_request, trigger=trigger)

[EXPERIMENTAL] CreateTask: Create a new Task

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
    api_instance = lusid_workflow.TasksApi(api_client)
    create_task_request = {"taskDefinitionId":{"scope":"A1","code":"ZZZ"},"correlationIds":["correlation-id"],"fields":[{"name":"clientId","value":"zzz123"},{"name":"assignee"},{"name":"resolutionDetail","value":""}]} # CreateTaskRequest | Request to create Task
trigger = 'trigger_example' # str | The name of the Trigger to invoke (optional)

    try:
        # [EXPERIMENTAL] CreateTask: Create a new Task
        api_response = api_instance.create_task(create_task_request, trigger=trigger)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_task_request** | [**CreateTaskRequest**](CreateTaskRequest.md)| Request to create Task | 
 **trigger** | **str**| The name of the Trigger to invoke | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> DeletedEntityResponse delete_task(id)

[EXPERIMENTAL] DeleteTask: Delete a Task

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
    api_instance = lusid_workflow.TasksApi(api_client)
    id = 'id_example' # str | The identifier for the Task to be deleted.

    try:
        # [EXPERIMENTAL] DeleteTask: Delete a Task
        api_response = api_instance.delete_task(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier for the Task to be deleted. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

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
**404** | Task not found. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> Task get_task(id, as_at=as_at)

[EXPERIMENTAL] GetTask: Get a Task

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
    api_instance = lusid_workflow.TasksApi(api_client)
    id = 'id_example' # str | Id of the Task to retrieve
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Task. Defaults to returning the latest version of the Task if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetTask: Get a Task
        api_response = api_instance.get_task(id, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Task to retrieve | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Task. Defaults to returning the latest version of the Task if not specified. | [optional] 

### Return type

[**Task**](Task.md)

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
**404** | Task not found. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> PagedResourceListOfTask list_tasks(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)

[EXPERIMENTAL] ListTasks: List Tasks

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
    api_instance = lusid_workflow.TasksApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Tasks. Defaults to return the latest version of each Task if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. (optional)
sort_by = ['sort_by_example'] # list[str] | A list of field names or properties to sort by, each optionally suffixed by \" ASC\" or \" DESC\" (optional)
limit = 10 # int | When paginating, limit the number of returned results to this many. (optional) (default to 10)
page = 'page_example' # str | The pagination token to use to continue listing tasks from a previous call to list tasks. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)

    try:
        # [EXPERIMENTAL] ListTasks: List Tasks
        api_response = api_instance.list_tasks(as_at=as_at, filter=filter, sort_by=sort_by, limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->list_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Tasks. Defaults to return the latest version of each Task if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here: https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**list[str]**](str.md)| A list of field names or properties to sort by, each optionally suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing tasks from a previous call to list tasks. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfTask**](PagedResourceListOfTask.md)

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
**404** | No Tasks found. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> Task update_task(id, trigger=trigger, update_task_request=update_task_request)

[EXPERIMENTAL] UpdateTask: Update a Task

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
    api_instance = lusid_workflow.TasksApi(api_client)
    id = 'id_example' # str | Id of the Task to act upon
trigger = 'trigger_example' # str |  (optional)
update_task_request = {"fields":[{"name":"clientId","value":"zzz123"},{"name":"assignee","value":"bob"},{"name":"resolutionDetail","value":""}]} # UpdateTaskRequest | The details of the request (optional)

    try:
        # [EXPERIMENTAL] UpdateTask: Update a Task
        api_response = api_instance.update_task(id, trigger=trigger, update_task_request=update_task_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TasksApi->update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the Task to act upon | 
 **trigger** | **str**|  | [optional] 
 **update_task_request** | [**UpdateTaskRequest**](UpdateTaskRequest.md)| The details of the request | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | Task not found. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

