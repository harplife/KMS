# Recipe Management System

manage recipes.

## Functions

- [x] Web Application up and running (w/ Flask)
- [] DB Handling (w/ Sqlite)
  - [x] db connect
  - [x] dummy data initialization
  - [x] dummy data query
  - [] real data
  - [] insert API
  - [] edit API
  - [] delete API
- [] Import data from csv
- [] Export data from csv
- [] Add Session Manager
- [] Login
- [] Take picture with webcam
- [] Take picture with phone
- [] Screen capture recipe page (w/ Selenium)
- [] Pyinstaller

## Project Structure

![project_structure](/rms_structure.png)

## Components of Recipe

- Food Name
- Source (Book/Page/Site)
- Chef (Author/Cook/Brand)
- Prep Time
- Cooking Time
- Servings
- Ingredients
- Directions
- After Review ("tried it")
- Screenshot
- Food Image
- Comment
- Frying?
- Oven?
- Special Equipment

## Components of Ingredient

- Measurements
- Type (Veges/Fruits/Sauce)
- Reference Recipe
- Market Price?
- Frozen available?

## Components of Review

- Which Food?
- When?
- How was it?
- Would you do it again?
- Did you change anyting from the recipe?
- Would you eat it every week?
- Would you recommend it to a friend?
- Difficulty Score out of 5?
- Taste Score out of 5?
- Any mistakes?
- Future note?
- How much did it cost overall?
- Made with leftover ingredients?
- Are there leftover ingredients?
- How long did it take?

## Data Structure

### Normal Recipe Post

- index
- prep time
- cooking time
- servings
- ingredients (relation)
- directions
- reviews (relation)
- food image
- comments (relation)
- equipment (pan, oven, juicer)
- special euqipment (waffle maker)
- createdAt
- editedAt
- delYN
- deletedAt
- attached
- tags (relation)
- createdBy
- editedBy
- deletedBy

### Comment

- index
- content
- createdAt
- editedAt
- delYN
- deletedAt
- attached
- targetPostIndex
- createdBy
- editedBy
- deletedBy

### Review

- index
- targetPostIndex
- cookedAt
- tasteScore
- difficultyScore
- content
- createdAt
- editedAt
- delYN
- deletedAt
- attached
- createdBy
- editedBy
- deletedBy

### User Profile

- index
- name
- createdAt
- editedAt
- delYN
- deletedAt
- createdBy
- editedBy
- deletedBy
- userAbout
- userPhoto

## Notes

- Consider comment as post
- Server other than Flask seems unncessary since this would be used for just two of us.

## References

- Sqlite DB operatoins [link](https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/)
