# TaskDefinition

TaskDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**version** | [**Version**](Version.md) |  | [optional] 
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**states** | [**list[TaskStateDefinition]**](TaskStateDefinition.md) | The states this Task Definition operates over | 
**field_schema** | [**list[TaskFieldDefinition]**](TaskFieldDefinition.md) | The Fields that this Task Definition operates on | [optional] 
**initial_state** | [**InitialState**](InitialState.md) |  | 
**triggers** | [**list[TransitionTriggerDefinition]**](TransitionTriggerDefinition.md) | The Triggers for State transition | [optional] 
**actions** | [**list[ActionDefinition]**](ActionDefinition.md) | The Actions of this Task - executed after a Transition completion | [optional] 
**transitions** | [**list[TaskTransitionDefinition]**](TaskTransitionDefinition.md) | The Transitions between States | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


