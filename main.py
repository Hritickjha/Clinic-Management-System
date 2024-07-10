class Patient:
    def __init__(self, name, age, gender, contact):
        self.name = name 
        self.age = age
        self.gender = gender
        self.contact = contact
        self.appointments = []
        
    def add_appointment(self, doctor_name, appointment_date, appointment_time):
        self.appointments.append({
            'doctor_name': doctor_name,
            'appointment_date': appointment_date,
            'appointment_time': appointment_time
        })
    
    def get_details(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'contact': self.contact,
            'appointments': self.appointments
        }
        
class ClinicManagementSystem:
    def __init__(self):
        self.patients = []
        
    def add_patient(self, name, age, gender, contact):
        patient = Patient(name, age, gender, contact)
        self.patients.append(patient)
        print(f"Patient {name} added successfully.")
        
    def schedule_appointment(self, patient_name, date, time, doctor):
        for patient in self.patients:
            if patient.name == patient_name:
                patient.add_appointment(doctor, date, time)
                print(f"Appointment for {patient_name} scheduled on {date} at {time} with Dr. {doctor}")
                return
        
        print(f"No patient found with the name {patient_name}.")
    
    def view_patient_details(self, patient_name):
        for patient in self.patients:
            if patient.name == patient_name:
                details = patient.get_details()
                print(f"Patient Details: \nName: {details['name']}")
                print(f"Age: {details['age']}")
                print(f"Gender: {details['gender']}")
                print(f"Contact: {details['contact']}")
                print("Appointments: ")
                for appointment in details['appointments']:
                    print(f"  Doctor: {appointment['doctor_name']}, Date: {appointment['appointment_date']}, Time: {appointment['appointment_time']}")
                return
        
        print(f"No patient found with the name {patient_name}.") 

def main():
    cms = ClinicManagementSystem()         
    
    while True:
        print("\nClinic Management System")
        print("1. Add patient")
        print("2. Schedule Appointment")
        print("3. View Patient Details")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            contact = input("Enter patient contact: ")
            
            cms.add_patient(name, age, gender, contact)
            
        elif choice == "2":
            name = input("Enter patient name: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            doctor = input("Enter doctor name: ")
            
            cms.schedule_appointment(name, date, time, doctor)
            
        elif choice == "3":
            name = input("Enter patient name: ")
            cms.view_patient_details(name)
        
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
         