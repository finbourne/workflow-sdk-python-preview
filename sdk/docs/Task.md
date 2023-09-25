# Task

Defines a Task created based on a Task Definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id for this Task | 
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**task_definition_version** | [**TaskDefinitionVersion**](TaskDefinitionVersion.md) |  | 
**state** | **str** | Current State | 
**ultimate_parent_task** | [**TaskSummary**](TaskSummary.md) |  | 
**parent_task** | [**TaskSummary**](TaskSummary.md) |  | [optional] 
**child_tasks** | [**list[TaskSummary]**](TaskSummary.md) | This Task&#39;s child tasks | [optional] 
**correlation_ids** | **list[str]** | User-provided ID used to link entities and tasks | [optional] 
**version** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**terminal_state** | **bool** | True if no onward transitions are possible | 
**as_at_last_transition** | **datetime** | Last Transition timestamp | [optional] 
**fields** | [**list[TaskInstanceField]**](TaskInstanceField.md) | Fields and their latest values - should correspond with the Task Definition field schema | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


