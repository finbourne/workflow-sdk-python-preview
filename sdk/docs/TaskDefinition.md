# TaskDefinition

TaskDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_definition_id** | [**TaskDefinitionId**](TaskDefinitionId.md) |  | [optional] 
**display_name** | **str** | Human readable name | [optional] 
**description** | **str** | Human readable description | [optional] 
**states** | [**list[State]**](State.md) | The states this Task Definition operates over | [optional] 
**fields_schema** | [**list[FieldSchema]**](FieldSchema.md) | The Fields that this Task Definition operates on | [optional] 
**initial_state** | [**InitialState**](InitialState.md) |  | [optional] 
**triggers** | [**list[Trigger]**](Trigger.md) | The Triggers for State transition | [optional] 
**outputs** | [**list[Output]**](Output.md) | The Outputs of this Task | [optional] 
**transitions** | [**list[Transition]**](Transition.md) | The Transitions between States | [optional] 
**instances** | **list[str]** | Each Definition will have a number of instances associated with it | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


