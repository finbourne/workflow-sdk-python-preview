# CreateChildTaskConfiguration

Create Child Task Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_definition_id** | [**ResourceId**](ResourceId.md) |  | 
**task_definition_as_at** | **datetime** | TaskDefinition AsAt timestamp | [optional] 
**initial_trigger** | **str** | The Initial Trigger for automatic start | [optional] 
**child_task_fields** | [**dict[str, FieldMapping]**](FieldMapping.md) | Field Mappings | [optional] 
**map_stacking_key_from** | **str** | If present, the value of this field on the parent task will be the Stacking Key on any created child tasks | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


