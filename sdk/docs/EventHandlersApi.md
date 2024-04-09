# lusid_workflow.EventHandlersApi

All URIs are relative to *https://www.lusid.com/workflow*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_handler**](EventHandlersApi.md#create_event_handler) | **POST** /api/eventhandlers | [EXPERIMENTAL] CreateEventHandler: Create a new Event Handler


# **create_event_handler**
> EventHandler create_event_handler(create_event_handler_request)

[EXPERIMENTAL] CreateEventHandler: Create a new Event Handler

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
    api_instance = lusid_workflow.EventHandlersApi(api_client)
    create_event_handler_request = {"id":{"scope":"A1","code":"ZZZ"},"displayName":"An example Event Handler","description":"Test","status":"Active","eventMatchingPattern":{"eventType":"PortfolioCreated","filter":"body.scope eq 'TestScope'"},"runAsUserId":{"setTo":"ExampleUserId"},"taskDefinitionId":{"scope":"A1","code":"YYY"},"taskDefinitionAsAt":"9999-12-31T23:59:59.9999999+00:00","taskActivity":{"InitialTrigger":"InitialTrigger","Type":"CreateNewTask","CorrelationIds":[],"TaskFields":{}}} # CreateEventHandlerRequest | The data to create an Event Handler

    try:
        # [EXPERIMENTAL] CreateEventHandler: Create a new Event Handler
        api_response = api_instance.create_event_handler(create_event_handler_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventHandlersApi->create_event_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_event_handler_request** | [**CreateEventHandlerRequest**](CreateEventHandlerRequest.md)| The data to create an Event Handler | 

### Return type

[**EventHandler**](EventHandler.md)

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

