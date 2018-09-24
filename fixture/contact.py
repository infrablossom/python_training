from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    # def fill_fields(self, contact):
        # wd.find_element_by_name("selected[]")

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        wd.find_element_by_xpath(".//*[@id='logo']").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("title", contact.title)
        self.change_field_value("phone2", contact.phone2)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_first_contact()
        # open modif form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modif
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//a[contains(text(),'Last name')]")) > 0):
            wd.find_element_by_xpath("//div[@id='nav']/ul/li/a").click()

    def count_contacts(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_xpath(".//*[@id='maintable']/tbody/tr[2]/td[8]/a/img"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            contacts = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                # text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                contacts.append(Contact(firstname=cells[1].text, lastname=cells[2].text, id=id))
            return contacts

    def open_new_address_form(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def input_list(self, contact):
        wd = self.app.wd
        self.open_new_address_form()
        self.fill_contact_form(contact)
        self.contact_submit()
        self.return_to_home_page()

    def contact_submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='content']/form/input[21]").click()





