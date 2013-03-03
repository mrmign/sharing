from storm.locals import *

class Person(object):
	__storm_table__ = "person"
	id = Int(primary=True)
	name = Unicode()

class Company(object):
    __storm_table__ = "company"
    id = Int(primary=True)
    name = Unicode()
 #    try :
 #    	import Employee,Accountant,CompanyAccountant
 #    except:
 #    	pass
	# employees = ReferenceSet(Company.id, Employee.company_id)

	# accountants = ReferenceSet(Company.id,CompanyAccountant.company_id,\
 #    							CompanyAccountant.accountant_id,Accountant.id)
	
    def __init__(self, name):
       	self.name = name
class Employee(Person):
     __storm_table__ = "employee"
     company_id = Int()
     company = Reference(company_id, Company.id)

     def __init__(self, name):
         self.name = name

class Accountant(Person):
    __storm_table__ = "accountant"
    def __init__(self, name):
        self.name = name

class CompanyAccountant(object):
    __storm_table__ = "company_accountant"
    __storm_primary__ = "company_id", "accountant_id"
    company_id = Int()
    accountant_id = Int()

Company.employees = ReferenceSet(Company.id, Employee.company_id)

Company.accountants = ReferenceSet(Company.id,CompanyAccountant.company_id,\
    							CompanyAccountant.accountant_id,Accountant.id)

debug = False
if debug:
	database = create_database("mysql://root:root@localhost:3306/test")
else:
	database = create_database("mysql://root:root@localhost:3306/storm")
store = Store(database)

# store.execute("CREATE TABLE person (id int auto_increment PRIMARY KEY, name varchar(20))")
# store.execute("CREATE TABLE company (id INTEGER auto_increment PRIMARY KEY, name VARCHAR(20))", noresult=True)
# store.execute("CREATE TABLE employee (id INTEGER auto_increment PRIMARY KEY, name VARCHAR(20), company_id INTEGER)",noresult=True)

store.execute("CREATE TABLE accountant "
               "(id INTEGER auto_increment PRIMARY KEY, name VARCHAR(20))", noresult=True)


store.execute("CREATE TABLE company_accountant "
               "(company_id INTEGER, accountant_id INTEGER,"
               " PRIMARY KEY (company_id, accountant_id))", noresult=True)

# joe = Person()
# joe.name = u"Arming"
# print "%r, %r" %(joe.id, joe.name

# ming = Person()
# ming.name = u"Yonuhg Alo"
# print "%r, %r" %(ming.id, ming.name)
# m = store.add(ming)

# store.commit()
# store.flush()
# print (Store.of(joe) is store)
# print (Store.of(Person()) is None)

# person = store.find(Person, Person.name==u"Joe Johns").one()
# print "%r, %r" %(person.id, person.name)

# print store.get(Person, 1).name

# print m.id, m.name

# circus = Company(u"Circus Inc.")
# ben = store.add(Employee(u"Ben Bill"))
# ben.company = circus
# print "%r, %r" % (ben.company_id, ben.company.name)
# store.flush()
# print "%r, %r" % (ben.company_id, ben.company.name)
# store.add(Company(u"SweetInc."))
# store.flush()
# ben = store.find(Employee, Employee.company_id==1).one()
# ben.company_id = 2
# store.add(ben)
# store.commit()