# ==============================================================================
# Lesson: Encapsulation (التغليف وحماية البيانات)
# ==============================================================================
# Encapsulation = إخفاء البيانات المهمة لحمايتها من التعديل المباشر أو الخاطئ،
# والتحكم في قراءتها أو تعديلها من خلال دوال مخصصة (Getters & Setters).

# ----------------------------------------------------------
# 1. مثال درجات الطلاب (Student Grades)
# ----------------------------------------------------------

class Student:
    def __init__(self, name, student_id, grade):
        self.name = name             # Public Attribute
        self._id = student_id        # Protected Attribute
        self.__grade = grade         # Private Attribute (مخفي ومحمي برمز __)

    # دالة قراءة الدرجة بأمان (Getter Method)
    def get_grade(self):
        return self.__grade

    # دالة تعديل الدرجة مع التحقق من صحتها (Setter Method)
    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
            print(f"Grade updated successfully to {new_grade}")
        else:
            print("Error: Grade must be between 0 and 100!")


# --- التجربة والاستدعاء ---
print("--- 1. اختبار حماية درجات الطلاب ---")
s1 = Student("Ali", 1001, 90)

print("Name:", s1.name)
print("Grade using Getter:", s1.get_grade())

s1.set_grade(95)         # تعديل صحيح
s1.set_grade(150)        # تعديل خاطئ يتم رفضه

# محاولة التعديل المباشر (لن تؤثر على المتغير الأصلي)
s1.__grade = 10
print("Grade after direct edit attempt:", s1.get_grade())


# ----------------------------------------------------------
# 2. مثال التحكم في صوت التلفزيون (Smart TV Volume)
# ----------------------------------------------------------

class SmartTV:
    def __init__(self, brand):
        self.brand = brand
        self.__volume = 10     # مستوى الصوت مخفي

    def get_volume(self):
        return self.__volume

    def volume_up(self):
        if self.__volume < 100:
            self.__volume += 1
            print(f"Volume: {self.__volume}")
        else:
            print("Maximum volume reached!")

    def volume_down(self):
        if self.__volume > 0:
            self.__volume -= 1
            print(f"Volume: {self.__volume}")
        else:
            print("Volume is muted!")


print("\n--- 2. اختبار التحكم في صوت التلفزيون ---")
tv = SmartTV("Samsung")
print("TV Brand:", tv.brand)
print("Current Volume:", tv.get_volume())

tv.volume_up()
tv.volume_up()
tv.volume_down()