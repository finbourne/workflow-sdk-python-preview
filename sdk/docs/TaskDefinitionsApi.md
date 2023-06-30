# lusid_workflow.TaskDefinitionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_definition**](TaskDefinitionsApi.md#create_task_definition) | **POST** /api/taskdefinitions | [EXPERIMENTAL] CreateTaskDefinition: Create a new Task Definition
[**delete_task_definition**](TaskDefinitionsApi.md#delete_task_definition) | **DELETE** /api/taskdefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteTaskDefinition: Delete a Task Definition
[**get_task_definition**](TaskDefinitionsApi.md#get_task_definition) | **GET** /api/taskdefinitions/{scope}/{code} | [EXPERIMENTAL] GetTaskDefinition: Get a Task Definition
[**list_task_definitions**](TaskDefinitionsApi.md#list_task_definitions) | **GET** /api/taskdefinitions | [EXPERIMENTAL] ListTaskDefinitions: List Task Definitions
[**list_tasks_for_task_definition**](TaskDefinitionsApi.md#list_tasks_for_task_definition) | **GET** /api/taskdefinitions/{scope}/{code}/tasks | [EXPERIMENTAL] ListTasksForTaskDefinition: List Tasks for a Task Definition
[**update_task_definition**](TaskDefinitionsApi.md#update_task_definition) | **PUT** /api/taskdefinitions/{scope}/{code} | [EXPERIMENTAL] UpdateTaskDefinition: Update an existing Task Definition


# **create_task_definition**
> TaskDefinition create_task_definition(create_task_definition_request)

[EXPERIMENTAL] CreateTaskDefinition: Create a new Task Definition

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_workflow
from lusid_workflow.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_workflow.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_workflow.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_workflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_workflow.TaskDefinitionsApi(api_client)
    create_task_definition_request = {"id":{"scope":"A1","code":"ZZZ"},"displayName":"An example TaskDefinition","description":"Test","states":[{"name":"Submitted"},{"name":"InProgress"},{"name":"SendingSurvey"},{"name":"Done"},{"name":"SurveyNotSent"},{"name":"NotDone"}],"fieldSchema":[{"name":"clientId","type":"String"},{"name":"assignee","type":"String"},{"name":"resolutionDetail","type":"String"}],"initialState":{"name":"Submitted","requiredFields":["clientId"]},"triggers":[{"name":"start","trigger":{"type":"External"}},{"name":"cancel","trigger":{"type":"External"}},{"name":"resolve","trigger":{"type":"External"}},{"name":"timeout","trigger":{"type":"External"}},{"name":"success","trigger":{"type":"External"}},{"name":"failure","trigger":{"type":"External"}}],"transitions":[{"fromState":"Submitted","toState":"InProgress","trigger":"start","guard":"fields['assignee'] exists AND fields['assignee'] NOT eq ''"},{"fromState":"InProgress","toState":"SendingSurvey","trigger":"resolve","guard":"fields['resolutionDetail'] exists AND fields['resolutionDetail'] NOT eq ''","action":"health-check"},{"fromState":"SendingSurvey","toState":"Done","trigger":"success"},{"fromState":"SendingSurvey","toState":"SurveyNotSent","trigger":"failure"},{"fromState":"SendingSurvey","toState":"NotDone","trigger":"timeout"},{"fromState":"InProgress","toState":"NotDone","trigger":"cancel","guard":"fields['cancellationDetail'] exists AND fields['cancellationDetail'] NOT eq ''"}],"actions":[{"name":"health-check","actionDetails":{"type":"RunWorker","workerId":{"scope":"Health","code":"HealthCheckWorker"},"workerAsAt":"2022-01-01T01:02:03.0000000+00:00","workerParameters":{},"workerStatusTriggers":{},"childTaskConfigurations":[{"taskDefinitionId":{"scope":"AAA","code":"BBB"},"initialTrigger":"test-trigger","childTaskFields":{"assignee":{"mapFrom":"foo","setTo":"bar"}}}]}}]} # CreateTaskDefinitionRequest | The data to create a Task Definition

    try:
        # [EXPERIMENTAL] CreateTaskDefinition: Create a new Task Definition
        api_response = api_instance.create_task_definition(create_task_definition_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskDefinitionsApi->create_task_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_task_definition_request** | [**CreateTaskDefinitionRequest**](CreateTaskDefinitionRequest.md)| The data to create a Task Definition | 

### Return type

[**TaskDefinition**](TaskDefinition.md)

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

# **delete_task_definition**
> DeletedEntityResponse delete_task_definition(scope, code)

[EXPERIMENTAL] DeleteTaskDefinition: Delete a Task Definition

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_workflow
from lusid_workflow.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_workflow.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_workflow.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_workflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_workflow.TaskDefinitionsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a Task Definition
code = 'code_example' # str | The code that identifies a Task Definition

    try:
        # [EXPERIMENTAL] DeleteTaskDefinition: Delete a Task Definition
        api_response = api_instance.delete_task_definition(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskDefinitionsApi->delete_task_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Task Definition | 
 **code** | **str**| The code that identifies a Task Definition | 

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
**404** | Task Definition not found. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_definition**
> TaskDefinition get_task_definition(scope, code, as_at=as_at)

[EXPERIMENTAL] GetTaskDefinition: Get a Task Definition

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_workflow
from lusid_workflow.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_workflow.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_workflow.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_workflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_workflow.TaskDefinitionsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a Task Definition
code = 'code_example' # str | The code that identifies a Task Definition
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Task Definition. Defaults to returning the latest version of the Task Definition if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetTaskDefinition: Get a Task Definition
        api_response = api_instance.get_task_definition(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskDefinitionsApi->get_task_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Task Definition | 
 **code** | **str**| The code that identifies a Task Definition | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Task Definition. Defaults to returning the latest version of the Task Definition if not specified. | [optional] 

### Return type

[**TaskDefinition**](TaskDefinition.md)

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
**404** | Task Definition not found. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_task_definitions**
> PagedResourceListOfTaskDefinition list_task_definitions(as_at=as_at, limit=limit, page=page)

[EXPERIMENTAL] ListTaskDefinitions: List Task Definitions

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_workflow
from lusid_workflow.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_workflow.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_workflow.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_workflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_workflow.TaskDefinitionsApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Task Definitions. Defaults to return the latest version of each Task Definition if not specified. (optional)
limit = 10 # int | When paginating, limit the number of returned results to this many. (optional) (default to 10)
page = 'page_example' # str | The pagination token to use to continue listing task definitions from a previous call to list task definitions. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. (optional)

    try:
        # [EXPERIMENTAL] ListTaskDefinitions: List Task Definitions
        api_response = api_instance.list_task_definitions(as_at=as_at, limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskDefinitionsApi->list_task_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Task Definitions. Defaults to return the latest version of each Task Definition if not specified. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] [default to 10]
 **page** | **str**| The pagination token to use to continue listing task definitions from a previous call to list task definitions. This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields must not have changed since the original request. | [optional] 

### Return type

[**PagedResourceListOfTaskDefinition**](PagedResourceListOfTaskDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Task Definitions |  -  |
**400** | The details of the input related failure |  -  |
**404** | No Task Definitions found. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks_for_task_definition**
> ResourceListOfTask list_tasks_for_task_definition(scope, code, as_at=as_at)

[EXPERIMENTAL] ListTasksForTaskDefinition: List Tasks for a Task Definition

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_workflow
from lusid_workflow.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_workflow.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_workflow.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_workflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_workflow.TaskDefinitionsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a Task Definition
code = 'code_example' # str | The code that identifies a Task Definition
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Tasks. Defaults to return the latest version of each Task if not specified. (optional)

    try:
        # [EXPERIMENTAL] ListTasksForTaskDefinition: List Tasks for a Task Definition
        api_response = api_instance.list_tasks_for_task_definition(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskDefinitionsApi->list_tasks_for_task_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Task Definition | 
 **code** | **str**| The code that identifies a Task Definition | 
 **as_at** | **datetime**| The asAt datetime at which to list the Tasks. Defaults to return the latest version of each Task if not specified. | [optional] 

### Return type

[**ResourceListOfTask**](ResourceListOfTask.md)

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
**404** | No tasks found for this Task Definition. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_definition**
> TaskDefinition update_task_definition(scope, code, update_task_definition_request)

[EXPERIMENTAL] UpdateTaskDefinition: Update an existing Task Definition

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_workflow
from lusid_workflow.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_workflow.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_workflow.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_workflow.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_workflow.TaskDefinitionsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a Task Definition
code = 'code_example' # str | The code that identifies a Task Definition
update_task_definition_request = {"displayName":"An example TaskDefinition","description":"Test","states":[{"name":"Submitted"},{"name":"InProgress"},{"name":"SendingSurvey"},{"name":"Done"},{"name":"SurveyNotSent"},{"name":"NotDone"}],"fieldSchema":[{"name":"clientId","type":"String"},{"name":"assignee","type":"String"},{"name":"resolutionDetail","type":"String"}],"initialState":{"name":"Submitted","requiredFields":["clientId"]},"triggers":[{"name":"start","trigger":{"type":"External"}},{"name":"cancel","trigger":{"type":"External"}},{"name":"resolve","trigger":{"type":"External"}},{"name":"timeout","trigger":{"type":"External"}},{"name":"success","trigger":{"type":"External"}},{"name":"failure","trigger":{"type":"External"}}],"transitions":[{"fromState":"Submitted","toState":"InProgress","trigger":"start","guard":"fields['assignee'] exists AND fields['assignee'] NOT eq ''"},{"fromState":"InProgress","toState":"SendingSurvey","trigger":"resolve","guard":"fields['resolutionDetail'] exists AND fields['resolutionDetail'] NOT eq ''","action":"health-check"},{"fromState":"SendingSurvey","toState":"Done","trigger":"success"},{"fromState":"SendingSurvey","toState":"SurveyNotSent","trigger":"failure"},{"fromState":"SendingSurvey","toState":"NotDone","trigger":"timeout"},{"fromState":"InProgress","toState":"NotDone","trigger":"cancel","guard":"fields['cancellationDetail'] exists AND fields['cancellationDetail'] NOT eq ''"}],"actions":[{"name":"health-check","actionDetails":{"type":"RunWorker","workerId":{"scope":"Health","code":"HealthCheckWorker"},"workerAsAt":"2022-01-01T01:02:03.0000000+00:00","workerParameters":{},"workerStatusTriggers":{},"childTaskConfigurations":[{"taskDefinitionId":{"scope":"AAA","code":"BBB"},"initialTrigger":"test-trigger","childTaskFields":{"assignee":{"mapFrom":"foo","setTo":"bar"}}}]}}]} # UpdateTaskDefinitionRequest | The data to update a Task Definition

    try:
        # [EXPERIMENTAL] UpdateTaskDefinition: Update an existing Task Definition
        api_response = api_instance.update_task_definition(scope, code, update_task_definition_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskDefinitionsApi->update_task_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope that identifies a Task Definition | 
 **code** | **str**| The code that identifies a Task Definition | 
 **update_task_definition_request** | [**UpdateTaskDefinitionRequest**](UpdateTaskDefinitionRequest.md)| The data to update a Task Definition | 

### Return type

[**TaskDefinition**](TaskDefinition.md)

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
**404** | Task Definition not found. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

