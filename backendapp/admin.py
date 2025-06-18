from django.contrib import admin
from .models import Role,Staff,Specialization,Doctor,Membership,Patient,Appointment,MedicineCategory,Medicine,MedicinePrescription,Consultation,MedicineStock,LabTestCategory,LabTest,LabTestPrescription

# Register your models here.
admin.site.register(Role)
admin.site.register(Staff)
admin.site.register(Specialization)
admin.site.register(Doctor)
admin.site.register(Membership)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicineCategory)
admin.site.register(Medicine)
admin.site.register(MedicinePrescription)
admin.site.register(Consultation)
admin.site.register(MedicineStock)
admin.site.register(LabTestCategory)
admin.site.register(LabTest)
admin.site.register(LabTestPrescription)