BEGIN;
--
-- Create model Author
--
CREATE TABLE "main_author" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"first_name" varchar(30) NOT NULL,
"last_name" varchar(50) NOT NULL);
--
-- Create model Book
--
CREATE TABLE "main_book" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
"title" varchar(50) NOT NULL,
"author_id" bigint NOT NULL REFERENCES "main_author" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Publisher
--
CREATE TABLE "main_publisher" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL);
CREATE TABLE "main_publisher_authors" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "publisher_id" bigint NOT NULL REFERENCES "main_publisher" ("id") DEFERRABLE INITIALLY DEFERRED, "author_id" bigint NOT NULL REFERENCES "main_author" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "main_publisher_books" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "publisher_id" bigint NOT NULL REFERENCES "main_publisher" ("id") DEFERRABLE INITIALLY DEFERRED, "book_id" bigint NOT NULL REFERENCES "main_book" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "main_book_author_id_1299d038" ON "main_book" ("author_id");
CREATE UNIQUE INDEX "main_publisher_authors_publisher_id_author_id_9509ed35_uniq" ON "main_publisher_authors" ("publisher_id", "author_id");
CREATE INDEX "main_publisher_authors_publisher_id_ef08ed93" ON "main_publisher_authors" ("publisher_id");
CREATE INDEX "main_publisher_authors_author_id_4d4f1ee7" ON "main_publisher_authors" ("author_id");
CREATE UNIQUE INDEX "main_publisher_books_publisher_id_book_id_21273ba7_uniq" ON "main_publisher_books" ("publisher_id", "book_id");
CREATE INDEX "main_publisher_books_publisher_id_b739a9fe" ON "main_publisher_books" ("publisher_id");
CREATE INDEX "main_publisher_books_book_id_f352e88f" ON "main_publisher_books" ("book_id");
COMMIT;
