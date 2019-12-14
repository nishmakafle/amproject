from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.views.generic import *
from datetime import datetime
from .models import *
from .forms import *


class LoginView(FormView):
    template_name = 'amapp/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        self.username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        self.user = authenticate(username=self.username,
                                 password=password)
        if self.user is not None and self.user.is_superuser is False:
            login(self.request, self.user)

        elif self.user is not None and self.user.is_superuser is True:
            login(self.request, self.user)
        else:
            return render(self.request, self.template_name, {
                'form': form,
                'errors': "Please correct username or password"})

        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        if self.request.user.groups.filter(name='Teacher').exists():
            return reverse('amapp:teacherhome')
        elif self.request.user.groups.filter(name='Student').exists():
            return reverse('amapp:studenthome')
        elif self.request.user.groups.filter(name='Admin').exists():
            return reverse('amapp:adminhome')
        else:
            return reverse('amapp:login')


class LogoutView(View):
    login_url = reverse_lazy('amapp:login')

    def get(self, request):
        logout(request)
        return redirect('amapp:login')


class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        u = request.user
        if u.is_authenticated and u.groups.filter(name="Admin").exists():
            pass
        else:
            return redirect('amapp:login')

        return super().dispatch(request, *args, **kwargs)


class AdminHomeView(AdminRequiredMixin, TemplateView):
    template_name = "admintemplates/adminhome.html"


class AdminTeacherListView(AdminRequiredMixin, ListView):
    template_name = "admintemplates/adminteacherlist.html"
    queryset = Teacher.objects.all()
    context_object_name = "teacherlist"


class AdminTeacherRegistrationView(AdminRequiredMixin, CreateView):
    template_name = "admintemplates/adminteacherregistration.html"
    form_class = TeacherForm
    success_url = reverse_lazy('amapp:adminteacherlist')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        return super().form_valid(form)


class AdminTeacherUpdateView(AdminRequiredMixin, UpdateView):
    template_name = 'admintemplates/adminteacherregistration.html'
    form_class = TeacherUpdateForm
    model = Teacher
    success_url = reverse_lazy('amapp:adminteacherlist')


class AdminTeacherDeleteView(AdminRequiredMixin, DeleteView):
    template_name = 'admintemplates/adminteacherdelete.html'
    model = Teacher
    success_url = reverse_lazy('amapp:adminteacherlist')


class AdminStudentListView(AdminRequiredMixin, ListView):
    template_name = "admintemplates/adminstudentlist.html"
    queryset = Student.objects.all()
    context_object_name = "studentlist"


class AdminTeacherDetailView(AdminRequiredMixin, DetailView):
    template_name = "admintemplates/adminteacherdetail.html"
    model = Teacher
    context_object_name = "teacher"


class AdminStudentRegistrationView(AdminRequiredMixin, CreateView):
    template_name = "admintemplates/adminstudentregistration.html"
    form_class = StudentForm
    success_url = reverse_lazy('amapp:adminstudentlist')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        return super().form_valid(form)


class AdminStudentUpdateView(AdminRequiredMixin, UpdateView):
    template_name = 'admintemplates/adminstudentregistration.html'
    form_class = StudentUpdateForm
    model = Student
    success_url = reverse_lazy('amapp:adminstudentlist')


class AdminStudentDeleteView(AdminRequiredMixin, DeleteView):
    template_name = 'admintemplates/adminstudentdelete.html'
    model = Student
    success_url = reverse_lazy('amapp:adminstudentlist')


class AdminProgramCreateView(AdminRequiredMixin, CreateView):
    template_name = 'admintemplates/adminprogramcreate.html'
    form_class = ProgramForm
    success_url = reverse_lazy('amapp:adminprogramlist')


class AdminProgramListView(AdminRequiredMixin, ListView):
    template_name = 'admintemplates/adminprogramlist.html'
    model = Program
    context_object_name = 'progarmlist'


class AdminClassRoomCreateView(AdminRequiredMixin, CreateView):
    template_name = 'admintemplates/adminclassroomcreate.html'
    form_class = ClassRoomForm
    success_url = reverse_lazy('amapp:adminclassroomlist')


class AdminClassRoomListView(AdminRequiredMixin, ListView):
    template_name = 'admintemplates/adminclassroomlist.html'
    model = ClassRoom
    context_object_name = 'classroomlist'


class TeacherRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        u = request.user
        if u.is_authenticated and u.groups.filter(name="Teacher").exists():
            pass
        else:
            return redirect('amapp:login')

        return super().dispatch(request, *args, **kwargs)


class TeacherHomeView(TeacherRequiredMixin, TemplateView):
    template_name = 'teachertemplates/teacherhome.html'


class TeacherAssignmentCreateView(TeacherRequiredMixin, CreateView):
    template_name = 'teachertemplates/teacherassignmentcreate.html'
    form_class = AssignmnetForm
    success_url = reverse_lazy('amapp:teacherhome')

    def form_valid(self, form):
        form.instance.teacher = Teacher.objects.get(user=self.request.user)
        return super().form_valid(form)


class TeacherAssignmentListView(TeacherRequiredMixin, ListView):
    template_name = 'teachertemplates/teacherassignmentlist.html'
    model = Assignment
    context_object_name = 'assignmentlist'


class TeacherAssignmentUpdate(TeacherRequiredMixin, UpdateView):
    template_name = 'teachertemplates/teacherassignmentcreate.html'
    form_class = AssignmnetForm
    model = Assignment
    success_url = reverse_lazy('amapp:teacherassignmnetlist')


class TeacherAssignmentDeleteView(TeacherRequiredMixin, DeleteView):
    template_name = 'teachertemplates/teacherassignmentdelete.html'
    model = Assignment
    success_url = reverse_lazy('amapp:teacherassignmnetlist')


class TeacherAssignmentDetailView(TeacherRequiredMixin, DetailView):
    template_name = "teachertemplates/teacherassignmentdetail.html"
    model = Assignment
    context_object_name = "teacherassignment"


class TeacherReviewView(TeacherRequiredMixin, UpdateView):
    template_name = "teachertemplates/teacherreview.html"
    form_class = TeacherReviewForm
    model = Submission

    def get_success_url(self):
        am = Submission.objects.get(id=self.kwargs['pk']).assignment
        return reverse('amapp:teacherassignmentdetail',
                       kwargs={"pk": am.id})

# Student Views


class StudentRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        u = request.user
        if u.is_authenticated and u.groups.filter(name="Student").exists():
            self.student = request.user.student
        else:
            return redirect('amapp:login')

        return super().dispatch(request, *args, **kwargs)


class StudentHomeView(StudentRequiredMixin, TemplateView):
    template_name = 'studenttemplates/studenthome.html'


class StudentAssignmentListView(StudentRequiredMixin, ListView):
    template_name = "studenttemplates/studentassignmentlist.html"
    queryset = Assignment.objects.all()
    context_object_name = "studentassignments"

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        return qs.filter(class_room=self.student.class_room)


class StudentAssignmentStartView(StudentRequiredMixin, TemplateView):
    template_name = "studenttemplates/studentassignmentstart.html"

    def dispatch(self, request, *args, **kwargs):
        # get assignment
        self.assignment = Assignment.objects.get(id=self.kwargs['pk'])
        # get student
        self.student = request.user.student
        # check whether the student has started the assigment or not
        if self.student.submission_set.filter(assignment=self.assignment).exists():
            # if existst get that submission object
            submission = self.student.submission_set.filter(
                assignment=self.assignment).first()
            return redirect(reverse("amapp:studentsubmissiondetail",
                                    kwargs={'pk': submission.id}))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        submission = Submission.objects.create(
            assignment=self.assignment,
            assignment_status="Started",
            student=self.student)
        context['submission'] = submission

        return context


class StudentSubmissionDetailView(StudentRequiredMixin, DetailView):
    template_name = "studenttemplates/studentsubmissiondetail.html"
    model = Submission
    context_object_name = "submission"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        return context


class StudentFileUploadView(StudentRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        submission = Submission.objects.get(id=self.kwargs['sub_id'])
        file = request.FILES['submisison_file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        submission.file = uploaded_file_url
        submission.assignment_status = "Completed"
        submission.file_upload_date = datetime.now()
        submission.save()

        return redirect(reverse("amapp:studentsubmissiondetail",
                                kwargs={'pk': submission.id}))
