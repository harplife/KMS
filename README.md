# Recipe Management System

manage recipes.

## Functions

- [x] Web Application up and running (w/ Flask)
- [] DB Handling (w/ Sqlite)
- [] Import data from csv
- [] Export data from csv
- [] Add Session Manager
- [] Login
- [] Pyinstaller

## Data Structure

Picture here

### Normal Post

- index
- content
- createdAt
- editedAt
- deletedAt
- attached
- tags (n relation with tags table)
- createdBy
- editedBy
- deletedBy

### Comment

- index
- content
- createdAt
- editedAt
- deletedAt
- attached
- targetPostIndex
- createdBy
- editedBy
- deletedBy

### User

## Notes

- Consider comment as post
- Server other than Flask seems unncessary since this would be used for just two of us.
