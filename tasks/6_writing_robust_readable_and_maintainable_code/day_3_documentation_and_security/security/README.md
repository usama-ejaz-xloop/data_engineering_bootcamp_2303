# Security tasks

To show you the impact of security vulnerabilities, we have prepared three vulnerable applications for you.

The task for you would be to hack them.

All tasks can be solved without looking at the code.

If you hack the application successfully, you will obtain a flag - a short string in the form of FLAG{...} that proves that you solved the task successfully.

## Hackme 1

Browse to:

`tasks/6_writing_robust_readable_and_maintainable_code/
day_3_documentation_and_security/security/hackme1`

Start the hackme with:

`docker-compose up`

When filtering, the application builds the query in the following way:

`f"SELECT content FROM todo WHERE content LIKE '%{containing_string}%'"`

The flag is in the database in the secret column of the secrets table - but how can you solve the task if you don’t know that?


<details><summary>Hint 1</summary>

	`The vulnerability is called SQL Injection.`

</details>

<details><summary>Hint 2</summary>

	`You may make SQL ignore the rest of the query via a comment, [space]--[space].`

</details>

<details><summary>Hint 3</summary>

	`You may extract data from a different table using UNION clause.`

</details>


## Hackme 2

Browse to:

`tasks/6_writing_robust_readable_and_maintainable_code/
day_3_documentation_and_security/security/hackme2`

Start the hackme with:

`docker-compose up`

There are two flags in this task. It is sufficient to find one.


<details><summary>Hint 1</summary>

	`The vulnerability is called security misconfiguration.`

</details>

<details><summary>Hint 2</summary>

	`Try to cause an error in the application.`

</details>


## Hackme 3

This is an additional task: let us assume you want the capability to download URLs (e.g. to display a thumbnail for a link) but you want to disallow scanning internal network. How can you do that?






