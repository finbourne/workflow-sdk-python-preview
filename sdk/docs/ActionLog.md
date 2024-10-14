# ActionLog

An Action Log contains the processing history of an Action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the Action | 
**origin** | [**ActionLogOrigin**](ActionLogOrigin.md) |  | 
**action_type** | **str** | The type of the Action | 
**run_as_user_id** | **str** | The ID of the user that the Action was performed by.  If not specified, the actions were performed by the \&quot;current user\&quot;. | [optional] 
**logged_items** | [**list[ActionLogItem]**](ActionLogItem.md) | The logged items for this Action | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


