# TriggerSchema

Triggers can operate in response to different stimuli

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of Trigger: Manual, Timeout or WebHook | [optional] 
**time_in_state** | **int** | The amount of time to wait in seconds (Timeout only) | [optional] 
**response_codes** | **dict(str, list[int])** | Defines a set of HTTP response codes that correspond to an outcome. eg: &#39;OK &#x3D;&gt;  [&#39;200&#39;, &#39;204&#39;] (WebHook only) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


