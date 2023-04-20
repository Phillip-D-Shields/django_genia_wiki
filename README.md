# Django Genia Wiki

## Genia Playbook

### Install

- Run `docker compose up` from the root to start the server

  > Note: A postgresql db container will be created and started automatically, once this container is ready to accept connections, the django server will start. This can take a few seconds.

- Once everything is connected and operating, run the command `python manage.py rebuild_index` to create the search index.

  > Note: This command will take a few seconds to complete. And you must confirm the rebuild.

#### Playbook UI

- Once both containers are running navigate to [localhost:8000/wiki](http://localhost:8000/wiki) to view the wiki landing page.

  ![wiki landing page](/media/images/playbook-ui.png)

- The navbar has four links:

1. `Genia Playbook` displays all products.
2. `Architectural` displays all architectural products.
3. `Componentry` displays all componentry products.
4. `Outdoors` displays all outdoor products.

- The search bar can be used to search for products by name and keywords. The search index can easily be modified and updated using the haystack library.

#### Admin UI

- Navigate to [localhost:8000/admin](http://localhost:8000/admin) to view the admin page.

- A default superuser is already created with the following credentials:

  > username: admin

  > password: adminpassword

![admin landing page](/media/images/admin-login.png)

- From the superuser page all groups, users, tags, products, and product categories can be created, updated, and deleted.

---

#### Create customer service group and user

##### Create customer service group

- Navigate to Groups and click `+ Add`
- Add the name `Customer Service` to the Name field
- Since customer service will only need to create and update products select the following options in the Permissions box:
  - `Can change category`
  - `Can view category`
  - `Can add product`
  - `Can change product`
  - `Can view product`
  - other permissions are omited to prevent accidental actions, only the tech team will have access to all permissions
  - Once the permissions are selected and highlighted click on the right arrow to move them to the Chosen Permissions box

![customer service group permissions](/media/images/group-permissions.png)

- Click `Save` to save the customer service group

##### Create customer service user

- Navigate to Users and click `+ Add`
- Add the username `arthur` to the Username field
- Add the password `arthurpassword` to the Password and Password Confirmation field

![customer service user](/media/images/add-user.png)

- Click `Save` to save the user
- The following screen will allow us to customise the user and add them to the customer service group
- Under the permissions header check the box for `staff status`, this will allow the user to login to the admin dashboard
- Highlight and shift the `Customer Service` group to the Chosen groups box
- Since the `Customer Service` group already has the correct permissions, we dont need to set any other permissions for the user

![customer service user permissions](/media/images/user-permissions.png)

- click `Save` to save the user
- logout and then log back in with the new user credentials

![customer service login](/media/images/user-login.png)

- the new user will only have access to the specific items and permissions we established earlier

![customer service dashboard](/media/images/user-dashboard.png)

- add a new product or update an existing product with a photo to test the workflow, then go check it out on the Playbook UI

---

### Known bugs and issues

- the `view site` link in the admin dashboard needs to be configured correctly.
- maybe the `~admin` should be changed to `~/wiki/admin`
- more to come, i am sure
