# CreateTaskDefinitionRequest

Contains required info to create a new Task Definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**display_name** | **str** | Human readable name | [optional] 
**description** | **str** | Human readable description | [optional] 
**fields** | [**list[FieldSchema]**](FieldSchema.md) | Defines the fields associated with this Task | [optional] 
**states** | [**list[State]**](State.md) | The states this Task Definition operates over | [optional] 
**transitions** | [**list[Transition]**](Transition.md) | Transitions | [optional] 
**triggers** | [**list[Trigger]**](Trigger.md) | Triggers | [optional] 
**initial_state** | [**InitialState**](InitialState.md) |  | [optional] 
**outputs** | [**list[Output]**](Output.md) | The Outputs of this Task | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


