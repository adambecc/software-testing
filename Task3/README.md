# Since webdriver sessions must be separate, each of these processes will:

    -   Start and close a new WebDriver session
    -   USe unit test annotations for setup and teardown
    -   Store the created user's credentials for later use in tests

## Step 1: User Registration Script

    Open the website.
    Navigate to the "Register" page.
    Fill out and submit the form.
    Save the registered email and password in a file (user.json).

## Step 2: Implement Two Test Cases

    ### Each test case will:

        Read login credentials from user.json.
        Log in and navigate to "Digital downloads".
        Read product names from a respective data file (data1.txt or data2.txt).
        Add items to the cart.
        Proceed through checkout.
        Verify order completion.

## Step 3: WebDriver Management

    Use @classmethod annotations for setting up and tearing down WebDriver sessions.
    Each test case runs independently of the user creation step.

## Step 4: Running the Tests via Jenkins

    ### Jenkins will execute:
    
        User creation script first.
        Test 1 and Test 2 sequentially.