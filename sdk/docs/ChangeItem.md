# ChangeItem

Defines a change that occured to a Task

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_modified** | **datetime** | The AsAt time of the change | 
**user_id_modified** | **str** | The User ID that performed the change | 
**request_id_modified** | **str** | The Request ID of the request that caused the change | 
**as_at_version_number** | **int** | The AsAt Version number | 
**action** | **str** | The Action that resulted in the change | 
**attribute_name** | **str** | The name of the attribute that has been change | 
**previous_value** | **object** | The value of the attribute prior to the change | [optional] 
**new_value** | **object** | The value of the attribute following the change | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


