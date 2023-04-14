# lusid_workflow.TaskDefinitionsApi

All URIs are relative to *https://www.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_definition**](TaskDefinitionsApi.md#create_task_definition) | **POST** /api/taskdefinitions | [EXPERIMENTAL] CreateTaskDefinition: Create a new Task Definition.
[**delete_task_definition**](TaskDefinitionsApi.md#delete_task_definition) | **DELETE** /api/taskdefinitions/{scope}/{code} | [EXPERIMENTAL] DeleteTaskDefinition: Delete a Task Definition.
[**get_task_definition**](TaskDefinitionsApi.md#get_task_definition) | **GET** /api/taskdefinitions/{scope}/{code} | [EXPERIMENTAL] GetTaskDefinition: Get a Task Definition.
[**list_task_definitions**](TaskDefinitionsApi.md#list_task_definitions) | **GET** /api/taskdefinitions/{scope} | [EXPERIMENTAL] ListTaskDefinitions: List Task Definitions
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
    create_task_definition_request = {"id":{"scope":"A1","code":"ZZZ"},"displayName":"An example TaskDefinition","description":"Test","states":[{"name":"Submitted"},{"name":"InProgress"},{"name":"SendingSurvey"},{"name":"Done"},{"name":"SurveyNotSent"},{"name":"NotDone"}],"fieldSchema":[{"name":"clientId","type":"String"},{"name":"assignee","type":"String"},{"name":"resolutionDetail","type":"String"}],"initialState":{"name":"Submitted","requiredFields":["clientId"]},"triggers":[{"name":"start","trigger":{"type":"External"}},{"name":"cancel","trigger":{"type":"External"}},{"name":"resolve","trigger":{"type":"External"}},{"name":"timeout","trigger":{"type":"External"}},{"name":"success","trigger":{"type":"External"}},{"name":"failure","trigger":{"type":"External"}}],"transitions":[{"fromState":"Submitted","toState":"InProgress","trigger":"start","guard":"fields.assignee exists AND fields.assignee NOT eq ''"},{"fromState":"InProgress","toState":"SendingSurvey","trigger":"resolve","guard":"fields.resolutionDetail exists AND fields.resolutionDetail NOT eq ''"},{"fromState":"SendingSurvey","toState":"Done","trigger":"success"},{"fromState":"SendingSurvey","toState":"SurveyNotSent","trigger":"failure"},{"fromState":"SendingSurvey","toState":"NotDone","trigger":"timeout"},{"fromState":"InProgress","toState":"NotDone","trigger":"cancel","guard":"fields.cancellationDetail exists AND fields.cancellationDetail NOT eq ''"}]} # CreateTaskDefinitionRequest | The data to create a Task Definition

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
**201** | Created |  -  |
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

# **list_task_definitions**
> ResourceListOfTaskDefinition list_task_definitions(scope)

[EXPERIMENTAL] ListTaskDefinitions: List Task Definitions

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
    scope = 'default' # str |  (default to 'default')

    try:
        # [EXPERIMENTAL] ListTaskDefinitions: List Task Definitions
        api_response = api_instance.list_task_definitions(scope)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskDefinitionsApi->list_task_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | [default to &#39;default&#39;]

### Return type

[**ResourceListOfTaskDefinition**](ResourceListOfTaskDefinition.md)

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
**404** | No Task Definitions found in the requested scope |  -  |
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
update_task_definition_request = {"displayName":"bar","description":"foo","fieldSchema":[{"name":"foo","type":"Boolean"}]} # UpdateTaskDefinitionRequest | The data to update a Task Definition

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

