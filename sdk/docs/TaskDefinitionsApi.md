# lusid_workflow.TaskDefinitionsApi

All URIs are relative to *https://www.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_definition**](TaskDefinitionsApi.md#create_task_definition) | **POST** /api/taskdefinitions | [EXPERIMENTAL] CreateTaskDefinition: Create a new Task Definition.
[**create_task_instance**](TaskDefinitionsApi.md#create_task_instance) | **POST** /api/taskdefinitions/{scope}/{code} | [EXPERIMENTAL] CreateTaskInstance: Create a new Task Instance.
[**delete_task_definition**](TaskDefinitionsApi.md#delete_task_definition) | **DELETE** /api/taskdefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteTaskDefinition: Delete a Task Definition.
[**get_task_definition**](TaskDefinitionsApi.md#get_task_definition) | **GET** /api/taskdefinitions/{scope}/{code} | [EXPERIMENTAL] GetTaskDefinition: Get a Task Definition.
[**get_task_instances_for_definition**](TaskDefinitionsApi.md#get_task_instances_for_definition) | **GET** /api/taskdefinitions/{scope}/{code}/instances | [EXPERIMENTAL] GetTaskInstancesForDefinition: Get all Task Instances based on a Task Definition
[**update_task_definition**](TaskDefinitionsApi.md#update_task_definition) | **PUT** /api/taskdefinitions/{scope}/{code} | [EXPERIMENTAL] UpdateTaskDefinition: Update an existing Task Definition.


# **create_task_definition**
> TaskDefinition create_task_definition(create_task_definition_request)

[EXPERIMENTAL] CreateTaskDefinition: Create a new Task Definition.

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
    api_instance = lusid_workflow.TaskDefinitionsApi(api_client)
    create_task_definition_request = {"id":{"scope":"A1","code":"ZZZ"},"displayName":"An example TaskDefinition","description":"Test","fields":[{"name":"assignee","type":"String"},{"name":"resolutionDetail","type":"String"}],"states":[{"type":"Input","name":"Submitted"},{"type":"Internal","name":"InProgress"},{"type":"Internal","name":"SendingSurvey"},{"type":"Output","name":"Done"},{"type":"Output","name":"SurveyNotSent"},{"type":"Output","name":"NotDone"}],"transitions":[{"from":"Submitted","to":"InProgress","trigger":"start","guard":"fields.assignee exists AND fields.assignee NOT eq ''"},{"from":"InProgress","to":"SendingSurvey","trigger":"resolve","guard":"fields.resolutionDetail exists AND fields.resolutionDetail NOT eq ''","output":"sendSurvey"},{"from":"SendingSurvey","to":"Done","trigger":"success"},{"from":"SendingSurvey","to":"SurveyNotSent","trigger":"failure"},{"from":"SendingSurvey","to":"NotDone","trigger":"timeout"},{"from":"InProgress","to":"NotDone","trigger":"cancel","guard":"fields.cancellationDetail exists AND fields.cancellationDetail NOT eq ''"}],"triggers":[{"name":"start","schema":{"type":"Manual","timeInState":0}},{"name":"cancel","schema":{"type":"Manual","timeInState":0}},{"name":"resolve","schema":{"type":"Manual","timeInState":0}},{"name":"timeout","schema":{"type":"Timeout","timeInState":30}},{"name":"success","schema":{"type":"WebHook","timeInState":0,"responseCodes":{"in":[200]}}},{"name":"failure","schema":{"type":"WebHook","timeInState":0,"responseCodes":{"notIn":[200]}}}],"initialState":{"name":"Submitted","requiredFields":["clientId","description"]},"outputs":[{"name":"a web hook","schema":{"requestDetails":{"method":"Get","url":"www.zzz.com","parameters":[{"kind":"Query","key":"client_id","value":"ZZZ"}],"expectedHttpResponseCodes":["200"]},"type":"WebHook"}}]} # CreateTaskDefinitionRequest | The data to create a Task Definition

    try:
        # [EXPERIMENTAL] CreateTaskDefinition: Create a new Task Definition.
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
**201** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task_instance**
> TaskInstance create_task_instance(scope, code, create_task_instance_request, task_instance_scope=task_instance_scope)

[EXPERIMENTAL] CreateTaskInstance: Create a new Task Instance.

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
    api_instance = lusid_workflow.TaskDefinitionsApi(api_client)
    scope = 'scope_example' # str | The scope of task definition to create task instance from
code = 'code_example' # str | The code of task definition to create a task instance from
create_task_instance_request = {"correlationId":"correlation-id"} # CreateTaskInstanceRequest | Request to create task instance
task_instance_scope = 'default' # str | The scope of the task instance should be in; set to 'default' if not provided. (optional) (default to 'default')

    try:
        # [EXPERIMENTAL] CreateTaskInstance: Create a new Task Instance.
        api_response = api_instance.create_task_instance(scope, code, create_task_instance_request, task_instance_scope=task_instance_scope)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskDefinitionsApi->create_task_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of task definition to create task instance from | 
 **code** | **str**| The code of task definition to create a task instance from | 
 **create_task_instance_request** | [**CreateTaskInstanceRequest**](CreateTaskInstanceRequest.md)| Request to create task instance | 
 **task_instance_scope** | **str**| The scope of the task instance should be in; set to &#39;default&#39; if not provided. | [optional] [default to &#39;default&#39;]

### Return type

[**TaskInstance**](TaskInstance.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task_definition**
> DeletedEntityResponse delete_task_definition(scope, code)

[EXPERIMENTAL] DeleteTaskDefinition: Delete a Task Definition.

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
    api_instance = lusid_workflow.TaskDefinitionsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a Task Definition
code = 'code_example' # str | The code that identifies a Task Definition

    try:
        # [EXPERIMENTAL] DeleteTaskDefinition: Delete a Task Definition.
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
**404** | No task definition exists in current scope |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_definition**
> TaskDefinition get_task_definition(scope, code, as_at=as_at)

[EXPERIMENTAL] GetTaskDefinition: Get a Task Definition.

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
    api_instance = lusid_workflow.TaskDefinitionsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a Task Definition
code = 'code_example' # str | The code that identifies a Task Definition
as_at = '2013-10-20T19:20:30+01:00' # datetime | AsAt time to retrieve stated Task Definition. Default to current time if not provided. (optional)

    try:
        # [EXPERIMENTAL] GetTaskDefinition: Get a Task Definition.
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
 **as_at** | **datetime**| AsAt time to retrieve stated Task Definition. Default to current time if not provided. | [optional] 

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
**404** | No task definition exists in current scope |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_instances_for_definition**
> ResourceListOfTaskInstance get_task_instances_for_definition(scope, code, as_at=as_at)

[EXPERIMENTAL] GetTaskInstancesForDefinition: Get all Task Instances based on a Task Definition

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
    api_instance = lusid_workflow.TaskDefinitionsApi(api_client)
    scope = 'scope_example' # str | The scope of the source Task Definition and the Task Instances so be searched under.
code = 'code_example' # str | The code that identifies the source Task Definition
as_at = '2013-10-20T19:20:30+01:00' # datetime | AsAt time to retrieve stated Task Instances. Default to latest AsAt if not provided. (optional)

    try:
        # [EXPERIMENTAL] GetTaskInstancesForDefinition: Get all Task Instances based on a Task Definition
        api_response = api_instance.get_task_instances_for_definition(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskDefinitionsApi->get_task_instances_for_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the source Task Definition and the Task Instances so be searched under. | 
 **code** | **str**| The code that identifies the source Task Definition | 
 **as_at** | **datetime**| AsAt time to retrieve stated Task Instances. Default to latest AsAt if not provided. | [optional] 

### Return type

[**ResourceListOfTaskInstance**](ResourceListOfTaskInstance.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Task Instances which share the requested Definition |  -  |
**400** | The details of the input related failure |  -  |
**404** | No Task Instances found in current scope for this Definition |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_definition**
> TaskDefinition update_task_definition(scope, code, update_task_definition_request)

[EXPERIMENTAL] UpdateTaskDefinition: Update an existing Task Definition.

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
    api_instance = lusid_workflow.TaskDefinitionsApi(api_client)
    scope = 'scope_example' # str | The scope that identifies a Task Definition
code = 'code_example' # str | The code that identifies a Task Definition
update_task_definition_request = {"displayName":"bar","description":"foo","fields":[{"name":"foo","type":"Boolean"}]} # UpdateTaskDefinitionRequest | The data to update a Task Definition

    try:
        # [EXPERIMENTAL] UpdateTaskDefinition: Update an existing Task Definition.
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
**404** | No task definition exists in current scope |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

