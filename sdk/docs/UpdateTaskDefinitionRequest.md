# UpdateTaskDefinitionRequest

Contains required info to update a Task Definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Human readable name | [optional] 
**description** | **str** | Human readable description | [optional] 
**states** | [**list[TaskStateDefinition]**](TaskStateDefinition.md) | The states this Task Definition operates over | [optional] 
**field_schema** | [**list[TaskFieldDefinition]**](TaskFieldDefinition.md) | Defines the fields associated with this Task | [optional] 
**initial_state** | [**InitialState**](InitialState.md) |  | [optional] 
**triggers** | [**list[TransitionTriggerDefinition]**](TransitionTriggerDefinition.md) | Triggers | [optional] 
**transitions** | [**list[TaskTransitionDefinition]**](TaskTransitionDefinition.md) | Transitions | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


