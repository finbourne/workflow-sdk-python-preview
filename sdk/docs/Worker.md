# Worker

Information about the Worker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**display_name** | **str** | Human readable name | 
**description** | **str** | Human readable description | [optional] 
**worker_configuration** | **object** | Information about how the worker should be executed | 
**version** | [**VersionInfo**](VersionInfo.md) |  | [optional] 
**parameters** | [**list[Parameter]**](Parameter.md) | The Parameters this Worker accepts or requires. | [optional] 
**result_fields** | [**list[ResultField]**](ResultField.md) | The Fields that the Worker results will come back with. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


