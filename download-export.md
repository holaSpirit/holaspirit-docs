Download export
===============

[<<< Back](README.md)

The exports are build asynchronously (in order to avoid timeouts, even with large organizations)

You need to be [authenticated](api.md) to download exports.

### Step 1

Call:

```
POST https://app.holaspirit.com/api/async/organizations/{organization_id}/spreadsheet
```

With parameter `tabs=` indicating what will be exported, it's possible to export many tabs in a spreadsheet. The complete list of possible tabs is listed in [the documentation](https://app.holaspirit.com/api/doc/async#post--api-async-organizations-{organization_id}-spreadsheet)

For example: 

* If you want to export the list of roles in the organization, use: `tabs=role`.
* If you want to export the structure of your organization, use: `tabs=member,assignation,role`.

The response of the request will be of the form:

```json
{
    "data": {
        "id": "5f17dd3c956935687627b656",
        "status": "current",
        "taskType": "export_spreadsheet",        
        [...]
    }
}
```
(write down the `id`, you will need it in the next Steps)

### Step 2

Now you need to wait for the task to finish.

Depending on the size of you organization, the export might take from a few seconds to a few minutes.

You need to check the status with: (check only the task with the `id` you created in Step 1)

```
GET https://app.holaspirit.com/api/organizations/{organization_id}/tasks/{task_id}
```
([See documentation](http://localhost:8080/api/doc/organization#get--api-organizations-{organization_id}-tasks-{task_id}))

When the status is `done` you can go to the next step. If the status is still `current`, wait a little and try again.

The task is available for 1 week, after that it is deleted.

### Step 3

Using the task id from Steps 1 & 2, you can now download the file by calling:

```
GET https://app.holaspirit.com/api/public/export/organizations/{organization_id}/tasks/{task_id}/download
```

And you are done!
