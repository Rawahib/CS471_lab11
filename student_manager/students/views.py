from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Address, Student2, Address2, StudentProfile
from .forms import StudentForm, AddressForm, Student2Form, Address2Form,StudentProfileForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        address_form = AddressForm(request.POST)
        
        if student_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            student = student_form.save(commit=False)
            student.address = address
            student.save()
            return redirect('student_list')
    else:
        student_form = StudentForm()
        address_form = AddressForm()
    
    return render(request, 'students/student_form.html', {
        'student_form': student_form,
        'address_form': address_form,
    })

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    address = student.address
    
    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student)
        address_form = AddressForm(request.POST, instance=address)
        
        if student_form.is_valid() and address_form.is_valid():
            address_form.save()
            student_form.save()
            return redirect('student_list')
    else:
        student_form = StudentForm(instance=student)
        address_form = AddressForm(instance=address)
    
    return render(request, 'students/student_form.html', {
        'student_form': student_form,
        'address_form': address_form,
    })

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.address.delete()  # Delete the associated address
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})



# New views for many-to-many relationship
def student2_list(request):
    students = Student2.objects.all().prefetch_related('addresses')
    return render(request, 'students/student2_list.html', {'students': students})

def student2_create(request):
    if request.method == 'POST':
        student_form = Student2Form(request.POST)
        if student_form.is_valid():
            student = student_form.save()
            return redirect('student2_list')
    else:
        student_form = Student2Form()
    
    return render(request, 'students/student2_form.html', {
        'student_form': student_form,
    })

def student2_update(request, pk):
    student = get_object_or_404(Student2, pk=pk)
    if request.method == 'POST':
        student_form = Student2Form(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('student2_list')
    else:
        student_form = Student2Form(instance=student)
    
    return render(request, 'students/student2_form.html', {
        'student_form': student_form,
    })

def student2_delete(request, pk):
    student = get_object_or_404(Student2, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student2_list')
    return render(request, 'students/student2_confirm_delete.html', {'student': student})

def address2_create(request):
    if request.method == 'POST':
        address_form = Address2Form(request.POST)
        if address_form.is_valid():
            address_form.save()
            return redirect('student2_list')
    else:
        address_form = Address2Form()
    
    return render(request, 'students/address2_form.html', {
        'address_form': address_form,
    })




def student_profile_create(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.student = student
            profile.save()
            return redirect('student_list')
    else:
        form = StudentProfileForm()
    
    return render(request, 'students/student_profile_form.html', {
        'form': form,
        'student': student,
    })

def student_profile_update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    profile = get_object_or_404(StudentProfile, student=student)
    
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentProfileForm(instance=profile)
    
    return render(request, 'students/student_profile_form.html', {
        'form': form,
        'student': student,
    })

def student_profile_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    try:
        profile = StudentProfile.objects.get(student=student)
    except StudentProfile.DoesNotExist:
        return redirect('student_profile_create', student_id=student.id)
    
    return render(request, 'students/student_profile_view.html', {
        'student': student,
        'profile': profile,
    })