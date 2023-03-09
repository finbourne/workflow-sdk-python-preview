# TaskInstance

Defines an Instance of a TaskDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_definition_id** | [**TaskDefinitionId**](TaskDefinitionId.md) |  | [optional] 
**task_instance_id** | **str** | The unique id for this Task Instance | [optional] 
**correlation_id** | **str** | User-provided ID used to link entities and tasks | [optional] 
**states** | [**list[State]**](State.md) | States | [optional] 
**transitions** | [**list[Transition]**](Transition.md) | Transitions | [optional] 
**triggers** | [**list[Trigger]**](Trigger.md) | Triggers | [optional] 
**active_state** | **str** | Currently Active State | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**terminal_state** | **bool** | True if no onward transitions are possible | [optional] 
**created** | **datetime** | Creation timestamp | [optional] 
**updated** | **str** | Last Update timestamp | [optional] 
**last_transition** | **str** | Last Transition timestamp | [optional] 
**fields** | [**list[FieldInstance]**](FieldInstance.md) | Fields and their latest values - should correspond with the Task Definition field schema | [optional] 
**receivers** | **list[str]** | A list of downstream Tasks to be invoked on completion | [optional] 
**history** | [**list[HistoryEntry]**](HistoryEntry.md) | A list of timestamped messages detailing what has occurred to this Task | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


