# api_yamdb

### About API
YaMDb - group project on the Python course from [Yandex.Praktikum](https://praktikum.yandex.ru/)

The YaMDb project collects user reviews of works. Works are divided into categories: "Books", "Movies", "Music".The works themselves are not stored in YaMDb. You can't watch a movie or listen to music here. In each category there are works, such as books, movies or music. For example, the "Books" category may include the works "Winnie the Pooh and all-all-all" and "the Martian Chronicles", while the "Music" category may include the song "Recently" by the group "Insects" and the second Suite by Bach. A work can be assigned a genre from the preset list (for example, "fairy tale", "rock", or "art house"). Only the administrator can create new genres.

Grateful or outraged readers leave text reviews for the works and give the work a rating (rating in the range from one to ten). The average score of the product is automatically calculated from the set of ratings.

### Features
- User's registration
- Different User's permissions (admin, moderator, user)
- Token authnentication (JWT)
- Review, caregories, comments creating

### Sources
- **Auth** - authentication
- **Users** - users
- **Review** - reviews of works. The review is linked to a specific work.
- **Comments** - comments on reviews. The comment is linked to a specific review.
- **Categories** - categories (types) of works ("Movies", "Books", "Music").
- **Genres** - genres of works. A single work can be linked to several genres.
- **Titles** - works that are reviewed (a particular movie, book, or song).

### Made by
- [iljuevgrafov](https://github.com/iljuevgrafov)
- [gordeev40k](https://github.com/gordeev40k)
- [alexx](https://github.com/AlexxSandbox)
