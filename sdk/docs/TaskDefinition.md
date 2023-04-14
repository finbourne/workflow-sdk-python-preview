# TaskDefinition

TaskDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**display_name** | **str** | Human readable name | [optional] 
**description** | **str** | Human readable description | [optional] 
**states** | [**list[TaskStateDefinition]**](TaskStateDefinition.md) | The states this Task Definition operates over | [optional] 
**field_schema** | [**list[TaskFieldDefinition]**](TaskFieldDefinition.md) | The Fields that this Task Definition operates on | [optional] 
**initial_state** | [**InitialState**](InitialState.md) |  | [optional] 
**triggers** | [**list[TransitionTriggerDefinition]**](TransitionTriggerDefinition.md) | The Triggers for State transition | [optional] 
**transitions** | [**list[TaskTransitionDefinition]**](TaskTransitionDefinition.md) | The Transitions between States | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


