API changelog
=============

[<<< Back](README.md)

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
