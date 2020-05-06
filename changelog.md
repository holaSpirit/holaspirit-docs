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

## 30 April 2020

### Improvements:

Edit "description field"
https://www.loom.com/share/d39a9e67efee4b8fb202e43b97954ceb
