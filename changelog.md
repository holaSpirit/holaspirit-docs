API changelog
=============

[<<< Back](README.md)

## 28 September 2023

Replacement of `GET roles?view=diagram` by `GET roles-diagram`

private :

-    Old URL : GET `/api/organizations/{organization_id}/roles?view=diagram`
-    New URL : GET `/api/organizations/{organization_id}/roles-diagram`

public :

-    Old URL : GET `/api/public/organizations/{organization_slug}/roles?view=diagram`
-    New URL : GET `/api/public/organizations/{organization_slug}/roles-diagram`

After 28 September, the old URLs will return an error when using `view=diagram`, calls without this parameter are not affected and can still be used.

The new URLs don't accept any parameter, if you need to use some parameters, keep the old URL and remove the `view=diagram` part.

## 12 September 2023

Removal of some properties of the member : 

### isCore & isCoreWithoutRole
```json
{
    "circle": {
        "circle": "566ff608d796df94058b46c8",
        "circleAdmin": true,
        "isDecisionMaker": true,
        "isCore": true,
        "isCoreWithoutRole": false
    }
}
```

- The `isCore` property will be deleted, use `isDecisionMaker` instead.
- The `isCoreWithoutRole` property will be deleted, the value is always `false`.

### integrations
```json
{
    "integrations": {
        "projects": true
    }
}
```
The `integrations` property will be deleted, the info can be found in the webhooks.

## 11 September 2023

Pagination will be enabled on the routes : 

 - GET `/api/organizations/{organization_id}/circles?view=light`
 - GET `/api/organizations/{organization_id}/circles?view=tensionCount`

If you used this route with `page` or `count` parameters already, nothing will change for you.
Read more about pagination [here](https://github.com/holaSpirit/holaspirit-docs/blob/master/api.md#pager).

## 7 September 2023

The `media` object containing the avatar of the member is not available in `linked` any more.

The URL of the avatar is still available in `avatarUrl` in the `member` object.

## 6 September 2023

The rate limit for API usage is now 1000 requests every 5 minutes.

When you reach this limit, every request will have a `429 Too Many Requests` response. You will have to wait until the 5 minutes window expires.

The limit will be lowered to 500 requests every 5 minutes in the future.

[Read more](api.md#rate-limit)

## 8 August 2023

All actions and projects endpoint are deprecated soon.

You need to use the tasks endpoint instead.

They are structured in the same way, when creating a task just add `"taskType":"action"` if you to create an action, and `"taskType":"project"` for a project.

[See the api doc for a list of all endpoints.](https://app.holaspirit.com/api/doc/project)

## 2 May 2023

The deprecated URLs to download files (PDF or Spreadsheet) are not availbable any more:

| Deprecated                                                                                                  | New                                                                                                |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ~https://app.holaspirit.com/api/public/export/organizations/{organization_id}/jobs/{job_id}/download~       | https://app.holaspirit.com/api/export/organizations/{organization_id}/jobs/{job_id}/download       |
| ~https://app.holaspirit.com/api/public/pdf/organizations/{organization_id}/meetings/{meeting_id}~           | https://app.holaspirit.com/api/pdf/organizations/{organization_id}/meetings/{meeting_id}           |
| ~https://app.holaspirit.com/api/public/pdf/organizations/{organization_id}/roles~                           | https://app.holaspirit.com/api/pdf/organizations/{organization_id}/roles                           |
| ~https://app.holaspirit.com/api/public/spreadsheet/organizations/{organization_id}/templates/{template_id}~ | https://app.holaspirit.com/api/spreadsheet/organizations/{organization_id}/templates/{template_id} |

## 21 March 2023

For security reasons, it is not possible to send the access_token as a GET parameter. Send it in the headers instead.

[See example of token in the headers.](api.md#access-token-usage)

## 8 March 2023

The core member / non core member parameter in assignations to a role has been removed.

On the circle level, it is possible to choose `decisionMaker=true` (old: `coreMember`) or `decisionMaker=false` (old: `nonCoreMember`).

[See the endpoint documentation](https://app.holaspirit.com/api/doc/role#post--api-organizations-{organization_id}-circles-{circle_id}-members)

## 6 March 2023

As part of the update of our API, the `task` entity has been replaced by the `job` entity

[Check out our API documentation to view what's been updated!](download-export.md)

## 4 April 2022

### "status=notarchived" is removed in GET projects

You must replace :

`/api/organizations/5cf6888a545480100a46de00/projects?status=notarchived` 

by

`/api/organizations/5cf6888a545480100a46de00/projects?status=current` 

For the same result

## 10 January 2022

### Removal of the following endpoints:

* GET /api/organizations/{organization_id}/meetings/{meeting_id}/tensions
* POST /api/organizations/{organization_id}/meetings/{meeting_id}/tensions
* DELETE /api/organizations/{organization_id}/meetings/{meeting_id}/tensions/{tension_id}
* GET /api/organizations/{organization_id}/meetings/{meeting_id}/tensions/{tension_id}
* PATCH /api/organizations/{organization_id}/meetings/{meeting_id}/tensions/{tension_id}

You must use the endpoints without `meetings/{meeting_id}` instead.

## 30 August 2021

### Removal of deprecated attachments endpoints

* /api/organizations/{organization_id}/roles/{role_id}/attachments
* /api/organizations/{organization_id}/roles/{role_id}/attachments/{publication_id}
* /api/organizations/{organization_id}/roles/{role_id}/attachments/external

Use the endpoints in https://app.holaspirit.com/api/doc/checklist#post--api-organizations-{organization_id}-attachments instead

## 3 May 2021

### Removal of deprecated spreadsheet endpoints

* /api/public/xlsx/organizations/{organization_id}/data
* /api/public/xlsx/organizations/{organization_id}/roles
* /api/public/xlsx/organizations/{organization_id}/stats

You can download the same data using the new endpoint as explained in: [Download Export](download-export.md)

This will fix the intermittant "Gateway errors".

## 13 February 2021

### Removal of old meeting endpoints

All endpoints with URLs starting with:

* /api/organizations/{organization_id}/governances 
* /api/organizations/{organization_id}/tacticals 

are removed, you should use the ones starting with: 

* /api/organizations/{organization_id}/meetings 

### Removal of tensionType attribute in tension

`tensionType` has be removed in the input and the output of tensions.

## 5 October 2020

### Modification of webhooks format

For actions, projects, checklists & metrics:

The members are now listed inside an array, with the form:

```
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

```

## 10 September 2020

### Modification of API

Removal of the fields:

- checklist.htmlBody
- action.htmlBody
- project.htmlBody
- publication.htmlBody
- metric.htmlBody
- strategy.htmlBody
- policy.htmlBody
- tension.htmlBody
- user.htmlBiography

Use the fields:

- checklist.body
- action.body
- project.body
- publication.body
- metric.body
- strategy.body
- policy.body
- tension.body
- user.biography

instead.

## 27 July 2020

### Removal of `link` field in action, publication and strategy

Create an HTML link inside the `description` field instead

### Removal of endpoint `GET https://app.holaspirit.com/api/public/xlsx/organizations/{organization_id}/circles/{circle_id}/data`

## 16 June 2020

### Removal of all **public** endpoints for operations:

* GET /api/public/organizations/{organization_slug}/actions
* GET /api/public/organizations/{organization_slug}/actions/{action_id}
* GET /api/public/organizations/{organization_slug}/badges
* GET /api/public/organizations/{organization_slug}/badges/{badge_id}
* GET /api/public/organizations/{organization_slug}/checklists
* GET /api/public/organizations/{organization_slug}/checklists/{checklist_id}
* GET /api/public/organizations/{organization_slug}/governances
* GET /api/public/organizations/{organization_slug}/governances/{meeting_id}
* GET /api/public/organizations/{organization_slug}/metrics
* GET /api/public/organizations/{organization_slug}/metrics/{metric_id}
* GET /api/public/organizations/{organization_slug}/okrs
* GET /api/public/organizations/{organization_slug}/okrs/{okr_id}
* GET /api/public/organizations/{organization_slug}/projects
* GET /api/public/organizations/{organization_slug}/projects/{project_id}
* GET /api/public/organizations/{organization_slug}/publications
* GET /api/public/organizations/{organization_slug}/publications/{publication_id}
* GET /api/public/organizations/{organization_slug}/tacticals
* GET /api/public/organizations/{organization_slug}/tacticals/{meeting_id}
* GET /api/public/organizations/{organization_slug}/tacticals/{meeting_id}/issues
* GET /api/public/organizations/{organization_slug}/webhooks

These URLs will return a 404.

These information will only be available for the authenticated members, trough the **private** API.

(For organizations who have not changed their setting to be public, this changes nothing)

### Removal of some settings in create organization

The following settings are removed from `POST /api/organizations`

* enableEmails
* enableAnchorCircleLeadLink
* enableObjectionReason
* gogDurationDays

They are still available in `PATCH /api/organizations/{organization_id}`

## 15 June 2020

### Removal of video integrations at the organization level

Removal of the endpoints:

* GET /api/organizations/{organization_id}/integrations
* POST /api/organizations/{organization_id}/integrations
* DELETE /api/organizations/{organization_id}/integrations/{integration_id}
* POST /api/organizations/{organization_id}/governances/{meeting_id}/integrations
* POST /api/organizations/{organization_id}/tacticals/{meeting_id}/integrations

Use the `videoConfUrl` field in the meeting instead.

## 9 June 2020

### Removal of meetingType parameter in tensions

* GET /api/organizations/{organization_id}/tensions

`meetingType` parameter is removed, use `tensionType` instead.

In all the output of Tensions, `meetingType` is removed, use `tensionType` instead.

## 8 June 2020

### Removal of the "private" field in Projects

`private` is no longer a parameter in endpoints: 

* POST /api/organizations/{organization_id}/projects
* PUT /api/organizations/{organization_id}/projects/{project_id}
* PATCH /api/organizations/{organization_id}/projects/{project_id}

`private` is also removed in the output of the Project objects.

`showPrivate` is no longer a parameter in endpoint: 

* GET /api/organizations/{organization_id}/projects

## 11 May 2020

### Modification of API

Modification of the fields:

- checklist.body
- action.body
- project.body
- publication.body
- metric.body
- strategy.body
- policy.body
- tension.body
- user.biography

These field use to contain Markdown code, from now on they contain HTML code.

## 6 May 2020

### Improvements:

OKRs now have a "parent" field, this can be used to create a tree of OKRs.

## 30 April 2020

### Improvements:

The body field of objects now accepts HTML code https://www.loom.com/share/d39a9e67efee4b8fb202e43b97954ceb

## 01 April 2020

### Improvements:

"page=" & "count=" parameters are required on :

- GET /api/organizations/{organization_id}/checklists
- GET /api/organizations/{organization_id}/metrics
- GET /api/organizations/{organization_id}/governances
- GET /api/organizations/{organization_id}/tacticals
- GET /api/organizations/{organization_id}/okrs
- GET /api/organizations/{organization_id}/projects
- GET /api/organizations/{organization_id}/actions
- GET /api/organizations/{organization_id}/publications
- GET /api/organizations/{organization_id}/members
- GET /api/organizations/{organization_id}/roles
- GET /api/organizations/{organization_id}/tensions

Or you will only get the first 50 results

## 30 March 2020

### Improvements:

Allows "type=domain" to search for domains on endpoint :

- GET /api/api/organizations/{organization_id}/search 

Tensions have a new field: "tensionType"

## 28 February 2020

### Modifications of APIs:

- Remove "leadLinkMember" and "repLinkMember" attributes in the role output
- Remove "leadLinkRole" and "repLinkRole" attributes in the circle output

## 17 February 2020

### Improvements:

Tensions have a "draft" status

## 29 January 2020

### Improvements:

Add "policies" attribute on roles
