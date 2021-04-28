# djangoMarket

Pip install the following to run locally
django==2.2
bcrypt


## Pages/routes needed:
Log in page = index.html
Sign up page
All items
items by category
Users
Add item
edit item
delete item
Users Items
edit user
logout

Possibly have route to sort items bu category only...so you only see the category that you chose


Have some static images for either items (like a general image for all items in a certain category) or just the main pages
general profile image that is set for all users


        <h3>Select a category to see items for sale</h3>
        <form action='/' method='post'>
            <label for='category'>Category</label>
            <select id='category' name='category'>
                {% for type in category %}
                <option value='{{type}}'>{{type}}</option>
                {% endfor %}
            </select>
        </form>