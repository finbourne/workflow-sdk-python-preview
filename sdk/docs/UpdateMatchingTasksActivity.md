# UpdateMatchingTasksActivity

Update all matching tasks based on filter matches

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of task activity | 
**filter** | **str** | The filter that matches on existing tasks | [optional] 
**trigger** | **str** | Trigger to supply to all tasks that have been matched | 
**correlation_ids** | [**list[EventHandlerMapping]**](EventHandlerMapping.md) | The event to correlation ID mappings | [optional] 
**task_fields** | [**dict[str, FieldMapping]**](FieldMapping.md) | The event to task field mappings | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


