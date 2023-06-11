# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
# имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, 
# когда пользователь будет пытаться добавить документ на несуществующую полку.
# d – delete – команда, которая спросит номер документа и удалит полностью документ из каталога и его номер из перечня полок.
#  Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. 
# Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, 
# которая уже существует.;


documents = [
        {"type": "passport", "number": "2207", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "1112", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "1566", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207', '1112','112121'],
        '2': ['1566'],
        '3': []
      }

def getNameByNumber():
  number_doc=input("Введите номер документа ")
  for doc in documents:
    if doc["number"]==number_doc:
      print(doc["name"])
      break
  print("Документа c таким номером не существует")

def getShelfByNumber():
  number_doc=input("Введите номер документа ")
  i=0
  for key in directories:
      for number in directories.get(key):
         if number == number_doc:
            print(key) 
            i+=1
  if i==0:
    print("Документа на полках c таким номером не существует")
   
def getAllDocuments():
  for doc in documents:
    print(doc["number"],doc["name"])

def deleteDocument():
  i=0
  number_doc=input("Введите номер документа для удаления ")
  for doc in documents:
    if doc["number"]==number_doc:
      del(doc["name"])
      print(f"Документ {number_doc} удален")
      i+=1
      break
  if i==0: print("Документа c таким номером не существует")

def moveDocument():
  i=0
  number_doc=input("Введите номер документа для перемещения ")
  number_shelf=''
  while number_shelf not in ('1','2','3'):
          number_shelf=input("Введите номер полки 1-3 ") 
  for key in directories:
      for number in directories.get(key):
        if number == number_doc:
            directories.get(number_shelf).append(number_doc)
            directories.get(key).remove(number_doc)
            print(f"документ {number_doc} перемещен на полку {number_shelf}") 
            i+=1
            print(directories.items())
      break
  if i==0:
    print("Документа на полках c таким номером не существует")

def addShelf():
  shelf='1'
  while shelf in (directories.keys()):
          shelf=input("Введите номер новой полки ") 
  directories[shelf]=[]
  print(directories.items())

def addNewDocument():
  type=''
  while  type not in ('passport','invoice','insurance'):
          type=input("Введите корректный тип документа 'passport' or 'invoice'or 'insurance' ")
  number=''
  while  not number.isdigit():
          number=input("Введите номер документа состоящий из цифр ")
  name=input("Введите имя ")
  shelf=''
  while shelf not in ('1','2','3'):
          shelf=input("Введите номер полки 1-3 ") 
  documents.append({type,number,name})
  directories.get(shelf).append(number)
  print(shelf,directories.get(shelf))
    
def main():
    while True:
        operation = input("Введите команду \
                          \n p - person by number document,\
                          \n s - #shelf by number document, \
                          \n l - list of documents, \
                          \n a - add new document, \
                          \n d - delete document, \
                          \n m - move document,  \
                          \n as - add self  \n")
        if operation == 'p':
            getNameByNumber()
        elif operation == 's':
            getShelfByNumber()
        elif operation == 'l':
            getAllDocuments()
        elif operation == 'a':    
            addNewDocument()
        elif operation == 'd':    
            deleteDocument()
        elif operation == 'm':    
           moveDocument()
        elif operation == 'as':    
           addShelf()
        break 

main()
