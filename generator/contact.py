from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data\contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nick="", homephone="", company="",
            title="", mobilephone="", workphone="", secondaryphone="", home="",
            phone2="", work="", email="", email2="", email3="", fax="",
            mobile="", address="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
            lastname=random_string("lastname", 20), homephone=random_string("homephone",10),
            company=random_string("company", 10), title=random_string("title", 10),
            mobilephone=random_string("mobilephone", 10),
            workphone=random_string("workphone", 10), secondaryphone=random_string("secondaryphone", 10),
            home=random_string("home", 10), phone2=("phone2", 10), work=("work", 10), email=("email", 10),
            email2=("email2", 10), email3=("email3", 10), fax=("fax", 10),
            mobile=random_string("mobile", 10), address=random_string("address", 10))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))