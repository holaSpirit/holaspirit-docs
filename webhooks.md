Outgoing Webhooks
=================

[<<< Back](README.md)

[See general info about the webhooks](https://help.holaspirit.com/articles/3725006-outgoing-webhooks)

### Standard exchange

A POST call will be done after each events.

Data are encode in JSON, with this structures:

Task (create/update/delete):
```
{
  "object": "task",
  "activity": "create | update | delete",
  "id": "5f7139d99b62fd692133406f",
  "text": "description of the event",
  "title": "title field of the task",
  "body": "description field of the task",
  "status": "current | waiting | future | done",
  "url": "Link to the task",
  "context": {
    "funnels": [
      {
        "circle": "name of the circle",
        "members": [
          {
            "id": "5f7139d99b62fd692133406f",
            "member": "John Doe"
          },
          {
            "id": "5f7139d99b62fd6921334070",
            "member": "Jane Doe"
          }
        ],
        "isSync": "yes"
      }
    ]
  },
  // deprecated
  "circle": "id of the circle",
  "members": [
    {
      "id": "5f7139d99b62fd692133406f",
      "member": "John Doe",
      "action": "assign"
    },
    {
      "id": "5f7139d99b62fd6921334070",
      "member": "Jane Doe",
      "action": "assign"
    }
  ],
  "role": "Name of the role"
}
```
OKR (create/update/delete) :
```
{
'object' : 'objective',
'activity' : 'create | update | delete',
'id': '5f7139d99b62fd692133406f',
'text' : 'description of the event',
'title' : 'title field of the OKR',
'body' : 'description field of the OKR',
'circle' : 'id of the circle',
 'members': [
        {
            "id": "5f7139d99b62fd692133406f",
            "member": "John Doe",
            "action": "assign"
        },
        {
            "id": "5f7139d99b62fd6921334070",
            "member": "Jane Doe",
            "action": "assign"
        }
    ]
'role' : 'Name of the role',
'status' : 'current' or 'done',
'url' : 'Link to the OKR'
}
```
Checklist (creation/update) :
```
{
'object' : 'checklist',
'id': '5f7139d99b62fd692133406f',
'text' : 'description of the event',
'title' : 'title field of the checklist',
'body' : 'description field of the checklist',
'circle' : 'id of the circle',
'members': [
        {
            "id": "5f7139d99b62fd692133406f",
            "member": "John Doe",
            "action": "assign"
        }
    ]
'role' : 'Name of the role',
'recurrence' : 'daily ... yearly',
'last_checked' : 'last time the checklist was checked during a tactical meeting'
}
```
Metric (creation/update) :
```
{
'object' : 'metric',
'id': '5f7139d99b62fd692133406f',
'text' : 'description of the event',
'title' : 'title field of the metric',
'body' : 'description field of the metric',
'circle' : 'id of the circle',
'members': [
        {
            "id": "5f7139d99b62fd692133406f",
            "member": "John Doe",
            "action": "assign"
        }
    ]
'role' : 'Name of the role',
'recurrence' : 'daily ... yearly',
'last_checked' : 'last time the metric was checked during a tactical meeting'
}
```
Publication (creation/update) :
```
{
'object' : 'publication',
'id': '5f7139d99b62fd692133406f',
'text' : 'description of the event',
'title' : 'title field of the publication',
'body' : 'description field of the publication',
'circle' : 'id of the circle',
'member' : 'Name of assigned member',
'role' : 'Name of the role'
}
```
Policy (creation/update/deletion) :
```
{
'object' : 'policy',
'id': '5f7139d99b62fd692133406f',
'text' : 'description of the event',
'circle' : 'id of the circle',
'url' : 'Link to the policy in Holaspirit'
}
```
Role/Circle (creation/update/deletion) :
```
{
'object' : 'role',
'id': '5f7139d99b62fd692133406f',
'text' : 'description of the event',
'purpose' : 'purpose',
'circle' : 'id of the circle',
'url' : 'Link to the role/circle in Holaspirit',
* 'domains' : 'Domains, split by a carriage return',
* 'accountabilities' : 'Accountabilities, split by a carriage return'
}
```
* This fields aren't fill if they are empty
Election
```
{
'object' : 'corerole',
'text' : 'quickly description of the event',
'circle' : 'name of the circle',
'circle_id' : 'id of the circle',
'role' : 'name of the role',
'role_id' : 'id of the role',
'member' : 'name of the member',
'member_id' : 'id of the member',
'until' : 'end date (format: YYYY-MM-DD)',
'election' : 'complete description of the event',
'url' : 'Link to the role in Holaspirit'
}
```
Assignation
```
{
'object' : 'assignation',
'text' : 'quickly description of the event',
'circle' : 'name of the circle',
'circle_id' : 'id of the circle',
'role' : 'name of the role',
'role_id' : 'id of the role',
'member' : 'name of the member',
'member_id' : 'id of the member',
'focus' : 'focus',
'assignation' : 'complete description of the event',
'url' : 'Link to the role in Holaspirit'
}
```
Unassignation
```
{
'object' : 'unassignation',
'text' : 'quick description of the event',
'circle' : 'name of the circle',
'circle_id' : 'id of the circle',
'role' : 'name of the role',
'role_id' : 'id of the role',
'member' : 'name of the member',
'member_id' : 'id of the member',
'assignation' : 'complete description of the event',
'url' : 'Link to the role in Holaspirit'
}
```
