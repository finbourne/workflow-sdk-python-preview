# RunWorkerActionResponse

Defines a read-only Run Worker Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type name for this Action | [optional] 
**worker_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**worker_as_at** | **datetime** | Worker AsAt | [optional] 
**worker_parameters** | [**dict[str, FieldMapping]**](FieldMapping.md) | Parameters for this Worker | [optional] 
**worker_status_triggers** | [**WorkerStatusTriggers**](WorkerStatusTriggers.md) |  | [optional] 
**child_task_configurations** | [**list[ResultantChildTaskConfiguration]**](ResultantChildTaskConfiguration.md) | Tasks can be generated from run worker results; this is the configuration | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


