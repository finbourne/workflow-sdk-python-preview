# CreateTaskDefinitionRequest

Contains required info to create a new Task Definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**states** | [**list[TaskStateDefinition]**](TaskStateDefinition.md) | The states this Task Definition operates over | 
**field_schema** | [**list[TaskFieldDefinition]**](TaskFieldDefinition.md) | Defines the fields associated with this Task | [optional] 
**initial_state** | [**InitialState**](InitialState.md) |  | 
**triggers** | [**list[TransitionTriggerDefinition]**](TransitionTriggerDefinition.md) | Triggers | [optional] 
**transitions** | [**list[TaskTransitionDefinition]**](TaskTransitionDefinition.md) | Transitions | [optional] 
**actions** | [**list[ActionDefinition]**](ActionDefinition.md) | Actions | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


