# EventHandler

Information about an Event Handler

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**version** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**status** | **str** | The current status of the event handler | 
**event_matching_pattern** | [**EventMatchingPattern**](EventMatchingPattern.md) |  | 
**run_as_user_id** | [**EventHandlerMapping**](EventHandlerMapping.md) |  | 
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**task_definition_as_at** | **datetime** | AsAt of the required task definition | [optional] 
**task_activity** | [**TaskActivityResponse**](TaskActivityResponse.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


