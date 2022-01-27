class Dog :
  def __init__(self, name, breed, color,gender,age, height, weight):
    self.name = name
    self.breed = breed
    self.color = color
    self.gender = gender
    self.age = age
    self.height = height
    self.weight = weight
  
  def growth(self):
    self.name = self.name
    self.breed = 'พันธุ์'+self.breed
    self.color = 'สี'+self.color
    self.gender = self.gender
    self.age = self.age
    self.height = self.height*1.1
    self.weight = self.weight*1.1 

class Owner :
  def __init__(self, name, gender, ege, phone, address):
    self.name = name
    self.gender = gender
    self.ege = ege
    self.phone = phone
    self.address = address
  
  def register(self):
    self.name = 'ชื่อเจ้าของ'+self.name
    self.gender = 'เพศ'+self.gender
    self.ege = 'อายุ'+self.ege
    self.phone = 'เบอร์โทร'+self.phone
    self.address = 'ที่อยู่'+self.address

owner_A = Owner(' เมย์ ', ' หญิง' , ' 16 ปี ', '0812345678' , '101/53 kmitl bkk' )
owner_A.register()
dog_A = Dog('มูมู่', 'โกเด้น', 'ทอง', 'เพศผู้', 2 , 20, 10)
dog_A.growth()

print( owner_A.name, owner_A.gender, owner_A.ege , owner_A.phone , owner_A.address )
print('เจ้าของน้อง🐶',dog_A.name)   
print('breed =', dog_A.breed)
print('gender =', dog_A.gender) 
print('age =', dog_A.age , 'ขวบ')
print('color =', dog_A.color)
print('height =', dog_A.height)
print('weight =', dog_A.weight)


