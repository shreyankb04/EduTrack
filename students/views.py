from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Student, Course
from .forms import StudentForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):

    students = Student.objects.all().order_by('-id')

    search_query = request.GET.get('search', '')

    if search_query:
        students = students.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query)
        )

    context = {
        'students': students,
        'total_students': Student.objects.count(),
        'total_courses': Course.objects.count(),
        'search_query': search_query
    }

    return render(request, 'students/dashboard.html', context)

@login_required
def add_student(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Add New Student'
    })

@login_required
def edit_student(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Edit Student'
    })

@login_required
def delete_student(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('dashboard')

    return render(request, 'students/delete_confirm.html', {
        'student': student
    })

@login_required
def course_list(request):

    courses = Course.objects.all().order_by('name')

    return render(request, 'students/course_list.html', {
        'courses': courses
    })


@login_required
def add_course(request):

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()

        if name:
            Course.objects.create(
                name=name,
                description=description
            )

            return redirect('course_list')

    return render(request, 'students/course_form.html')