class elem():
    # NAME
    username = "username"
    password = "password"
    # TAG NAME
    btnLogin = "button"
    # XPATH
    menuAdmin = "//body/div[@id='app']/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]/span[1]"
    selectDropdown = "//header/div[2]/nav[1]/ul[1]/li[3]/span[1]"
    selectOrganization = "//a[contains(text(),'Locations')]"
    btnAdd = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]"

    # Search Location XPATH
    nameLoc = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]"

    # Add Location XPATH
    nameAdd = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]"
    city = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]"
    pCode = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[3]/div[1]/div[2]/input[1]"
    phone = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[5]/div[1]/div[2]/input[1]"
    address = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[7]/div[1]/div[2]/textarea[1]"
    state = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]"
    country = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]"
    fax = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[6]/div[1]/div[2]/input[1]"
    notes = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[8]/div[1]/div[2]/textarea[1]"

    # Edit Location XPATH
    nameEdit = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]"
    cityEdit = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]"
    pCodeEdit = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[3]/div[1]/div[2]/input[1]"
    phoneEdit = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[5]/div[1]/div[2]/input[1]"
    addressEdit = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[7]/div[1]/div[2]/textarea[1]"
    stateEdit = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]"
    countryEdit = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]"
    faxEdit = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[6]/div[1]/div[2]/input[1]"
    notesEdit = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[8]/div[1]/div[2]/textarea[1]"

    # Button save add location
    btnSave = "//body/div[@id = 'app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]"

    # Buttoncancel add location button
    btnCancel = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[1]"

    # ButtonSearch
    btnSearch = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/button[2]"

    # ButtonEdit
    btnEdit = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/button[2]"
    btnCancelEdit = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[1]"
    btnSaveEdit = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/button[2]"

    # Button Delete
    btnDelete = "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/button[1]"
    # confirm Delete button
    confirmDelete = "//body/div[@id='app']/div[3]/div[1]/div[1]/div[1]/div[3]/button[2]"
