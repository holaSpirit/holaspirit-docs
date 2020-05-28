API changelog
=============

[<<< Back](README.md)

## Date TBD

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
